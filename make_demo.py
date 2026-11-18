"""Create a new folder of disposable example files. Never overwrite a demo."""
from pathlib import Path
import zipfile


def main():
    folder = Path(__file__).resolve().parent / "demo-sandbox"
    try:
        folder.mkdir()
    except FileExistsError:
        print("demo-sandbox already exists. Rename it if you want another fresh demo.")
        return 1
    (folder / "lembrete.txt").write_text("Comprar pão e organizar as fotografias.\n", encoding="utf-8")
    (folder / "despesas.csv").write_text("item,euros\ncaderno,2.50\ncaneta,1.20\n", encoding="utf-8")
    (folder / "desenho.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="180" height="120"><rect width="180" height="120" fill="#193b57"/><circle cx="90" cy="60" r="35" fill="#41d1b7"/></svg>', encoding="utf-8")
    with zipfile.ZipFile(folder / "exemplo.zip", "w") as archive:
        archive.writestr("readme.txt", "A disposable FolderPilot example.")
    print(f"Demo ready: {folder}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
