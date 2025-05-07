import os
import google_auth_httplib2
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from datetime import datetime, time, timedelta
import json


def authenticate_youtube():
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    TOKEN_FILE = 'token.json'
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

    # Load client secrets file, put the path of your file
    client_secrets_file = "yt_client.json"

    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, SCOPES)
    credentials = flow.run_local_server()

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    return youtube

def upload_video(youtube):
    today = datetime.today()
    tomorrow = (datetime.now() + timedelta(days=1)).date()


    date_only = today.date()

    time_10am = datetime.combine(date_only, time(17, 0)).strftime("%Y-%m-%dT%H:%M:%SZ")
    time_1pm = datetime.combine(date_only, time(20, 0)).strftime("%Y-%m-%dT%H:%M:%SZ")
    time_6pm = datetime.combine(tomorrow, time(1, 0)).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open("./output/vid_details.json", "r", encoding="utf-8") as file:
        vid_details = json.load(file)
    print(vid_details)
    print(f"Video title: {vid_details['title']}")
    print(type(vid_details["title"]))
    
    request_body = {
        "snippet": {
            "categoryId": "22",
            "title": vid_details["title"],
            "description": "Top Reddit stories from AITA subreddit",
            "tags": ["redditstories","minecraftgameplay", "AITA" ],
            "thumbnails": {
                "default": {
                    "url": "./output/thumbnail.png",
                }
            }
        },
        "status":{
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
            'publishAt': time_6pm,
            

        }
    }

    # put the path of the video that you want to upload
    media_file = "./output/final_video.mp4"

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True)
    )

    response = None 

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress()*100)}%")

        print(f"Video uploaded with ID: {response['id']}")

# if __name__ == "__main__":
#     youtube = authenticate_youtube()
#     upload_video(youtube)