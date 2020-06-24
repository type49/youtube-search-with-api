# YouTube Video Searching

A simple library for finding videos on YouTube.
Uses YouTube -api to search.

Returns a list of videos with a dictionary in which the id, title and description of the video, the name and id of the channel, the date of publication and thumbnails.

# Install 
```bash
pip install youtube-search-with-api
```
# Usage

```python
 from youtube_search_with_api import YoutubeSearch

a = YoutubeSearch('backing track', 50).to_dict()

#first arg - search request, second - results count

```
