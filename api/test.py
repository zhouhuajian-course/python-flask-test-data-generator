"""
测试数据接口

@author  : zhouhuajian
@version : v1.0
"""
import re
import time

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



@bp.route('/api/test/timestamp', methods=['POST'])
def timestamp():
    """转时间戳接口"""
    r = {"success": 1, "message": "生成成功", "data": ""}
    try:
        # 2023-12-01 00:00:00
        date_time = request.form.get('date_time', '')
        date_time = date_time.strip()
        print(date_time)
        if not date_time:
            # 当前时间的时间戳
            data = time.time()
        else:
            # 2023-12-01 00:00:00
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', date_time):
                raise ValueError("请输入正确的日期时间格式，例如2023-12-01 00:00:00")
            # 根据用户提供的日期时间来转时间戳
            struct_time = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
            # 命名元组
            print(struct_time)
            data = time.mktime(struct_time)
        print(data)
        data = int(data)
        # TODO: 写入到数据库
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r
