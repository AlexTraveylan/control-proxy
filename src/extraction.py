import re

import nltk
import requests
from bs4 import BeautifulSoup

nltk.download("punkt")


def format_pretty_url(pretty_url: str) -> str:
    return f"https://{pretty_url}"


def extract_main_content(url: str) -> dict[str, str]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.find("title")
        title = title_element.get_text() if title_element else "Titre non trouvé"

        for element in soup(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header",
                "aside",
                "meta",
                "form",
                "iframe",
                "noscript",
            ]
        ):
            element.decompose()

        main_content = (
            soup.find("main")
            or soup.find("article")
            or soup.find("div", {"id": re.compile("content|main|article", re.I)})
        )
        if main_content:
            elements = main_content.find_all_next(
                ["p", "h1", "h2", "h3", "h4", "h5", "li"]
            )
        else:
            elements = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "li"])

        textes = [
            elem.get_text().strip()
            for elem in elements
            if len(elem.get_text().strip()) > 20
        ]
        text = "\n".join(textes)

        return {"title": title, "text": text, "url": url}

    except Exception as e:
        return {
            "title": "Erreur lors de l'extraction",
            "text": f"Impossible d'extraire le contenu: {str(e)}",
            "url": url,
        }
