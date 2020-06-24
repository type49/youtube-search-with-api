from pprint import pprint
from googleapiclient.discovery import build
import json


class YoutubeSearch:
    def __init__(self, search_request: str, max_results=None, api=None):
        self.youtube = build('youtube', 'v3', developerKey=api)
        self.search_request = search_request
        self.max_results = max_results
        self.videos = self.search()

    def search(self):
        req = self.youtube.search().list(q=self.search_request, part='snippet', type='video', maxResults=self.max_results)
        res = req.execute()
        results = []
        for item in res['items']:
            results.append({item['id']['videoId']:
                                [[item['snippet']['title'],
                                  item['snippet']['description'],
                                  item['snippet']['channelTitle'],
                                  item['snippet']['channelId'],
                                  item['snippet']['publishedAt']],
                                 [
                                     item['snippet']['thumbnails']['default']['url'],
                                     item['snippet']['thumbnails']['medium']['url'],
                                     item['snippet']['thumbnails']['high']['url']
                                 ]]})

        return results

    def to_dict(self):
        return self.videos

    def to_json(self):
        return json.dumps({"videos": self.videos})
