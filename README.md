# FolderPilot

**Preview your file moves. Organise a folder. Undo when needed.**

FolderPilot is a small, offline Python utility for organising a personal data
folder into Images, Documents, Audio, Videos and Archives. It includes a
Portuguese desktop interface and an English command line.

This is version **0.1.0**, a new project developed with AI assistance. There are
no established adoption figures, downloads or community metrics to report.
The first release deliberately focuses on a small, working feature set.

## Why this exists

Manual sorting is repetitive. FolderPilot offers a lightweight, inspectable
workflow for people who want to see the proposed moves before applying them.
It does not require an account, an AI subscription or a network connection.
It is one approach to file organisation, not a claim that other organisers do
not already exist.

## Start on Windows

1. Install Python **3.11 or newer** from <https://www.python.org/downloads/>.
   Ensure the Python launcher or the `python` command is available.
2. Extract the entire project ZIP into a folder.
3. Double-click **START_WINDOWS.bat**.
4. Choose a personal data folder, click **Pré-visualizar**, review the moves,
   then click **Organizar** and confirm.
5. **Desfazer última organização** restores the last batch when the recorded
   files have not been edited and their original names are available.

There is no `pip install` step for normal use. The desktop UI needs Tkinter.
Use `py -3 -m tkinter` to check it. For Portuguese instructions, read
[COMECA_AQUI.md](COMECA_AQUI.md).

## Try it on demo files first

From the extracted project directory:

```powershell
py -3 make_demo.py
py -3 -m folderpilot preview demo-sandbox
py -3 -m folderpilot organize demo-sandbox --apply
py -3 -m folderpilot undo demo-sandbox --yes
```

The demo script creates a new `demo-sandbox` folder and refuses to overwrite an
existing one. It creates a text note, a CSV, an SVG and a ZIP; these are local
sample files rather than personal data.

## Command line

```text
python -m folderpilot preview "PATH_TO_FOLDER"
python -m folderpilot preview "PATH_TO_FOLDER" --json
python -m folderpilot organize "PATH_TO_FOLDER"
python -m folderpilot organize "PATH_TO_FOLDER" --apply
python -m folderpilot undo "PATH_TO_FOLDER" --yes
python -m folderpilot gui
python -m folderpilot --version
```

`organize` without `--apply` is only a preview. `undo` without `--yes` makes no
changes. On macOS/Linux, use `python3` or `sh start.sh`. Some Linux Python
installations provide Tkinter in a separate distribution package; the CLI does
not require Tkinter.

## Behaviour

| Situation | Behaviour |
| --- | --- |
| Preview | Reads names, metadata and SHA-256 hashes; creates no files or folders. |
| Existing destination name | Plans `name (2).ext`, `name (3).ext`, etc. |
| File changed after preview | Refuses the stale plan or leaves that file untouched. |
| Existing subfolder | Does not recursively scan or move its contents. |
| Hidden/system file, link or reparse point | Skips it; category links are refused. |
| Unknown extension or incomplete download | Leaves it where it is. |
| Source-code project folder | Refuses common project roots to avoid reorganising a repository. |
| Undo with edited content | Reports the conflict and preserves the edited file. |
| Undo with occupied original name | Reports the conflict and preserves both files. |
| No history | Reports nothing to undo. |

Files are classified by **extension**, not by their contents. Renaming a file
extension does not convert or validate the file. Empty category directories
remain after undo. Repeated undo calls restore earlier batches in reverse order.

## Filesystem requirements and limits

- Use a local folder you own. Do not run concurrent organisers or edit files
  while an operation is running. Active sync clients and shared directories
  have not been validated.
- A move creates an exclusive hard link, then removes the old directory entry.
  Both locations must be on a filesystem supporting hard links. If hard-link
  creation fails, the original stays in place; there is no copy/delete fallback.
- Collision checks and exclusive link creation avoid replacing existing files.
  This tool is not a sandbox against hostile concurrent local processes.
- Undo depends on the `.folderpilot` history directory and the original root
  path. Moving or renaming the whole parent folder is not supported by undo.
- File hashes require reading each eligible file. Preview can take time on
  large video folders or slow disks. The desktop stays responsive.
- The history helps recover ordinary interruptions. It is not a backup or a
  guarantee against disk failure or sudden power loss. Try disposable files
  first and retain backups for important data.
- No recursive organisation, duplicate deletion, cloud sync, AI integration,
  automatic background scheduling or compiled Windows executable is included.

## History and interruption recovery

Each batch is recorded in `.folderpilot/run-*.json` before any file moves.
History is local and contains paths, sizes and content hashes, never file
contents. Normal completion updates the history after each file.

If a run is interrupted, reopen the app and use undo. If it reports an active
lock, first confirm that **all FolderPilot processes have stopped**. Then remove
only `.folderpilot/operation.lock` inside the affected folder and retry undo.
Do not remove history JSON files. Undo checks the actual files, including a
possible interruption between creating a new hard link and removing the old
one. It preserves conflicts for manual review.

If a crash leaves several matching journal entries or the history is damaged,
stop and review the files before continuing. Do not edit journal paths to point
at another folder.

## Development and validation

```text
python -m unittest discover -s tests -v
python -m compileall -q folderpilot tests
```

Tests use temporary directories only. See [VALIDATION.md](VALIDATION.md) for
what was actually run. CI is configured for Windows, Linux and macOS with
Python 3.11 and 3.13; that configuration is not evidence of a successful remote
CI run until the repository has been published and Actions has completed.

Optional installation as a package: `python -m pip install .`. This packaging
route may download setuptools; it is not required to run from the source folder.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Useful next steps include real Windows
desktop testing, accessibility improvements, translations, file selection
within a preview, and custom rules. These are planned improvements, not shipped
features.

Licensed under the [MIT License](LICENSE).

## Reference documentation

- [Python and Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python `os.link`](https://docs.python.org/3/library/os.html#os.link)
- [Publishing files to GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [GitHub Actions checkout](https://github.com/actions/checkout)
- [GitHub Actions Python setup](https://github.com/actions/setup-python)
