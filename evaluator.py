from typing import List, Optional
from .models import Alert, ProcessInfo
from .rules import RULE_REGISTRY

def evaluate_process(proc: ProcessInfo, enabled_rules: Optional[list[str]] = None) -> List[Alert]:
    alerts: List[Alert] = []
    allowed = set(enabled_rules) if enabled_rules else set(RULE_REGISTRY.keys())

    for rule_name, rule_fn in RULE_REGISTRY.items():
        if rule_name not in allowed:
            continue
        matched, severity, reason = rule_fn(proc)
        if matched:
            alerts.append(
                Alert(
                    severity=severity,
                    rule_name=rule_name,
                    pid=proc.pid,
                    name=proc.name,
                    cmdline=proc.cmdline,
                    matched_value=reason,
                )
            )
    return alerts
