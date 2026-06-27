from dataclasses import dataclass
from typing import Optional

@dataclass
class ProcessInfo:
    pid: int
    ppid: Optional[int]
    name: str
    cmdline: str
    user: Optional[str]
    create_time: Optional[float]
    exe: Optional[str]

@dataclass
class Alert:
    severity: str
    rule_name: str
    pid: int
    name: str
    cmdline: str
    matched_value: str
