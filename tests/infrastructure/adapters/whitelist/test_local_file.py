from pathlib import Path

import pytest
from pytest import TempPathFactory

from src.infrastructure.adapters import whitelist


@pytest.fixture
def mock_whitelist_file(tmp_path_factory: TempPathFactory) -> Path:
    header = "domain_display_name,domain_url,who_authorizes"
    mock_line = "Youtube_Kid,youtube.com/kids,Timothee"

    whitelist_file = tmp_path_factory.mktemp("whitelist") / "whitelist.csv"
    whitelist_file.write_text(f"{header}\n{mock_line}", encoding="utf-8")
    return whitelist_file


@pytest.mark.parametrize(
    "domain, expected",
    [
        ("youtube.com/kids", True),
        ("youtube.com", False),
        ("https://youtube.com/kids", True),
        ("", False),
        ("*", False),
        ("test.com", False),
    ],
)
def test_local_file_whitelist_is_whitelisted(
    mock_whitelist_file: Path,
    domain: str,
    expected: bool,
):
    # Given fixtures

    # When
    adapter = whitelist.LocalFileWhitelist(mock_whitelist_file)
    is_authorized = adapter.is_whitelisted(domain)

    # Then
    assert is_authorized is expected


def test_local_file_whitelist_get_domains(mock_whitelist_file: Path):
    # Given fixture

    # When
    adapter = whitelist.LocalFileWhitelist(mock_whitelist_file)
    domains = adapter.get_domains()

    # Then
    assert len(domains) == 1
    assert domains[0].domain_display_name == "Youtube_Kid"
    assert domains[0].domain_url == "youtube.com/kids"
    assert domains[0].who_authorizes == "Timothee"
