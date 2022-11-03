from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/', methods=['POST'])
def operation():
    if request.method == 'POST':
        operation = request.json["operation_type"]
        x = request.json['x']
        y = request.json['y']
        slackUsername = 'Nats'

        if operation == 'addition':
            sum = x + y
            return { "slackUsername": slackUsername, "operation_type" : operation, "result": sum }
        elif operation == 'subtraction':
            minus = x - y
            return { "slackUsername": slackUsername, "operation_type" : operation, "result": minus }
        elif operation == 'multiplication':
            times = x * y
            { "slackUsername": slackUsername, "operation_type" : operation, "result": times }
        else:
            return {"response": "Operation must be either addition, multiplication or Subtration"}
    
    return "there was a issue processing you operation!!!"


if __name__ == '__main__':
    app.run(debug=True)
