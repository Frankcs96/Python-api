from pydantic import BaseModel
class Score(BaseModel):

    home: int = 0
    away: int = 0
    