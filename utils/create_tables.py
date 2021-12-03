# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 7:48 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : create_tables.py
# @Software : PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 导入相应的模块
from utils.models import Base

engine = create_engine("mysql+pymysql://root:@localhost:3306/test")

# 创建session对象
session = sessionmaker(engine)()

# 创建表，执行所有BaseModel类的子类
Base.metadata.create_all(engine)

# 提交，必须
session.commit()