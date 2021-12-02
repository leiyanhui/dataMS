# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:49 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : serve.py
# @Software : PyCharm

from sanic import Blueprint
from utils.utils import location_url

bim = Blueprint('bim',url_prefix='/bim')

@bim.route('/<urlString>')
async def bp_root(request,urlString):
    method = "get"
    if request.method == "POST":
        method = "post"
    response =  await location_url(method, f"bim-{urlString}",request.args)
    return response