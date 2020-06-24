# YouTube Video Searching

A simple library for finding videos on YouTube.
Uses YouTube -api to search.

Returns a list of videos with a dictionary in which the id, title and description of the video, the name and id of the channel, the date of publication and thumbnails.

# Install 
```bash
pip install youtube-video-search-with-api
```
# Usage

```python
 from youtube-video-search-with-api import YoutubeSearch

YT_API = 'YOUR API'

#first arg - search request, second - results count, third - api key
a = YoutubeSearch('backing track', 50, YT_API).to_dict()

#return json string
a = YoutubeSearch('backing track', 50, YT_API).to_json()


```
