# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:53:43 2018

@author: Administrator
"""

import asyncio
from aiohttp import web
import re



def __name():
    loop = asyncio.get_event_loop();
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/wx',getWX)
    loop.close()


if __name__ == '__main__':
    __name()