# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 7:47 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : models.py
# @Software : PyCharm
import _asyncio

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

bind = create_async_engine("mysql+aiomysql://root:@localhost:3306/test")
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