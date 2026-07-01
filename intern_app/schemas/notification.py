from enum import Enum
from pydantic import BaseModel

class ChannelEnum(str, Enum):
    sms = "SMS"
    email = "Email"
    push = "Push"

class StatusEnum(str, Enum):
    pending = "Pending"
    sent = "Sent"
    failed = "Failed"