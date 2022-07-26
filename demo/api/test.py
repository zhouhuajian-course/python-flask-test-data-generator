"""
测试接口模块

@author  : zhouhuajian
@version : v1.0
"""

import random
import re
import string
import time

from flask import Blueprint, request, jsonify
from db.database import db, TestData

# 测试接口蓝图
bp = Blueprint('bp', __name__)

# 字符
CHARS = string.ascii_letters + string.digits + "零一二三四五六七八九"

# 表情
EMOJIS = "😀😃😄😁😆"


@bp.route('/api/test/text', methods=['POST'])
def text():
    """生成测试文本"""
    r = {'success': 1, 'message': '生成成功', 'data': ''}
    try:
        size = request.form.get('size', default=0, type=int)
        if size <= 0:
            raise ValueError("请输入正确的长度")
        data = ''.join(random.choices(CHARS, k=size))
        test_data = TestData(type="text",
                             arg=size,
                             data=data)
        db.session.add(test_data)
        db.session.commit()
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r


@bp.route('/api/test/emoji', methods=['POST'])
def emoji():
    """生成测试表情"""
    r = {'success': 1, 'message': '生成成功', 'data': ''}
    try:
        size = request.form.get('size', default=0, type=int)
        if size <= 0:
            raise ValueError("请输入正确的长度")
        data = ''.join(random.choices(EMOJIS, k=size))
        test_data = TestData(type="emoji",
                             arg=size,
                             data=data)
        db.session.add(test_data)
        db.session.commit()
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r


@bp.route('/api/test/timestamp', methods=['POST'])
def timestamp():
    """转时间戳"""
    r = {'success': 1, 'message': '生成成功', 'data': ''}
    try:
        # date_time = request.form.get('date_time', default='', type=str)
        date_time = request.form.get('date_time', default='')
        date_time = date_time.strip()
        if not date_time:
            data = time.time()
        else:
            if not re.fullmatch('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', date_time):
                raise ValueError("请输入正确的时间格式，格式为YYYY-mm-dd HH:MM:SS")
            struct_time = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
            data = time.mktime(struct_time)
        data = int(data)  # 直接去掉小数 不是四舍五入
        test_data = TestData(type="timestamp",
                             arg=date_time,
                             data=data)
        db.session.add(test_data)
        db.session.commit()
        r['data'] = data
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r


@bp.route('/api/test/file', methods=['POST'])
def file():
    """生成测试文件 没有实际生成文件 下载的时候动态创建文件"""
    r = {'success': 1, 'message': '', 'data': ''}
    try:
        name = request.form.get('name', default='').strip()
        size = request.form.get('size', default='').strip()  # 10B 10K 10M 10G 10M+1B 10G+1B
        if not name or not size:
            raise ValueError("请输入文件名和文件大小")
        if ' ' in name:
            raise ValueError("文件名不能有空格")
        if not re.fullmatch('[1-9][0-9]*(B|K|M|G)(\+1B)?', size):
            raise ValueError("请输入正确的文件大小格式，例如1B、2K、3M、4G、5M+1B、6G+1B")
        test_data = TestData(type="file",
                             arg=f"{name} {size}",
                             data='')
        db.session.add(test_data)
        db.session.commit()
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r
