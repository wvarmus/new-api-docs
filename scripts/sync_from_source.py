from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "文档"

CHINESE_NUMERALS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
}


def chapter_key(name: str):
    match = re.match(r"^([一二三四五六七八九十]+)、", name.strip())
    if match:
        return (0, CHINESE_NUMERALS.get(match.group(1), 999), name)
    return (1, 999, name)


def file_key(name: str):
    stripped = name.strip()
    match = re.match(r"^(\d+)", stripped)
    if match:
        return (0, int(match.group(1)), stripped)
    return (1, stripped)


def chapter_dirs(root: Path):
    return sorted(
        [p for p in root.iterdir() if p.is_dir() and p.name != "scripts"],
        key=lambda p: chapter_key(p.name),
    )


def transform_markdown(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "<br />", text, flags=re.IGNORECASE)
    return text


def sync_docs():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source docs directory not found: {SOURCE}")

    source_chapters = chapter_dirs(SOURCE)
    source_names = {chapter.name for chapter in source_chapters}

    for existing in chapter_dirs(ROOT):
        if existing.name in source_names:
            shutil.rmtree(existing, ignore_errors=True)

    for chapter in source_chapters:
        target_chapter = ROOT / chapter.name
        shutil.copytree(chapter, target_chapter)
        for md in target_chapter.glob("*.md"):
            md.write_text(transform_markdown(md.read_text(encoding="utf-8")), encoding="utf-8")


def build_docs_json():
    groups = [{"group": "首页", "pages": ["index"]}]

    for chapter in chapter_dirs(ROOT):
        files = sorted(chapter.glob("*.md"), key=lambda p: file_key(p.stem))
        pages = [f"{chapter.name}/{file.stem}" for file in files]
        groups.append({"group": chapter.name, "pages": pages})

    docs = {
        "$schema": "https://mintlify.com/docs.json",
        "theme": "mint",
        "name": "无限星河 AI 文档",
        "colors": {"primary": "#4f46e5"},
        "navigation": {"groups": groups},
    }

    (ROOT / "docs.json").write_text(
        json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    sync_docs()
    build_docs_json()
    print("synced mintlify mirror")


if __name__ == "__main__":
    main()
