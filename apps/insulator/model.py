from werkzeug.security import generate_password_hash, check_password_hash
from exts import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    org_id = db.Column(db.Integer, db.ForeignKey('orgnization.id'))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

# organization 运行单位
class Orgnization(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_name = db.Column(db.String(20))
    employees = db.relationship('User', backref='org')
    account = db.relationship('Account', backref='org')

class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    line_name = db.Column(db.String(20))
    account = db.relationship('Account', backref='org')

# 台账
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_id = db.Column(db.Integer, db.ForeignKey('orgnization.id'))
    line_id = db.Column(db.Integer, db.ForeignKey('line.id'))
    tower_id = db.Column(db.Integer)
    tower_type = db.Column(db.String(30)) # 塔型
    ton = db.Column(db.Integer)
    insulator_type = db.Column(db.String(255)) # 复合绝缘子型号
    str_num = db.Column(db.Integer) # 串数
    str_type = db.Column(db.String(50)) # 串型
    manufacturer = db.Column(db.String(255)) # 生产厂家
    insu_date = db.Column(db.String(255))  # 绝缘子投运时间
    remark = db.Column(db.Text) # 备注
    signature = db.Column(db.String(30)) #班长签字
    equip_status = db.Column(db.String(10)) #设备状态  由特征一和特征二得出设备状态
    scrap_status = db.Column(db.Integer)  # 退运状态
    feature1 = db.Column(db.String(30)) # 抽检特征一
    feature2 = db.Column(db.String(30)) # 抽检特征二



