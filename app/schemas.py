#PyDantic models (Data type validation)

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogEntry(BaseModel):
   service_name:str
   level:str
   message:str
   timestamp: Optional[datetime] = None

