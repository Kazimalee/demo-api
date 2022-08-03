from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_name():
    return "hello world"
    
@app.route("/hello")
def hehe_name():
    d={"first_name":"Kazim"}
    return d
if __name__ == "__main__":
    app.run()



