from typing import Callable, Optional, Tuple
from .models import ProcessInfo

RuleResult = Tuple[bool, str, str]
RuleFn = Callable[[ProcessInfo], RuleResult]

def rule_encoded_command(proc: ProcessInfo) -> RuleResult:
    cmd = proc.cmdline.lower()
    if "base64" in cmd or "-enc" in cmd or "encodedcommand" in cmd:
        return True, "high", "possible encoded command"
    return False, "", ""

def rule_temp_execution(proc: ProcessInfo) -> RuleResult:
    cmd = proc.cmdline.lower()
    if "\\temp\\" in cmd or "/tmp/" in cmd or "/downloads/" in cmd:
        return True, "medium", "execution from temp/downloads path"
    return False, "", ""

def rule_suspicious_scripting(proc: ProcessInfo) -> RuleResult:
    cmd = proc.cmdline.lower()
    if any(x in cmd for x in ["powershell", "bash", "sh", "python", "wscript", "cscript"]):
        if any(x in cmd for x in ["curl", "wget", "invoke-webrequest", "downloadstring"]):
            return True, "high", "scripting tool downloading content"
    return False, "", ""

RULE_REGISTRY: dict[str, RuleFn] = {
    "encoded_command": rule_encoded_command,
    "temp_execution": rule_temp_execution,
    "suspicious_scripting": rule_suspicious_scripting,
}
