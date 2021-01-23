from pydantic import BaseModel
import enum

class Team(enum.Enum):

    home ="home"
    away = "away"

