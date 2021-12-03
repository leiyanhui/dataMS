# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 1:12 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : bim.py
# @Software : PyCharm
from sqlalchemy import select
from utils.models import User


async def get_info(request):
    session= request.ctx.session
    async with session.begin():
        result = await session.execute(select(User).where(User.name == request.args.get("name")))
        user = result.scalar()
        return {'code': 200,'message':"查询成功","data":user.to_dict()if user else {}}

async def post_info(request):
    session = request.ctx.session
    get_data = await get_info(request)
    if get_data.get('data',None).get("name") is None:
        async with session.begin():
            user = User(**request.args)
            session.add(user)
        return user.to_dict()
    else:
        return {"message":"the name has been exist!"}
