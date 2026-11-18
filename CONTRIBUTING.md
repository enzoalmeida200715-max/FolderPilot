# Contributing to FolderPilot

This project is early in its development. Small, reproducible improvements are
welcome. Before changing behaviour, describe the problem and expected result
in an issue in the repository where this code is published.

1. Use Python 3.11 or newer. No third-party runtime or test dependency is needed.
2. Work on a branch and test with disposable folders.
3. Run `python -m unittest discover -s tests -v`.
4. For file-operation changes, include a regression test covering preservation
   of the original data and collision behaviour.
5. Describe what changed, how you tested it and any limitations in the pull request.

Keep preview read-only. Never add an overwrite or recursive deletion as a
silent fallback. Preserve incomplete-operation recovery and refuse links and
path traversal in history. Avoid adding telemetry or uploading user files.

Useful contributions include GUI accessibility, Windows tests, translations,
better error messages, selective moves and configurable extension rules.
Discuss scope before adding cloud services or AI dependencies.

AI-assisted contributions are welcome when reviewed and understood by their
submitter. Share the actual tests run; do not fabricate results or usage data.

For a security-sensitive report, use GitHub private vulnerability reporting if
the maintainer has enabled it. Otherwise post a minimal issue asking for a
private contact without including secrets or exploit details. Reports must
not include private file contents, credentials or personal folder listings.
