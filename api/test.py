"""
测试数据接口

@author  : zhouhuajian
@version : v1.0
"""
from flask import Blueprint, request
import string
import random

bp = Blueprint('bp', __name__)

CHARS = string.ascii_letters + string.digits + "零一二三四五六七八九"
EMOJIS = "😀😃😄😁😆"


@bp.route('/api/test/text', methods=['POST'])
def text():
    """生成测试文本数据接口"""
    r = {"success": 1, "message": "生成成功", "data": ""}
    try:
        size = request.form.get('size', 0, int)
        print("用户提供的长度为" + str(size))
        if size <= 0:
            raise ValueError("请输入正确的长度")
        data = ''.join(random.choices(CHARS, k=size))
        # TODO: 写入到数据库
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r


@bp.route('/api/test/emoji', methods=['POST'])
def emoji():
    """生成测试表情数据接口"""
    r = {"success": 1, "message": "生成成功", "data": ""}
    try:
        size = request.form.get('size', 0, int)
        print("用户提供的长度为" + str(size))
        if size <= 0:
            raise ValueError("请输入正确的长度")
        data = ''.join(random.choices(EMOJIS, k=size))
        # TODO: 写入到数据库
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r
