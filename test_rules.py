from process_guard.models import ProcessInfo
from process_guard.rules import rule_encoded_command

def test_encoded_command():
    proc = ProcessInfo(1, None, "powershell", "powershell -enc AAAA", None, None, None)
    matched, severity, reason = rule_encoded_command(proc)
    assert matched
    assert severity == "high"
    assert reason
