from dataclasses import dataclass
from pathlib import Path
import tomllib

@dataclass
class Config:
    interval: float = 2.0
    json_output: bool = False
    enabled_rules: list[str] | None = None
    ignore_process_names: list[str] | None = None

def load_config(path: str | None = None) -> Config:
    cfg = Config()
    if not path:
        return cfg

    data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    section = data.get("process_guard", {})
    cfg.interval = float(section.get("interval", cfg.interval))
    cfg.json_output = bool(section.get("json_output", cfg.json_output))
    cfg.enabled_rules = section.get("enabled_rules", None)
    cfg.ignore_process_names = section.get("ignore_process_names", None)
    return cfg
