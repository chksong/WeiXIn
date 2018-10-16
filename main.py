# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:53:43 2018

@author: Administrator
"""

import asyncio
from   aiohttp import web
import hashlib


def get_update(token, timestamp, nonce):
    arguments = ''
    for k in sorted([token, timestamp, nonce]):
        arguments = arguments + str(k)
    
    m = hashlib.sha1()
    m.update(arguments.encode('utf8'))
    return m.hexdigest()

def check_signature(request):
    signature = request.query['signature']  
    timestamp = request.query['timestamp']
    nonce     = request.query['nonce']
    token = "iaski_www_token"   #请按照公众平台官网\基本配置中信息填写
#    print("timestamp(%s), nonce:(%s) echostr(%s)" %(timestamp, nonce, echostr))
    
    hashcode = get_update(token, timestamp, nonce)
    print("[check_signature]: hashcode(%s), signature:(%s)" %(hashcode, signature))
    return True if hashcode == signature else False


async def getWX(request):
    
    echostr   = request.query['echostr']
    if check_signature(request):
        return web.Response(body = echostr.encode('utf-8'))

    


def __name():
    app = web.Application()
    app.router.add_route('GET', '/wx',getWX)
    web.run_app(app,port=4131)

if __name__ == '__main__':
    __name()