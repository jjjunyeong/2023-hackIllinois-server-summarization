from config import *
import os
import replicate
import moviepy.editor

def video_to_audio(video_file_path):
    video = moviepy.editor.VideoFileClip(video_file_path)
    
    file_name = video_file_path.split('.mp4')[0]
    audio_file_path = file_name + ".mp3"
    
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    
    return audio_file_path

def parse_audio(file_path):
    #Set the REPLICATE_API_TOKEN environment variable
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
    
    model = replicate.models.get("openai/whisper")
    version = model.versions.get(AUDIO_TOKEN)
    inputs = {
        'audio': open(file_path, "rb"),
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
    text_objects = [{'type': 'audio', 'raw': seg['text'], 'start': seg['start'], 'end': seg['end'], 'id': seg['id']} for seg in output['segments']]
        
    return text_objects