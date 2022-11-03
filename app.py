from flask import Flask, request, json, Response
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
            data = { "slackUsername": slackUsername, "result": sum, "operation_type" : operation }

            response = json.dumps(data, sort_keys=False)
            return Response(response, mimetype='application/json')

        elif operation == 'subtraction':
            minus = x - y
            data = { "slackUsername": slackUsername, "result": minus, "operation_type" : operation }

            response = json.dumps(data, sort_keys=False)
            return Response(response, mimetype='application/json')

        elif operation == 'multiplication':
            times = x * y
            data = { "slackUsername": slackUsername, "result": times, "operation_type" : operation }

            response = json.dumps(data, sort_keys=False)
            return Response(response, mimetype='application/json')
        else:
            return {"response": "Operation must be either addition, multiplication or Subtration"}
    
    return "there was a issue processing you operation!!!"


if __name__ == '__main__':
    app.run(debug=True)
