#!/usr/bin/env bash
# Regenerates the package from openapi.json and fails if it differs from the committed code.
set -euo pipefail
cd "$(dirname "$0")/.."
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
python -m pip install -q openapi-python-client==0.29.1
openapi-python-client generate --path openapi.json --config codegen/config.yml --meta pdm --output-path "$T/gen" --overwrite --fail-on-warning >/dev/null
mkdir -p "$T/gen/codegen" && cp codegen/* "$T/gen/codegen/"
SHA=$(python -c 'import tomllib;print(tomllib.load(open("pyproject.toml","rb"))["tool"]["nextfarm"]["spec-sha256"])')
VER=$(python -c 'import tomllib;print(tomllib.load(open("pyproject.toml","rb"))["project"]["version"])')
[ "$(shasum -a 256 openapi.json | cut -c1-64)" = "$SHA" ] || { echo "openapi.json does not match spec-sha256 in pyproject.toml"; exit 1; }
bash "$T/gen/codegen/finish.sh" "$T/gen" "$VER" "$SHA"
diff -r -x __pycache__ "$T/gen/nextfarm_sdk" nextfarm_sdk
diff "$T/gen/pyproject.toml" pyproject.toml
echo "generated code matches openapi.json"
