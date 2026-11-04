# Offline example catalog

Open `index.html` directly in a browser. No web server, network, JavaScript, or fetch is needed.

Regenerate from the repository root after cloning, without the original temporary workspaces:

```sh
python validation/publish_examples.py
python validation/publish_examples.py --check
```

The generator automatically reuses additional runs listed in the previous publication inventory from their committed `raw/runs/` snapshots. An equivalent explicit command is:

```sh
python validation/publish_examples.py --extra-run 11-report-derived-criteria-mixed=docs/examples/raw/runs/11-report-derived-criteria-mixed --extra-run 11-report-derived-criteria-correct=docs/examples/raw/runs/11-report-derived-criteria-correct --extra-run 12-empty-evidence-correct=docs/examples/raw/runs/12-empty-evidence-correct --extra-run 12-empty-evidence-mixed=docs/examples/raw/runs/12-empty-evidence-mixed
```

To refresh a snapshot from a retained workspace, pass `--extra-run ID=tmp/WORKSPACE` for each additional run to include. Original workspace provenance is preserved when rebuilding from the published snapshots.

`raw/` contains byte-preserving snapshots; `view/` provides escaped text or native previews. `publication-integrity.json` records source paths and SHA-256 hashes. Original manifests are preserved unchanged. The publication inventory excludes itself to avoid a recursive hash. Native document originals, SQLite indexes, and proof logs are retained; toolchain/build caches, symlinks and fixture authoring masters are excluded. Evaluator expectations are in a separate after-audit study area.

This generator reports stored results and never executes Lean, re-audits a claim, or declares a legacy bundle compliant with v2. Running the same command against unchanged inputs produces the same files. Working directories under `tmp/` are not changed or deleted.
