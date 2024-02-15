import googleapiclient.discovery
import pprint as pprint
from pydantic import ValidationError
from yt_search_api_pydantic import YoutubeSearchResponse
from airflow.decorators import task, dag
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
  
  @task
  def get_search_terms():
      # placeholder task for search term input retrieval
      return ["grandmother", "performance", "diamond"]

  api_service_name = "youtube"
  api_version = "v3"
  DEVELOPER_KEY = developer_key

  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

  request = youtube.search().list(
    part='snippet',
    q='trump',
    maxResults=1,
    order='date',
    type='video'
  )

  respose = request.execute()

  try:
    pprint.pprint(YoutubeSearchResponse(**respose).model_dump())
  except ValidationError as e:
      pprint.pprint(e.errors())
      
youtube_search_collection()