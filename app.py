"""
测试数据生成器

@author  : zhouhuajian
@version : v1.0
"""
import re

from flask import Flask, render_template
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
    # 从数据库获取数据
    test_datas = TestData.query.order_by(TestData.id.desc()).limit(100).all()
    # print(test_datas)
    return render_template('index.html', test_datas=test_datas)


@app.route('/file/<int:id>')
def file(id):
    # print(id)
    # 根据ID获取数据库里面的数据
    # 文件名、文件大小
    test_data = TestData.query.get(id)
    name, size = tuple(test_data.arg.split())
    # abc.png 10M+1B
    match = re.fullmatch(r'([1-9][0-9]*)(G|M|K|B)(\+1B)?', size)
    size_number = match.group(1)
    size_unit = match.group(2)
    size_add_one_byte = match.group(3) == "+1B"  # 10M+1B 10M
    print(size_number, size_unit, size_add_one_byte)
    # 以后是返回文件内容
    return ""

if __name__ == '__main__':
    app.run(port=80, debug=True)