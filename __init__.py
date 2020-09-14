from flask import Flask, Response, jsonify, request, json

app = Flask(__name__)

client = app.test_client()

clm_attr = [
    {
        'title': 'INN',
        'info': '4444444'
    },
    {
        'title': 'KPP',
        'info': '101000165'
    }

]

#@app.route("/")
#def index():
#    return Response("It works!"), 200

@app.route("/getattr", methods=['GET'])
def get_list():
    return jsonify(clm_attr)

@app.route("/getattr", methods=['POST'])
def apdate_list():
    new_one = request.json
    clm_attr.append(new_one)
    return jsonify(clm_attr)


@app.route("/", methods=['POST'])
def return_list():
    x = request.json

    operator = x["graphs"][0]["formula"][11]
    operand2 = 0
    try:
        operand2 = int(x["graphs"][0]["formula"][12:])
        if operator == '*':
            for i, j in enumerate(x["data"]["CPULoad5min"]["values"]):
                x["data"]["CPULoad5min"]["values"][i] *= operand2
        elif operator == '+':
            for i, j in enumerate(x["data"]["CPULoad5min"]["values"]):
                x["data"]["CPULoad5min"]["values"][i] += operand2
        elif operator == '-':
            for i, j in enumerate(x["data"]["CPULoad5min"]["values"]):
                x["data"]["CPULoad5min"]["values"][i] -= operand2
        elif operator == '/':
            for i, j in enumerate(x["data"]["CPULoad5min"]["values"]):
                x["data"]["CPULoad5min"]["values"][i] /= operand2
        else:
            x = {
                'Error': 'operator error'
            }
    except:
        x = {
            'Error': 'operand error'
        }

    print(x)
    return(x)





if __name__ == "__main__":
    app.run(debug=True)

