# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 1:12 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : bisd.py
# @Software : PyCharm
from sanic import json


async def get_info():
    return json({"name":"leiyh","age":"18","type":"bim"})