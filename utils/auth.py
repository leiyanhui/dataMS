# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 11:17 下午
# @Author  : leiyh
# @Email   : leiyh0104@163.com
# @File    : auth.py
# @Software : PyCharm
from functools import wraps
from sanic_token_auth import SanicTokenAuth
import jwt
from sanic import Sanic
from sanic.response import text


def check_token(request):
    """ 校验token是否有效 """
    try:
        jwt.encode(request.headers.get('token'), request.app.config.SECRET, algorithms=["HS256"])
    except Exception as e:
        return False
    else:
        return True


def login_required(wrapped):
    """ token校验装饰器 """

    def decorator(func):
        @wraps(func)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated = check_token(request)

            if is_authenticated:
                response = await func(request, *args, **kwargs)
                return response
            else:
                return text("token无效", 401)

        return decorated_function

    return decorator(wrapped)


app = Sanic("AuthApp")
auth = SanicTokenAuth(app, secret_key='utee3Quaaxohh1Oo', header='X-My-App-Auth-Token')
app.config.SECRET = "KEEP_IT_SECRET_KEEP_IT_SAFE"


@app.post("/login")
async def login(request):
    print(request.args)
    token = jwt.encode(request.args, request.app.config.SECRET)
    return text(token)


@app.get("/secret")
@login_required
async def secret(request):
    return text("已登录，可继续操作")

@app.route("/")
async def index(request):
    return text("Go to /protected")


@app.route("/protected")
@auth.auth_required
async def protected(request):
    return text("Welcome!")


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
    app.run(host='0.0.0.0', port=8000, debug=True)