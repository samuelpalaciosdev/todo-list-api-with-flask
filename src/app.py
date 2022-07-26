from flask import Flask, jsonify, request, json

app = Flask(__name__)
##### code inside this #####

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todo = json.loads(request.data)
    # json.loads() parse a valid JSON string and convert it into a Python Dictionary.
    todos.append(todo) # Appending the new todo to the todos list
    print("Incoming request with the following body", todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) # delete the todo at the position passed to the url
    print("This is the position to delete: ",position)
    return jsonify(todos)


##### code inside this #####
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
