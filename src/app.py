from flask import Flask, jsonify, request

app = Flask(__name__)

#  Todos de ejemplo 
todos = [
    {"done": True, "label": "Sample Todo 1"},
    {"done": True, "label": "Sample Todo 2"}
]

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return '<h1>Hello!</h1>'

# Endpoint GET 
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Endpoint POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.get_json()  
    if not new_todo or 'done' not in new_todo or 'label' not in new_todo:
        return jsonify({"error": "Invalid data, must include 'done' and 'label'"}), 400
    
    todos.append(new_todo)  
    return jsonify(todos)

# Endpoint DELETE 
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400 
    todos.pop(position)  
    return jsonify(todos) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
