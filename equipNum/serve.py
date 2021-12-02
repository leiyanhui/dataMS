# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:49 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : serve.py
# @Software : PyCharm

from sanic import Blueprint
from utils.utils import location_url

devices = Blueprint('devices',url_prefix='/devices')

@devices.route('/<urlString>')
async def bp_root(request,urlString):
    method = "get"
    if request.method == "POST":
        method = "post"
    response =  await location_url(method, f"equipNum-{urlString}",request.args)
    return response