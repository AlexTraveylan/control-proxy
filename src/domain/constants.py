from pathlib import Path

WORKSPACE_DIR = Path(__file__).parents[2]

RESOURCE_DIR = WORKSPACE_DIR / "resources"

WHITELIST_FILE = RESOURCE_DIR / "whitelist.csv"

HTML_BLOCKED_FILE = RESOURCE_DIR / "blocked_template.html"

CSV_SEPARATOR = ","
