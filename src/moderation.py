from openai import OpenAI

from src.types import ModerationResponse


def moderate(url_content: str) -> ModerationResponse:
    client = OpenAI()

    reponse = client.moderations.create(
        model="omni-moderation-latest",
        input=url_content,
    )

    return ModerationResponse(
        flagged=reponse.results[0].flagged,
        categories=[
            reason
            for reason, flag in reponse.results[0].categories.model_dump().items()
            if flag is True
        ],
    )
