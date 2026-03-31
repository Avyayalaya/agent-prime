#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python 3.10+ is required to run Agent Prime first-time setup."
  exit 1
fi

exec "$PYTHON_BIN" "$ROOT_DIR/meta/scripts/first_run.py" "$@"
