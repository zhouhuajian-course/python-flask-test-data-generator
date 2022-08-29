"""
操作数据库

@author  : zhouhuajian
@version : v1.0
"""

# SQL
# ORM
# 对象 -》 数据库
# 类  -》  数据库表
# 对象 -》 表里面的一行数据

from flask_sqlalchemy import SQLAlchemy

# 数据库对象 -》 数据库
db = SQLAlchemy()

# 数据库表
class TestData(db.Model):
    """测试数据表 test_data"""
    __tablename__ = "test_data"
    # ID 类型 参数 内容
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text, nullable=False)  # 文本 text 表情 emoji 时间戳 timestamp 文件 file
    arg = db.Column(db.Text, nullable=False)
    data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """对象表示"""
        return f"TestData(id={self.id}, type={self.type}, arg={self.arg})"


if __name__ == '__main__':
    # 调试代码
    from flask import Flask
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    # 让数据库对象和Flask对象进行关联
    db.app = app
    db.init_app(app)
    # 创建表 并且创建数据库
    # db.create_all()
    test_data = TestData(type="text", arg="5", data="aaaaa")
    db.session.add(test_data)
    db.session.commit()


