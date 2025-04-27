import logging

from mitmproxy import http

from src import blacklist, constants, logs

logs.init_logger()
logger = logging.getLogger(__name__)


def request(flow: http.HTTPFlow) -> None:
    print(flow.request.pretty_url)
    logger.info(f"Request received: {flow.request.pretty_url}")
    host = flow.request.pretty_host.lower()

    if blacklist.BLACK_LIST.is_blocked(host) is True:
        with open(constants.HTML_BLOCKED_FILE, "r", encoding="utf-8") as f:
            html_template = f.read()
        html_content = html_template.replace("{{url}}", flow.request.pretty_url)

        flow.response = http.Response.make(
            403,
            html_content.encode("utf-8"),
            {"Content-Type": "text/html; charset=utf-8"},
        )
        logger.info(f"Blocked request: {flow.request.pretty_url}")
