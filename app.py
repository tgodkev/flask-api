from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

tasks = []

def generate_id():
    return str(uuid.uuid4())



@app.route('/api/hello', methods=['GET'])
def hello():
    response = {"message": "Hello, Flask API!"}
    return jsonify(response)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"message": "Title is required"}), 400
    
    new_task = {
        'id': generate_id(),
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False
    }
    
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)



@app.route('/api/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({"message": "Task not found"}), 404
        
    return jsonify(task)





if __name__ == '__main__':
    app.run(debug=True)
