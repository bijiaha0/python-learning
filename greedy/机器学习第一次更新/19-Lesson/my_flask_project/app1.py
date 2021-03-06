__author__ = "zhou"
__date__ = "2019-06-06 21:17"

from flask import Flask, make_response, jsonify
app = Flask(__name__)
@app.route('/hello')
def hello_world():

    headers = {
        'content-type': 'text/plain'
    }
    response = make_response("<html>sdfd</html>",404)
    response.headers = headers

    return response

@app.route("/getjson")
def get_json():

    headers = {
        'content-type': 'application/json'
    }

    result = {
        "name":"zhagnsan",
        "age": 18
    }

    response = make_response(str(result))
    response.headers = headers
    return response




@app.route("/getjson2")
def get_json2():

    headers = {
        'content-type': 'application/json'
    }

    result = {
        "name":"zhagnsan",
        "age": 18
    }
    # 其实返回的就是一个元组
    return str(result), headers

@app.route("/getjson3")
def get_json3():

    result = {
        "name":"zhagnsan",
        "age": 18
    }
    return jsonify(result)

@app.route("/param/<d1>/<d2>")
def param(d1,d2):
    print(d1)
    print(d2)
    return "1"

app.config.from_object('config')
app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=5001)



