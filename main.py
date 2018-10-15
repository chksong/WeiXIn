# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:53:43 2018

@author: Administrator
"""

import asyncio
from   aiohttp import web


async def getWX(request):
    echostr = 'success'
    try:
        echostr = request.query['echostr']   
    except Exception as ea:
    	pass
    return web.Response(body=echostr.encode('utf-8'))


def __name():
    app = web.Application()
    app.router.add_route('GET', '/wx',getWX)
    web.run_app(app,port=4131)

if __name__ == '__main__':
    __name()