import googleapiclient.discovery
import pprint as pprint
from pydantic import ValidationError
from yt_search_api_pydantic import YoutubeSearchResponse
from airflow.decorators import dag
import pendulum
import os

developer_key = os.environ["DEVELOPER_KEY"]

@dag(
  schedule=None,
  start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
  catchup=False,
  tags=["youtube"],
)

def youtube_search_collection():
  
  def get_search_terms():
    return ["trump", "palestine", "apple vision"]
    
  def get_search_results(_search_query):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = developer_key
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
      part='snippet',
      q=_search_query,
      maxResults=1,
      order='date',
      type='video'
    )

    response = request.execute()

    try:
      return _search_query, YoutubeSearchResponse(**response).items[0].snippet.title
    except ValidationError as e:
        pprint.pprint(e.errors())
        
  _search_terms = get_search_terms()
  _search_results = dict(map(get_search_results, _search_terms))
  pprint.pprint(_search_results)
      
youtube_search_collection()