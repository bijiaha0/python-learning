from crm import create_app

__author__ = "zhou"
__date__ = "2019-06-11 20:54"


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)







