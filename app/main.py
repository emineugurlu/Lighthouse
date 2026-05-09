#API endpoint
from fastapi import FastAPI
from app.schemas import LogEntry
import datetime

app = FastAPI(title="Lighthouse Log Collector")

@app.post("/ingest")
async def ingest_log(log:LogEntry):
    if not log.timestamp:
        log.timestamp=datetime.datetime.now()

    print(f"[{log.level}]{log.service_name}: {log.message}")
    return {"status": "recived","timestamp": log.timestamp}