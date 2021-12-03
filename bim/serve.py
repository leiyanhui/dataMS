# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:49 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : serve.py
# @Software : PyCharm

from sanic import Blueprint,response

from utils.util import location_url

bim = Blueprint('bim',url_prefix='/bim')

@bim.route('/<urlString>', methods=["GET","POST","PUT","DELETE"])
async def bp_root(request,urlString:str):
    """

    :param request:
    :param urlString:
    :return:
    """
    method = "get"
    if request.method == "POST":
        method = "post"
    resp =  await location_url(method, f"bim-{urlString}",request)
    return response.json(resp)