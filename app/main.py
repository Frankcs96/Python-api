from fastapi import FastAPI

from app.models.Score import Score
from app.models.Goal import Goal
from app.models.Team import Team

app = FastAPI()


# We are storing the data in memory so we will lose the score when the server shuts down.
# live_match will be where we will store the score information.

live_match = Score()


## Endpoints


@app.post("/goal", response_model=Score)
async def post_goal(goal: Goal):
    if goal.team == Team.away:
        live_match.away += 1
        return live_match
    if goal.team == Team.home:
        live_match.home += 1
        return live_match



@app.get("/score" , response_model=Score)
async def get_score():
    return {"away": live_match.away, "home":live_match.home}
    

    