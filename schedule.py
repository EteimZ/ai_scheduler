from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
from typing import Dict

from pydantic import BaseModel

class Schedule(BaseModel):
    title: str
    description: str
    datetime: datetime

@dataclass
class ScheduleDB:
    id: int = 1
    schedules: Dict[int, Schedule] = field(default_factory=lambda: defaultdict(list))

    def list(self):
        """
        Get lists of schedules
        """
        resp = {}
        for i, schedule in enumerate(self.schedules):
            resp[i] = self.schedules[i].model_dump_json()
        return resp
    
    def add(self, schedule: Schedule):
        self.schedules[self.id] = schedule
        self.id += 1
    
    def __getitem__(self, id):
        """
        Get a schedule
        """
        
        return { id : self.schedules[id].model_dump_json()}

    def __delitem__(self, id):
        """
        Delete a schedule
        """
        del self.schedules[id]

    def update_datetime(self, id, date_time):
        self.schedules[id].datetime = date_time

    def update_title(self, id, title):
        self.schedules[id].title = title

    def update_description(self, id, descr):
        self.schedules[id].description = descr