from setuptools import setup

setup(name='youtube-video-search-with-api',
      version='1.0',
      description='Search video in YouTube',
      long_description="""# YouTube Video Searching

A simple library for finding videos on YouTube.
Uses YouTube -api to search.

Returns a list of videos with a dictionary in which the id, title and description of the video, the name and id of the channel, the date of publication and thumbnails.

# Usage

```python
 from youtube-video-search-with-api import YoutubeSearch

YT_API = 'YOUR API'

#first arg - search request, second - results count, third - api key
a = YoutubeSearch('backing track', 50, YT_API).to_dict()

#return json string
a = YoutubeSearch('backing track', 50, YT_API).to_json()


```
""",
      long_description_content_type='text/markdown',
      packages=['youtube-video-search-with-api'],
      author_email='underalmaty@gmail.com',
      zip_safe=False)
