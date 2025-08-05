from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal
from langgraph.graph.message import add_messages
from typing import List, Annotated


## Create a state class
class State(BaseModel):
    """
    Represents the structure of the state used in graph
    """
    message:Annotated[List, add_messages] = Field(
        description= 'List of messages'
    )
    