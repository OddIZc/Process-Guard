from typing import Dict
import psutil
from .models import ProcessInfo

def collect_processes() -> Dict[int, ProcessInfo]:
    procs: Dict[int, ProcessInfo] = {}
    for p in psutil.process_iter(["pid", "ppid", "name", "cmdline", "username", "create_time", "exe"]):
        try:
            info = p.info
            cmdline = " ".join(info.get("cmdline") or [])
            procs[info["pid"]] = ProcessInfo(
                pid=info["pid"],
                ppid=info.get("ppid"),
                name=info.get("name") or "",
                cmdline=cmdline,
                user=info.get("username"),
                create_time=info.get("create_time"),
                exe=info.get("exe"),
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procs
