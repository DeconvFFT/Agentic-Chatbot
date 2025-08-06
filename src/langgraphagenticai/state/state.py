from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal
from langgraph.graph.message import add_messages
from typing import List, Annotated,Optional


## Create a state class
class State(TypedDict):
    """
    Represents the structure of the state used in graph
    """
    messages:Annotated[List, add_messages]

# class State(BaseModel):
#     """
#     Represents the structure of the state used in graph
#     """
#     messages:Annotated[List, add_messages] = Field(
#         description= 'List of messages'
#     )
#     frequency: Annotated[str, add_messages] = Field(
#         description='Frequency of messages'
#     )
#     news_data: List[dict] = Field(
#         description='News data scrapped using Tavily Search'
#     )
#     summary: Annotated[List, add_messages] = Field(
#         description='Summary of the news data stored in news_data field'
#     )
#     filename: Annotated[str, add_messages] = Field(
#         description="File name to store summary of AI news"
#     )