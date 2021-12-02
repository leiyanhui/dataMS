# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 12:49 上午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : serve.py
# @Software : PyCharm
from sanic import Sanic
from bim.serve import bim
from doors.serve import door
from drawings.serve import drawing
from equipNum.serve import devices
from timeOrd.serve import to
from hrs.serve import hr

app = Sanic(__name__)
app.blueprint((bim, door, drawing, devices, hr, to))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008, debug=True)
