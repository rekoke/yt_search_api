import googleapiclient.discovery
import pprint as pprint
from pydantic import ValidationError
from yt_search_api_pydantic import YoutubeSearchResponse

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyB4k7kt7Ka4D32VwwNtR8ewCFt7ZkPPyLU"

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