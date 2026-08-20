#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "ifortyninestack"
MANIFEST = PLUGIN_ROOT / ".cursor-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"
FRONTMATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$")
FORBIDDEN_QUALITY_BAR_PHRASES = (
    "senior-ready",
    "ready for senior review",
    "boss-ready",
    "review-ready",
    "before senior review",
    "a senior reviewer will accept",
    "a senior will send back",
    "fix before senior review",
)
FORBIDDEN_COMPANY_PHRASES = (
    "ordinal",
    "breakground",
    "heroku",
    "municipal",
    "reducto",
    "scrapingbee",
    "eng-###",
    "cycle tracking -",
)


def frontmatter(path):
    text = path.read_text()
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return None

    values = {}
    for line in match.group(1).splitlines():
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def validate_manifest(errors):
    try:
        manifest = json.loads(MANIFEST.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{MANIFEST.relative_to(ROOT)}: {error}")
        return

    if manifest.get("name") != "ifortyninestack":
        errors.append(
            "plugins/ifortyninestack/.cursor-plugin/plugin.json: name must be ifortyninestack"
        )

    for field in ("description", "version", "author", "skills", "agents", "rules"):
        if not manifest.get(field):
            errors.append(
                f"plugins/ifortyninestack/.cursor-plugin/plugin.json: missing {field}"
            )


def validate_marketplace(errors):
    try:
        marketplace = json.loads(MARKETPLACE.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{MARKETPLACE.relative_to(ROOT)}: {error}")
        return

    if marketplace.get("name") != "ifortyninestack":
        errors.append(".cursor-plugin/marketplace.json: invalid marketplace name")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        errors.append(".cursor-plugin/marketplace.json: expected one plugin")
        return

    plugin = plugins[0]
    if plugin.get("name") != "ifortyninestack":
        errors.append(".cursor-plugin/marketplace.json: missing ifortyninestack entry")
    if plugin.get("source") != "ifortyninestack":
        errors.append(".cursor-plugin/marketplace.json: invalid ifortyninestack source")


def validate_components(errors):
    components = {
        "rules": sorted((PLUGIN_ROOT / "rules").glob("*.mdc")),
        "skills": sorted((PLUGIN_ROOT / "skills").glob("*/SKILL.md")),
        "agents": sorted((PLUGIN_ROOT / "agents").glob("*.md")),
    }
    names = {}

    for component, paths in components.items():
        if not paths:
            errors.append(f"{component}: no component files found")
            continue

        for path in paths:
            metadata = frontmatter(path)
            relative_path = path.relative_to(ROOT)
            if metadata is None:
                errors.append(f"{relative_path}: missing YAML frontmatter")
                continue

            if not metadata.get("description"):
                errors.append(f"{relative_path}: missing description")

            if component == "rules":
                if "alwaysApply" not in metadata:
                    errors.append(f"{relative_path}: missing alwaysApply")
                continue

            name = metadata.get("name")
            if not name:
                errors.append(f"{relative_path}: missing name")
            elif not NAME_PATTERN.fullmatch(name):
                errors.append(f"{relative_path}: invalid name {name!r}")
            elif name in names:
                errors.append(
                    f"{relative_path}: duplicate name also used by {names[name]}"
                )
            else:
                names[name] = relative_path

            if component == "skills" and len(path.read_text().splitlines()) > 500:
                errors.append(f"{relative_path}: SKILL.md exceeds 500 lines")

    return components


def validate_links_and_style(errors):
    prose_paths = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        *sorted((ROOT / "docs").glob("*.md")),
        *sorted((PLUGIN_ROOT / "rules").glob("*.mdc")),
        *sorted((PLUGIN_ROOT / "skills").glob("**/*.md")),
        *sorted((PLUGIN_ROOT / "agents").glob("*.md")),
    ]

    for path in prose_paths:
        text = path.read_text()
        relative_path = path.relative_to(ROOT)

        if "—" in text:
            errors.append(f"{relative_path}: contains an em dash")

        lowered = text.lower()
        for phrase in FORBIDDEN_QUALITY_BAR_PHRASES:
            if phrase in lowered:
                errors.append(
                    f"{relative_path}: quality bar must be merge-ready, not {phrase!r}"
                )

        for phrase in FORBIDDEN_COMPANY_PHRASES:
            if phrase in lowered:
                errors.append(
                    f"{relative_path}: company-specific phrase {phrase!r} is not allowed"
                )

        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if clean_target and not (path.parent / clean_target).exists():
                errors.append(f"{relative_path}: broken link {target}")


def main():
    errors = []
    validate_manifest(errors)
    validate_marketplace(errors)
    components = validate_components(errors)
    validate_links_and_style(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    counts = ", ".join(
        f"{component}={len(paths)}" for component, paths in components.items()
    )
    print(f"OK: ifortyninestack plugin is valid ({counts})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
