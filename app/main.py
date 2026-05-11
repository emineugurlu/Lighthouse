from fastapi import FastAPI, BackgroundTasks
from app.schemas import LogEntry
from app.utils import send_to_queue # Burası utils.py ile birebir aynı olmalı
import datetime

app = FastAPI()

@app.post("/ingest")
async def ingest_log(log: LogEntry, background_tasks: BackgroundTasks):
    if not log.timestamp:
        log.timestamp = datetime.datetime.now()

    # Arka planda çalışması için asistana devrediyoruz
    background_tasks.add_task(send_to_queue, log)

    return {"status": "success", "detail": "Log kuyruğa alındı"}