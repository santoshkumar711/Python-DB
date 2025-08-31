from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="db",   # docker-compose.yml me db service ka naam use karo
        user="santosh",
        password="santoor711",
        database="python"
    )
    return connection

@app.route('/')
def home():
    return "Welcome to Student Records API! 🎉, welocme to Database deployment."

# Add new student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    student_id = data.get("id")
    name = data.get("name")
    course = data.get("course")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (id, name, course) VALUES (%s, %s, %s)", 
                   (student_id, name, course))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Student added successfully!"})

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
