from fastapi import FastAPI

from routers import chat
from src.agent_models import OutreachTarget
from src.vaani import outreach

app = FastAPI()

# app.include_router(chat.router)


@app.post("/suggest-speaker", response_model=dict)
async def outreach_start(target: OutreachTarget):
    outreach(target, send_mail=True)
    return {}
