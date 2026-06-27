from process_guard.models import ProcessInfo
from process_guard.evaluator import evaluate_process

def test_enabled_rules_filter():
    proc = ProcessInfo(1, None, "powershell", "powershell -enc AAAA", None, None, None)
    alerts = evaluate_process(proc, enabled_rules=["temp_execution"])
    assert alerts == []

def test_evaluator_returns_alert_for_enabled_rule():
    proc = ProcessInfo(1, None, "powershell", "powershell -enc AAAA", None, None, None)
    alerts = evaluate_process(proc, enabled_rules=["encoded_command"])
    assert len(alerts) == 1
    assert alerts[0].rule_name == "encoded_command"
