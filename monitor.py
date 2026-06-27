import time
from .collector import collect_processes
from .config import Config
from .evaluator import evaluate_process
from .output import print_alert, alert_to_json

def monitor(config: Config) -> None:
    seen = {}
    ignore = set(n.lower() for n in (config.ignore_process_names or []))

    while True:
        current = collect_processes()
        new_pids = set(current) - set(seen)

        for pid in new_pids:
            proc = current[pid]
            if proc.name.lower() in ignore:
                continue

            alerts = evaluate_process(proc, enabled_rules=config.enabled_rules)
            for alert in alerts:
                if config.json_output:
                    print(alert_to_json(alert))
                else:
                    print_alert(alert)

        seen = current
        time.sleep(config.interval)
