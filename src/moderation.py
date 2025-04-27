import requests
from openai import OpenAI
from openai.types import ModerationModel

from src import constants, types


def content_from_pretty_url(pretty_url: str) -> str:
    try:
        response = requests.get(pretty_url, timeout=10)
    except requests.exceptions.RequestException as e:
        raise e

    return response.text


def moderate(
    url_content: str,
    model: ModerationModel = constants.MODERATION_MODEL,
) -> types.ModerationResponse:
    client = OpenAI()

    reponse = client.moderations.create(
        model=model,
        input=url_content,
    )

    return types.ModerationResponse(
        flagged=reponse.results[0].flagged,
        categories=[
            reason
            for reason, flag in reponse.results[0].categories.model_dump().items()
            if flag is True
        ],
    )
