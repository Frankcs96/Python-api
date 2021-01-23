from pydantic import BaseModel,Field
class Score(BaseModel):

    home: int = Field(0,ge=0)
    away: int = Field(0,ge=0)
    