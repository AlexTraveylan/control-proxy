from pathlib import Path

from openai.types import ModerationModel

WORKSPACE_DIR = Path(__file__).parents[1]

RESOURCE_DIR = WORKSPACE_DIR / "resources"

BLACKLIST_FILE = RESOURCE_DIR / "blacklist.txt"

HTML_BLOCKED_FILE = RESOURCE_DIR / "blocked_template.html"

MODERATION_MODEL: ModerationModel = "omni-moderation-latest"
