# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:53:43 2018

@author: Administrator
"""

import asyncio
from   aiohttp import web


async def getWX(request):
    return "hello, this is handle view"


def __name():
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/wx',getWX)
    web.run_app(app)

if __name__ == '__main__':
    __name()