#!/usr/bin/env sh
set -eu
# Usage: sh reproduce.sh /absolute/path/to/lean
# Run in this directory. Only the Lean executable and ordinary shell tools are used.
lean_executable=$1
"$lean_executable" --version
sha256sum -c inputs.sha256
cat EvidenceLogic.lean Case.lean > replay.lean
"$lean_executable" replay.lean
