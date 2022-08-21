### Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

### Basic Requirements:
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimised.


### Endpoint details:
API Type | API Endpoint | Function |
---------| ------------ | -------- |
GET | /vidoes/ | Get all the video details.
GET | /vidoes?query={query_term} | Get all the video details with optional query parameter to fetch only videos which has given query term in video title or description.
GET | /videos?p_size=5&page=2 | Get data paginated with 5 records size and of page number 2.
GET | /videos?query=sport&p_size=5&page=2 | Get data which has sport in title or description and paginated with 5 records size and of page number 2.

### DashBoard
Created DashBoard for Video Data. You can view, search, filter, update and  delete records. Run app and open `http://127.0.0.1:8000/admin/api/videodetail/` in browser.

### Environment/Backend Setup
 - Add your YouTube API_KEY to keys.json file. You can add multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
 - Add your query in settings.py - Optional (default = 'video')
 - Fetching data using youtube api each minutes. Can be changed in settings.py
 - `docker build -t fampay .`
 - `docker run -it -d -p 8000:80 fampay` Print container ID
 - `docker exec -it <-put container ID here-> /bin/sh` Get interactive shell to container 

 


#### Django
 - `python manage.py runserver`
 - Go to http://127.0.0.1:8000/videos/




### Reference:
- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old