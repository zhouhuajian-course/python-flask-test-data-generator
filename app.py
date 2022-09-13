"""
测试数据生成器

@author  : zhouhuajian
@version : v1.0
"""
import mimetypes
import random
import re
from urllib.parse import quote

from flask import Flask, render_template, make_response
from api.test import bp
from db.database import db, TestData

app = Flask(__name__)
app.register_blueprint(bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
# 让数据库对象和Flask对象进行关联
db.app = app
db.init_app(app)


@app.route('/')
def index():
    """首页"""
    # 从数据库获取数据
    test_datas = TestData.query.order_by(TestData.id.desc()).limit(100).all()
    return render_template('index.html', test_datas=test_datas)


@app.route('/file/<int:id>')
def file(id):
    """文件下载接口"""
    # 根据数据ID，获取数据库里面的数据
    test_data = TestData.query.get(id)
    # 文件名、文件大小
    name, size = tuple(test_data.arg.split())
    # 使用正则匹配和正则捕获，获取文件大小信息
    match = re.fullmatch(r'([1-9][0-9]*)(G|M|K|B)(\+1B)?', size)
    size_number = match.group(1)
    size_unit = match.group(2)
    size_add_one_byte = match.group(3) == "+1B"  # 10M+1B 10M
    print(size_number, size_unit, size_add_one_byte)
    # 文件大小
    # 10B -> 10 * 1024 ** 0
    # 10K -> 10 * 1024 ** 1
    # 10M -> 10 * 1024 ** 2
    # 10G -> 10 * 1024 ** 3
    real_size = int(size_number) * (1024 ** "BKMG".index(size_unit))
    if size_add_one_byte:
        real_size += 1
    file_content = random.randbytes(real_size)
    response = make_response(file_content)
    response.headers.add_header("Content-Type", mimetypes.guess_type(name)[0])
    response.headers.add_header("Content-Disposition", f"attachment; filename={quote(name)}")
    return response


if __name__ == '__main__':
    app.run(port=80, debug=True)
