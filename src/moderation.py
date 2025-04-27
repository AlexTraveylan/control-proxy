from openai import OpenAI
from openai.types import ModerationModel

from src import constants, types_module


def moderate(
    cleaned_url_content: str,
    model: ModerationModel = constants.MODERATION_MODEL,
) -> types_module.ModerationResponse:
    client = OpenAI()

    reponse = client.moderations.create(
        model=model,
        input=cleaned_url_content,
    )

    return types_module.ModerationResponse(
        flagged=reponse.results[0].flagged,
        categories=[
            reason
            for reason, flag in reponse.results[0].categories.model_dump().items()
            if flag is True
        ],
    )
