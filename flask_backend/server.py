from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    # return {"test"}
    return {"test": ["test1", "test2", "test3"]}

if __name__ == '__main__':
    app.run(port=8000 ,debug=True)