from dataclasses import dataclass
from datetime import datetime

from logic.stamps.base_stamp import BaseStamp


@dataclass
class TimeStamp(BaseStamp):
    """
    object that holds a time stap and additional info about the function
    """
    start:datetime
    end:datetime
    format:str ="%Y-%m-%d %H:%M:%S.%f"

    @staticmethod
    def init_from_bytes(split_desc_string):
        """
        init date time from a string
        """
        if len(split_desc_string) > 0:
            id = split_desc_string[0]
            name = split_desc_string[1]
            file_name=split_desc_string[2]
            thread_id=split_desc_string[3]
            start = datetime.strptime(split_desc_string[4], TimeStamp.format)
            end = datetime.strptime(split_desc_string[5], TimeStamp.format)

            return TimeStamp(id=id,name=name,file_name=file_name,thread_id=thread_id,start=start,end=end)
    def __lt__(self, other):

        if self.start < other.start:
            return True
        elif self.start == other.start:
            if self.end - self.start <  other.end - other.start:
                return True