"""
测试数据生成器

@author  : zhouhuajian
@version : v1.0
"""
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


if __name__ == '__main__':
    app.run(port=80, debug=True)