# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 1:12 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : bim.py
# @Software : PyCharm
from sanic import json


async def get_info(*args):
    return json({"name":"leiyh","age":"18","type":"bim"})

async def post_info(*args):
    print('//////////////',args)
    return json({"name":"leiyh","age":"18","type":"bim"})