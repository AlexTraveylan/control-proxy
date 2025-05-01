import logging

from mitmproxy import http

from src.domain import constants
from src.infrastructure import logs
from src.infrastructure.adapters import whitelist

logs.init_logger()
logger = logging.getLogger(__name__)

whitelist_adapter = whitelist.LocalFileWhitelist(constants.WHITELIST_FILE)


def request(flow: http.HTTPFlow) -> None:
    print(f"Request received: {flow.request.pretty_url}")
    logger.info("Request received: %s", flow.request.pretty_url)
    host = flow.request.pretty_host.lower()

    if whitelist_adapter.is_whitelisted(host) is False:
        with open(constants.HTML_BLOCKED_FILE, "r", encoding="utf-8") as f:
            html_template = f.read()
        html_content = html_template.replace("{{url}}", flow.request.pretty_url)

        flow.response = http.Response.make(
            403,
            html_content.encode("utf-8"),
            {"Content-Type": "text/html; charset=utf-8"},
        )
        logger.info("Blocked request: %s", flow.request.pretty_url)
