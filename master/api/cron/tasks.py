from api.models import VideoDetail
import requests
from requests.models import Response
from datetime import datetime, timezone, timedelta
import json
import os
from django.conf import settings

def dummy():
    print('Scheduled Task')

def background_job():
    search_query = settings.BACKGROUND_JOB['query']
    fetchInterval = settings.BACKGROUND_JOB['fetchInterval']
    developer_keys_path = os.path.join(settings.BASE_DIR, 'keys.json')

    with open(developer_keys_path, 'rb') as keys_file:
        DEVELOPER_KEYS_OBJECT = json.load(keys_file)
        DEVELOPER_KEYS = DEVELOPER_KEYS_OBJECT["youtube_api_keys"]

    part = "snippet"
    maxResults = 50
    order = "date"
    publishedAfter = get_time_stamp(fetchInterval)
    count = 0

    try:
        '''
        Support for supplying multiple API keys so that if quota is exhausted on one, new API_KEY will be picked up
        automatically from the list of API Keys provided in settings.py
        '''
        for developer_key in DEVELOPER_KEYS:
            "For Multiple keys"
            response = fetch_data(developer_key=developer_key,
                    part=part,
                    maxResults=maxResults,
                    search_query=search_query,
                    order=order,
                    publishedAfter=publishedAfter
            )

            if response.status_code == 400:
                '''
                if request results in 400, then new API_KEY will be picked up
                '''
                print(f"{developer_key} Expired.")
                continue

            if response.status_code == 200:
                '''
                If status is 200 then new entries are made in VideoDetail table
                '''
                count = 0
                for item in response.json()["items"]:
                    try:
                        video = VideoDetail(
                            title=item["snippet"]["title"],
                            description=item["snippet"]["description"],
                            published_datetime=item["snippet"]["publishedAt"],
                            thumbnail_url=item["snippet"]["thumbnails"]["default"]["url"],
                            video_id=item["id"]["videoId"],
                            channel_name=item["snippet"]["channelTitle"],
                            channel_id=item["snippet"]["channelId"],
                        )
                        video.save()
                        count += 1
                    except Exception as e:
                        print("Something wrong happened.")
                        continue
                break

    except Exception as e:
        print("Error: ", str(e))

    print(f"Database updated with {count} new entries of {search_query}")


def get_time_stamp(fetchInterval):
    utc_past_hour = datetime.utcnow() + timedelta(minutes=-fetchInterval)
    my_time = str(utc_past_hour.replace(tzinfo=timezone.utc)).split(' ')
    return f"{my_time[0]}T{my_time[1][:-6]}Z"


def fetch_data(developer_key: str, part: str, order: str, search_query: str, maxResults: int,
               publishedAfter: str) -> Response:
    url = f"https://youtube.googleapis.com/youtube/v3/search?" \
          f"part={part}&" \
          f"maxResults={maxResults}&" \
          f"order={order}&" \
          f"publishedAfter={publishedAfter}&" \
          f"q={search_query}&" \
          f"key={developer_key}"

    return requests.get(url=url)




