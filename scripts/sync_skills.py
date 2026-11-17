#!/usr/bin/env python3
"""Synchronise les skills du plug-in avec leurs repos GitHub d'origine.

Lit scripts/sources.txt, télécharge la dernière version de chaque repo source,
remplace le dossier du skill dans plugins/cvd-marketing-skills/skills/, puis
augmente la version du plug-in si quelque chose a changé.

Usage : python3 scripts/sync_skills.py
"""
import filecmp
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "scripts" / "sources.txt"
PLUGIN = ROOT / "plugins" / "cvd-marketing-skills"
SKILLS = PLUGIN / "skills"
PLUGIN_JSON = PLUGIN / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".claude-plugin" / "marketplace.json"
IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc")


def read_sources():
    entries = []
    for line in SOURCES.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, repo, path = (part.strip() for part in line.split("|"))
        entries.append((name, repo, path))
    return entries


def dirs_differ(a: Path, b: Path) -> bool:
    if not a.exists() or not b.exists():
        return True
    cmp = filecmp.dircmp(a, b, ignore=[".DS_Store", "__pycache__"])
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return True
    return any(dirs_differ(a / d, b / d) for d in cmp.common_dirs)


def bump_patch(version: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    return f"{major}.{minor}.{patch + 1}"


def main() -> int:
    entries = read_sources()
    repos = sorted({repo for _, repo, _ in entries})
    changed = []
    missing = []

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for repo in repos:
            target = tmp / repo.replace("/", "__")
            subprocess.run(
                ["git", "clone", "--quiet", "--depth=1",
                 f"https://github.com/{repo}.git", str(target)],
                check=True,
            )

        for name, repo, path in entries:
            src = tmp / repo.replace("/", "__") / path
            dst = SKILLS / name
            if not (src / "SKILL.md").exists():
                missing.append(f"{name} ({repo}/{path})")
                continue
            if dirs_differ(src, dst):
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst, ignore=IGNORE)
                changed.append(name)

    if missing:
        print("Skills introuvables à la source (chemin déplacé ?) :")
        for item in missing:
            print(f"  - {item}")

    if not changed:
        print("Aucun changement.")
        return 1 if missing else 0

    plugin = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    new_version = bump_patch(plugin["version"])
    plugin["version"] = new_version
    PLUGIN_JSON.write_text(json.dumps(plugin, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    market = json.loads(MARKETPLACE_JSON.read_text(encoding="utf-8"))
    for entry in market["plugins"]:
        if entry["name"] == plugin["name"]:
            entry["version"] = new_version
    MARKETPLACE_JSON.write_text(json.dumps(market, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Version {new_version}. Skills mis à jour : {', '.join(changed)}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
