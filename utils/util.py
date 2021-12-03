# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:58 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : util.py
# @Software : PyCharm
from importlib import import_module

async def location_url(method, stringUrl,args):
    """

    :param stringUrl:
    :return:
    """
    packName,modelName,fileName, funcName = stringUrl.split("-")
    funcName = f"{method}_{funcName}"
    obj = import_module(f"{packName}.{modelName}s.{fileName}",funcName)
    func = getattr(obj,funcName)
    return await func(args)