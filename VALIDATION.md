# Validation record

Date: 2026-11-18.

Verified during initial creation on Linux with Python 3.12.14:

- 32 automated tests passed using `python3 -m unittest discover -s tests -v`.
- Tests covered preview without mutations, byte-preserving move/undo, Unicode
  names, collisions, changed files, same-size edits, missing files, interrupted
  moves, journal-write failure, malformed history, path traversal, symlinks,
  active locks, multiple batches and CLI confirmation behaviour.
- A separate CLI demo previewed, organised and restored all four generated
  files, then verified SHA-256 hashes matched the originals.
- Python source compilation, Python 3.11 grammar checks and package metadata
  parsing passed. The desktop module imported successfully.

Not verified at this stage:

- Interactive use of the Tkinter window on a real desktop: the build
  environment did not have a desktop display attached.
- Actual execution on Windows or macOS.
- GitHub-hosted CI results: the workflow is supplied but not yet published/run.
- Power-loss durability, network drives, active cloud sync folders or hostile
  concurrent modification of the filesystem.

Treat 0.1.0 as an initial implementation. Try the included demo and disposable
files before using it on important documents.
