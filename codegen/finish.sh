#!/usr/bin/env bash
# Post-processing for the generated package: create_client helper, VERSION, PyPI metadata.
set -euo pipefail
P=$1; PYVER=$2; SHA=$3
PKG=$P/nextfarm_sdk
cp "$(dirname "$0")/nextfarm.py" "$PKG/nextfarm.py"
printf 'VERSION = "%s"\n' "$PYVER" > "$PKG/_version.py"
cat >> "$PKG/__init__.py" <<'PYEOF'

from ._version import VERSION
from .nextfarm import PROD_URL, SANDBOX_URL, create_client

__all__ = (*__all__, "VERSION", "PROD_URL", "SANDBOX_URL", "create_client")
PYEOF
python3 "$(dirname "$0")/patch-pyproject.py" "$P/pyproject.toml" "$SHA"
