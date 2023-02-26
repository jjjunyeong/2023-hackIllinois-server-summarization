from flask import Flask
from flask import request
from summarization import summarization
app = Flask(__name__)


@app.route('/api/v1/machinelearning', methods=['GET', 'POST'])
def base():
    if request.method == 'POST':
        summarization(request.data)
        return 'Received a POST request!', 200

if __name__ == '__main__':
    app.run()