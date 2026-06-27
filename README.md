# Process Guard

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-pytest-purple)

A lightweight CLI tool that monitors running processes and flags suspicious command lines using simple detection rules.

## Features
- live process monitoring
- rule-based detections
- TOML config support
- JSON or readable terminal output
- enabled-rule filtering
- ignore-list support

## Example
```bash
process-guard --config config.toml
