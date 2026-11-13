# we are creating a graph & the first thing we create is a State

import os

# 1. typed DICT (Most common approach)

from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int


# 2. pydantic approach - it is good at data validation & type checking at runtime

from pydantic import BaseModel , field_validator

class State(BaseModel):
    topic : str
    summary : str
    score : int

    @field_validator
    def score_positive(cls , v):
        if v < 0:
            raise ValueError("Score must be Positive")


# 3. python dataclasses - standard python dataclass but it is used very rarely

from dataclasses import dataclass , field

@dataclass
class State:
    topic : str
    summary : str
    messages : list = field(default_factory=list)


# 4. Messages State  

from langgraph.graph import MessagesState

class State(MessagesState):
# messages field is already included with add_message reducer , just add your extra fields
    user_name : str
    language : str