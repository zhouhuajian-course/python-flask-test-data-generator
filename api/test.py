"""
测试数据接口

@author  : zhouhuajian
@version : v1.0
"""
from flask import Blueprint

bp = Blueprint('bp', __name__)

@bp.route('/api/test/text', methods=['POST'])
def text():
    r = {"success": 1, "message": "生成成功", "data": ""}
    try:
        # raise Exception("请输入正确的长度")
        pass
    except Exception as e:
        r['success'] = 0
        r['message'] = str(e)
    return r
