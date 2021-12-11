# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 7:47 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : models.py
# @Software : PyCharm
from asyncio import current_task

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_scoped_session
from sqlalchemy.orm import declarative_base

async_session_factory = create_async_engine("mysql+aiomysql://root:@localhost:3306/test")
# AsyncSession = async_scoped_session(async_session_factory, scopefunc=current_task)
# some_async_session = AsyncSession()
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, comment='id，主键')


class User(BaseModel):
    """ 用户表 """
    __tablename__ = "user"
    name = Column(String(64), comment='名字',unique=True)
    age = Column(Integer, comment='年龄')
    __mapper_args__ = {"eager_defaults": True}

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}


if __name__ == '__main__':
    pass