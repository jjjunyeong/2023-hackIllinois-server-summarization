from flask import Flask
from flask import request
from functions.parse_audio import parse_audio, video_to_audio
from functions.parse_pdf import pdf_to_text, parse_text
import json
from summarization import receive_data
# app = Flask(__name__)


# @app.route('/api/v1/machinelearning', methods=['GET', 'POST'])
# def base():
#     print('we are at the base!!')
#     json_data = request.data.decode('utf8')
#     if request.method == 'POST':
#         receive_data(json.loads(json_data))
#         return 'Received a POST request!', 200

# if __name__ == '__main__':
#     app.run()

pdfurl = "https://res.cloudinary.com/dlk3ezbal/image/upload/v1677408827/cramberry/muofg1xcckrqweherqhh.pdf"
videourl = "https://res.cloudinary.com/dlk3ezbal/video/upload/v1677407694/cramberry/yjtq56cqf9gharq60lfi.mov"

data = [{'type': 'pdf', 'url': pdfurl, 'id':0}, {'type':'video', 'url': videourl, 'id':1}]
summary = receive_data(data)
print(summary)