# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:49 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : serve.py
# @Software : PyCharm

from sanic import Blueprint,response

from utils.util import location_url

#@bim.route('/<urlString>', methods=["GET","POST","PUT","DELETE"])
async def bp_root(request,urlString:str):
    """

    :param request: request is a request object
    :param urlString:
    :return:
    """
    methods_dict= {"POST":"post","GET":"get","PUT":"put","DELETE":"delete"}
    resp =  await location_url(methods_dict.get(request.method), f"bim-{urlString}",request)
    return response.json(resp)

bim = Blueprint('bim',url_prefix='/bim')
bim.add_route(bp_root,'/<urlString>', methods=["GET","POST","PUT","DELETE"])