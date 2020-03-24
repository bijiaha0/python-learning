__author__ = "zhou"
__date__ = "2019-06-06 21:00"



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!eeee'

# if __name__ == "__main__":
#     # app.run()
#     app.run(host="0.0.0.0", debug=True, port=5001)
# import config
# app.run(host="0.0.0.0", debug=config.debug, port=5001)

# 通过配置文件载入的方式进行配置加载
app.config.from_object('config')
app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=5001)



