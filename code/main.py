from flask import Flask
from flask import request
from summarization import receive_data
app = Flask(__name__)


@app.route('/api/v1/machinelearning', methods=['GET', 'POST'])
def base():
    # return "hello world"
    if request.method == 'POST':
        receive_data(request.data)
        return 'Received a POST request!', 200

if __name__ == '__main__':
    app.run()