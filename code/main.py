from flask import Flask
from flask import request
from functions.parse_audio import parse_audio, video_to_audio
from functions.parse_pdf import pdf_to_text, parse_text
import json
from summarization import receive_data
app = Flask(__name__)


@app.route('/api/v1/machinelearning', methods=['GET', 'POST'])
def base():
    print('we are at the base!!')
    post_data = json.loads(request.data)['good']
    
    # print(request.data['good'])
    # print(request.data.good)
    # if request.data == None or request.data == '':
    #   print('I got a null or empty string value for data in a file')
    # else:
        # js = json.loads(str(data))
        # print("//////")
        # print(request.data.decode('utf8'))
        # print(json.loads(request.data.decode('utf8')[0]))
        # json_data = json.loads(request.data.decode('utf8'))
    # print(json_data)
    if request.method == 'POST':
        summary =  receive_data(post_data)
        print(summary)
        return summary
        #  'Received a POST request!', 200
    
    # elif request.method == 'GET':
        # return summary

if __name__ == '__main__':
    app.run()

# dolphin1 = "https://res.cloudinary.com/dlk3ezbal/image/upload/v1677413166/cramberry/t6pahrh2vitawswjviwf.pdf"
# dolphin2 = "https://res.cloudinary.com/dlk3ezbal/image/upload/v1677413167/cramberry/cfzqnhwp04xaqlqauyvu.pdf"
# dolphin3 = "https://res.cloudinary.com/dlk3ezbal/video/upload/v1677413167/cramberry/ntuoytefotxg0m6wnws1.mp4"

# fourier1 = "https://res.cloudinary.com/dlk3ezbal/image/upload/v1677413166/cramberry/sqd1slzn5zzkciyitmvh.pdf"
# fourier2 = "https://res.cloudinary.com/dlk3ezbal/video/upload/v1677413167/cramberry/lxgokwodalpkqlpbcenk.mp4"

# data = [{'type': 'pdf', 'url': dolphin1, 'id':0},
#         {'type': 'pdf', 'url': dolphin2, 'id':1},
#         {'type':'video', 'url': dolphin3, 'id':2}]

# data2 = [{'type': 'pdf', 'url': fourier1, 'id':0},
#         {'type': 'video', 'url': fourier2, 'id':1}]

# receive_data(data)