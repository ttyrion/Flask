from app import app
from flask_sqlalchemy import SQLAlchemy

# 默认值
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost:3306/sxh?charset=utf8mb4'
# 其他数据库
DB_STAFF = 'staff'
DB_COURSE = 'course'
SQLALCHEMY_BINDS = {
    DB_STAFF:        'mysql+pymysql://root:root123@localhost:3306/staff?charset=utf8mb4',
    DB_COURSE:      'mysql+pymysql://root:root123@localhost:3306/course?charset=utf8mb4'
}

app.secret_key = 'hellafwjeojfa[erkgerf'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
db = SQLAlchemy(app)
