"""
测试数据生成器

@author  : zhouhuajian
@version : v1.0
"""
import mimetypes
import os
import re
from urllib.parse import quote

from flask import Flask, render_template, make_response

from api.test import bp as api_test_bp
from db.database import db, TestData

# Flask 应用
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(api_test_bp)
db.app = app
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    """测试数据页面"""
    # 获取100条测试数据，ID倒排序
    rows = TestData.query.order_by(TestData.id.desc()).limit(100).all()
    return render_template('index.html', rows=rows)


@app.route('/file/<int:id>', methods=['GET'])
def file(id):
    """下载测试文件"""
    test_data: TestData = TestData.query.get(id)
    # 文件名、文件大小
    name, size = tuple(test_data.arg.split())
    match = re.fullmatch('([1-9][0-9]*)(B|K|M|G)(\+1B)?', size)
    size_num = int(match.group(1))
    size_unit = match.group(2)
    size_add_one_byte = match.group(3) == '+1B'
    # if size_unit == 'B':
    #     real_size = size_num
    # elif size_unit == 'K':
    #     real_size = size_num * 1024
    # elif size_unit == 'M':
    #     real_size = size_num * 1024 * 1024
    # ...
    units = "BKMG"
    real_size = size_num * (1024 ** units.index(size_unit))
    if size_add_one_byte:
        real_size += 1

    mime_type = mimetypes.guess_type(name)[0]
    response = make_response(os.urandom(real_size))
    response.headers['Content-Type'] = mime_type
    response.headers['Content-Disposition'] = f'attachment; filename={quote(name)}'
    return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)
