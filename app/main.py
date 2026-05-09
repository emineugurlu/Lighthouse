#API endpoint
from fastapi import FastAPI,BackgroundTasks
from app.schemas import LogEntry
from app.utils import send_to_queue

app = FastAPI(title="Lighthouse Log Collector")

@app.post("/ingest")
async def ingest_log(log:LogEntry):
    if not log.timestamp:
        log.timestamp=datetime.datetime.now()

    background_tasks.add_task(send_to_queue, log)

    return {"status": "recived","timestamp": log.timestamp}