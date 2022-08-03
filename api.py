from students import *
from datetime import datetime

# route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    '''Function to get all the students in the database'''
    return jsonify({'Students': Student.get_all_students()})

# route to get students by id
@app.route('/students/<int:id>', methods=['GET'])
def get_students_by_id(id):
    return_value = Student.get_student(id)
    return jsonify(return_value)

# route to add new stsudent
@app.route('/students', methods=['POST'])
def add_student():
    '''Function to add new student to  database'''
    request_data = request.get_json()  # getting data from client
    Student.add_student(request_data["first_name"], request_data["last_name"],
                    request_data["dob"], request_data["amount_due"])
    response = Response("Student added", 201, mimetype='application/json')
    return response

# route to update student with PUT method
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    '''Function to edit student in our database using student id'''
    request_data = request.get_json()
    Student.update_student(id, request_data['first_name'], request_data['last_name'], request_data['dob'], request_data["amount_due"])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response

# route to delete student using the DELETE method
@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    '''Function to delete student from our database'''
    Student.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=8080, debug=True)