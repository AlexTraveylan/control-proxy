from pathlib import Path

TEST_DIR = Path(__file__).parents[1]

MOCK_DIR = TEST_DIR / "mocks"

RESOURCE_TEST_DIR = TEST_DIR / "resources"

WHITELIST_TEST_FILE = RESOURCE_TEST_DIR / "whitelist.csv"
