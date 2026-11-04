#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"
lean_bin="${1:-/home/salboaie/.local/share/evidence-to-proof/toolchains/lean-4.24.0-linux/bin/lean}"
# Preserve a distinct reproduction run with its own source and real output.
replay_dir="$(mktemp -d ../agent-native-replay-XXXXXX)"
cp Audit.lean "$replay_dir/Audit.lean"
"$lean_bin" --version > "$replay_dir/lean-version.log" 2>&1
set +e
"$lean_bin" "$replay_dir/Audit.lean" > "$replay_dir/lean.log" 2>&1
code=$?
set -e
printf '%s\n' "$code" > "$replay_dir/lean-exit-status.txt"
printf '%s\n' "$replay_dir"
exit "$code"
