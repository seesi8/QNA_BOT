import asyncio
from typing import Literal

from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel

from QNA import QNA_BOT


def ask(messages, q):
    class SentimentSchema(BaseModel):
        command: str
        params: list[str]
        


    SYSTEM_PROMPT = """
    You are an voice asssitant to help users.

    Respond with the following JSON schema:

    {json_schema}
    """

    
    
    real_messages = []
    
    for message in messages:
        
        real_messages.append(
            GPTMessage(
                    role=GPTMessageRole.USER if message["role"] == "user" else GPTMessageRole.ASSISTANT,
                    content=message["data"],
                )
        )
    
    real_messages.append(
            GPTMessage(
                    role=GPTMessageRole.USER,
                    content=q,
                )
        )
        
    
    async def runner():
        gpt_json = GPTJSON[SentimentSchema](
            "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", model="gpt-3.5-turbo")
        response, _ = await gpt_json.run(
            messages=[
                GPTMessage(
                    role=GPTMessageRole.SYSTEM,
                    content=SYSTEM_PROMPT,
                ),
                *real_messages
            ]
        )
        return response
    
    result = asyncio.run(runner())
    return str(result) or "sorry did'nt get that"
 
bot = QNA_BOT(ask)

bot.start_loop()