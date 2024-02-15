from pydantic import BaseModel
from typing import Annotated, Dict, List, Literal, Tuple
from annotated_types import Gt

class Default(BaseModel):
    height: int
    url: str
    width: int

class High(BaseModel):
    height: int
    url: str
    width: int

class Medium(BaseModel):
    height: int
    url: str
    width: int

class Thumbnails(BaseModel):
    default: Default
    high: High
    medium: Medium

class Snippet(BaseModel):
  channelId: str
  channelTitle: str
  description: str
  liveBroadcastContent: str
  publishTime: str
  publishedAt: str
  thumbnails: Thumbnails
  title: str
    
class Id(BaseModel):
    kind: str
    videoId: str

class YoutubeSearchItem(BaseModel):
    etag: str
    id: Id
    kind: str
    snippet: Snippet

class PageInfo(BaseModel):
    resultsPerPage: int
    totalResults: int

class YoutubeSearchResponse(BaseModel):
    etag: str
    items: list[YoutubeSearchItem]
    kind: str
    nextPageToken: str
    pageInfo: PageInfo
    regionCode: str
    
    
class Fruit(BaseModel):
    name: str  
    color: Literal['red', 'green']  
    weight: Annotated[float, Gt(0)]  
    bazam: Dict[str, List[Tuple[int, bool, float]]]  

