"""
创建数据库表

@author  : zhouhuajian
@version : v1.0
"""
from flask import Flask
from db.database import db

# Flask 应用
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.app = app
db.init_app(app)

if __name__ == '__main__':
    # 创建所有表
    db.create_all()
