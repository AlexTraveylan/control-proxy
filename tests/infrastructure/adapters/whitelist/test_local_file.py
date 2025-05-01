from pytest import TempPathFactory

from src.infrastructure.adapters import whitelist


def test_local_file_whitelist_is_whitelisted(tmp_path_factory: TempPathFactory):
    # Given
    header = "domain_display_name,domain_url,who_authorizes"
    mock_line = "Youtube_Kid,youtubekids.com,Timothee"

    whitelist_file = tmp_path_factory.mktemp("whitelist") / "whitelist.csv"
    whitelist_file.write_text(f"{header}\n{mock_line}", encoding="utf-8")

    # When
    adapter = whitelist.LocalFileWhitelist(whitelist_file)
    authorized = adapter.is_whitelisted("youtubekids.com")
    not_authorized = adapter.is_whitelisted("youtube.com")

    # Then
    assert authorized is True
    assert not_authorized is False


def test_local_file_whitelist_get_domains(tmp_path_factory: TempPathFactory):
    # Given
    header = "domain_display_name,domain_url,who_authorizes"
    mock_line = "Youtube_Kid,youtubekids.com,Timothee"

    whitelist_file = tmp_path_factory.mktemp("whitelist") / "whitelist.csv"
    whitelist_file.write_text(f"{header}\n{mock_line}", encoding="utf-8")

    # When
    adapter = whitelist.LocalFileWhitelist(whitelist_file)
    domains = adapter.get_domains()

    # Then

    assert len(domains) == 1
    assert domains[0].domain_display_name == "Youtube_Kid"
    assert domains[0].domain_url == "youtubekids.com"
    assert domains[0].who_authorizes == "Timothee"
