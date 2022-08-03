from settings import *
import json
from datetime import datetime

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'  # creating a table name
    student_id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80))
    amount_due = db.Column(db.Integer, default = 0, nullable=False)

    # nullable is false so the column can't be empty

    def json(self):
        return {'student_id': self.student_id, 'first_name': self.first_name,
                'last_name': self.last_name, 'dob': self.dob, 'amount_due': self.amount_due}
        # this method we are defining will convert our output to json    

    
    def add_student(_first_name, _last_name, _dob, _amount_due):
        # creating an instance of students constructor
        new_student = Student(first_name=_first_name, last_name=_last_name, dob=_dob, amount_due = _amount_due )
        db.session.add(new_student)  # add new student to database session
        db.session.commit()  # commit changes to session

    def get_all_students():
        '''function to get all students in our database'''
        return [Student.json(student) for student in Student.query.all()]

    def get_student(_student_id):
        '''function to get student using the id of the student as parameter'''
        return [Student.json(Student.query.filter_by(student_id=_student_id).first())]

    def update_student(_student_id, _first_name, _last_name, _dob, _amount_due):
        '''function to update the details of a student using the id as parameters'''
        students_to_update = Student.query.filter_by(student_id=_student_id).first()
        students_to_update.first_name = _first_name
        students_to_update.last_name = _last_name
        students_to_update.dob = _dob
        students_to_update.amount_due = _amount_due
        db.session.commit()

    def delete_student(_student_id):
        '''function to delete a student from our database using
           the id of the student as a parameter'''
        Student.query.filter_by(student_id=_student_id).delete()
        # filter student by id and delete
        db.session.commit()  # commiting the new change to our databas