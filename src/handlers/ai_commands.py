import openai
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


openai.api_key = "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"

router = Router()

@router.message(
    Command(commands=["ai"])
)
async def echo_ai(message: Message):
    text = message.text.split('/ai', maxsplit=1)
    print(text)
    response = await openai.Completion.acreate(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    await message.answer(response["choices"][0]["text"])