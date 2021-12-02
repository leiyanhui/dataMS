# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 1:48 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : hrs.py
# @Software : PyCharm
from sanic import json


async def get_info(*args):
    return json({"name":"leiyh","age":"18","type":"hrs"})