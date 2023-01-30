from aiogram import Router
from . import nechego_commands, posts_parser, ai_commands


commandsRouter = Router()


commandsRouter.include_router(nechego_commands.router)
commandsRouter.include_router(posts_parser.router)
commandsRouter.include_router(ai_commands.router)