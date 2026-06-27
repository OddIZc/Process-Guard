import argparse
from .config import load_config
from .monitor import monitor

def main():
    parser = argparse.ArgumentParser(description="Process Guard")
    parser.add_argument("--config", default=None, help="Path to config TOML file")
    parser.add_argument("--interval", type=float, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config)
    if args.interval is not None:
        config.interval = args.interval
    if args.json:
        config.json_output = True

    monitor(config)

if __name__ == "__main__":
    main()
