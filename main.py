from mitmproxy import http

from src.constants import BLACK_LIST, HTML_BLOCKED_FILE


def request(flow: http.HTTPFlow) -> None:
    host = flow.request.pretty_host.lower()

    if BLACK_LIST.is_blocked(host) is True:
        with open(HTML_BLOCKED_FILE, "r", encoding="utf-8") as f:
            html_template = f.read()

        html_content = html_template.replace("{{url}}", flow.request.pretty_url)

        flow.response = http.Response.make(
            403,
            html_content.encode("utf-8"),
            {"Content-Type": "text/html; charset=utf-8"},
        )
