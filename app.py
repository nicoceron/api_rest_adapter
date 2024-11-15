from flask import Flask, jsonify, abort
from flask import request

app = Flask(__name__)

# Employee represents an employee with basic attributes
class Employee:
    def __init__(self, ID, Name, Salary, Role, Tech, Email):
        self.id = ID
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.tech = Tech
        self.email = Email

    def to_dict(self):
        return {
            "id": self.id,
            "salary": self.salary,
            "name": self.name,
            "role": self.role,
            "tech": self.tech,
            "email": self.email
        }

# Predefined list of employees with historical figures
employees = [
    Employee(1, "Albert Einstein", 15000000, "Theoretical Physicist", "Relativity", "albert.einstein@example.com"),
    Employee(2, "Marie Curie", 14000000, "Chemist", "Radioactivity", "marie.curie@example.com"),
    Employee(3, "Isaac Newton", 13000000, "Mathematician", "Calculus", "isaac.newton@example.com"),
    Employee(4, "Leonardo da Vinci", 16000000, "Renaissance Polymath", "Art & Engineering", "leonardo.da.vinci@example.com"),
    Employee(5, "Nikola Tesla", 14500000, "Electrical Engineer", "AC Power", "nikola.tesla@example.com"),
    Employee(6, "Ada Lovelace", 13500000, "Computer Programmer", "Analytical Engine", "ada.lovelace@example.com"),
    Employee(7, "Galileo Galilei", 12500000, "Astronomer", "Telescopic Discoveries", "galileo.galilei@example.com"),
    Employee(8, "Charles Darwin", 14000000, "Naturalist", "Evolutionary Biology", "charles.darwin@example.com"),
    Employee(9, "Thomas Edison", 15000000, "Inventor", "Electric Light", "thomas.edison@example.com"),
    Employee(10, "Srinivasa Ramanujan", 13000000, "Mathematician", "Number Theory", "srinivasa.ramanujan@example.com"),
]

@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    # Search for the employee with the given ID
    for employee in employees:
        if employee.id == employee_id:
            return jsonify(employee.to_dict()), 200
    # If not found, return 404
    abort(404, description="Employee not found")

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Additional route to get all employees (optional)
@app.route('/employees', methods=['GET'])
def get_all_employees():
    return jsonify([emp.to_dict() for emp in employees]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
