from pydantic import BaseModel
from app.models.Team import Team
from typing import Optional

class Goal(BaseModel):

    team: Team
    player: Optional[str]