from config import *
import os
import replicate
import moviepy.editor
import re

def video_to_audio(object):
    video_file_path = object['url']
    video = moviepy.editor.VideoFileClip(video_file_path)
    
    file_name = re.split('cramberry/|.mp4|.mov|', video_file_path)[1]
    audio_file_path = os.getcwd().split("code")[0] + 'data/' + file_name + ".mp3"
    
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    
    return audio_file_path

def parse_audio(audio_file_path, object):
    #Set the REPLICATE_API_TOKEN environment variable
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
    
    model = replicate.models.get("openai/whisper")
    version = model.versions.get(AUDIO_TOKEN)
    inputs = {
        'audio': open(audio_file_path, "rb"),
        'model': "base",
        'transcription': "srt",
        'translate': False,
        'temperature': 0,
        'suppress_tokens': "-1",
        'condition_on_previous_text': True,
        'temperature_increment_on_fallback': 0.2,
        'compression_ratio_threshold': 2.4,
        'logprob_threshold': -1,
        'no_speech_threshold': 0.6,
    }
    # https://replicate.com/openai/whisper/versions/30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed#input
    
    output = version.predict(**inputs)
    text_objects = [{'type': object['type'], 'raw': seg['text'], 'start': seg['start'], 'end': seg['end'], 'id': object['id'], 'url':object['url']} for seg in output['segments']]
        
    return text_objects