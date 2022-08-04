"""
测试数据生成器

@author  : zhouhuajian
@version : v1.0
"""
from flask import Flask, render_template
from api.test import bp

app = Flask(__name__)
app.register_blueprint(bp)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=80, debug=True)