from db.db import db
from db.db import DB_STAFF
from db.db import DB_COURSE

# db.create_all()将自动生成表student_teacher_relationship, student, teacher
student_teacher_relationship = db.Table('student_teacher_relationship',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')),
    info={'bind_key': DB_STAFF}
)

class Student(db.Model):
    __bind_key__ = DB_STAFF
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    teachers = db.relationship('Teacher', secondary = student_teacher_relationship, back_populates = 'students')

class Teacher(db.Model):
    __bind_key__ = DB_STAFF
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    students = db.relationship('Student', secondary = student_teacher_relationship, back_populates = 'teachers')