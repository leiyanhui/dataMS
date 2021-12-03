# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 9:40 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : middleWare.py
# @Software : PyCharm
from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

bind = create_async_engine("mysql+aiomysql://root:@localhost:3306/test")
_base_model_session_ctx = ContextVar("session")
async def inject_session(request) :
    '''请求中间件
    创建一个可用的Asyncsession对象并且将其鄉定至request.ctx中,
    而basemodelsessionctx也会在这是被赋子可用的值，
    如果需要在其他地方使用session对象（而非从request.ctx中取值），该全局变量或许能帮助您（它是线程安全的）'''
    request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False) ()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


async def close_session(request, mashanse):
    """啊应中间件，将创建的Asyncsession关闭。并重置_base_model_session_ctx的值，谜而释放资源"""
    if hasattr (request.ctx,"session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()
