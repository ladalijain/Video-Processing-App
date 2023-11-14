# app/routes.py

from flask import render_template, request, send_from_directory
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from app import app, api
from app.models import VideoInfo

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
import os 

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
parser = reqparse.RequestParser()
parser.add_argument('user', type=str, help='User who uploaded the video', required=True)
parser.add_argument('position', type=str, help='Position of watermark', required=False)

video_info = VideoInfo()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
class AudioExtraction(Resource):
    def post(self):
        user = request.form.get('user')

        file = request.files.get('video')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = f'app/static/{filename}'
            file.save(file_path)

            # Perform audio extraction here
            audio_output_path = f'app/static/{filename.rsplit(".", 1)[0]}.mp3'
            video_clip = VideoFileClip(file_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(audio_output_path)
            audio_clip.close()

            video_info.insert_video_info(user, 'audio_extraction', filename)
            return {'message': 'Audio extraction successful', 'audio_file': audio_output_path}

        return {'error': 'Invalid file or format'}

class VideoWatermarking(Resource):
    def post(self):
        
        user = request.form.get('user')
        position = request.form.get('position')

        video_file = request.files['video']
        watermark_file = request.files['watermark']

        if video_file and allowed_file(video_file.filename) and watermark_file and allowed_file(watermark_file.filename, allowed_extensions={'png', 'jpg', 'jpeg'}):
            video_filename = secure_filename(video_file.filename)
            watermark_filename = secure_filename(watermark_file.filename)

            file_path = f'app/static/{video_filename}'
            video_file.save(f'app/static/{video_filename}')
            file_path2 = f'app/static/{watermark_filename}'
            watermark_file.save(f'app/static/{watermark_filename}')

            # video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
            # watermark_file_path = os.path.join(app.config['UPLOAD_FOLDER'], watermark_filename)

            # video_file.save(video_file_path)
            # watermark_file.save(watermark_file_path)

            # Perform video watermarking here with the specified position

            watermark_image = ImageClip(file_path2, transparent=True)
            
            video_clip = VideoFileClip(file_path)
            if position == "center":
                watermarked_clip = CompositeVideoClip([video_clip, watermark_image.set_duration(video_clip.duration).set_position("center")])
            else:
                # Add more positions as needed
                watermarked_clip = CompositeVideoClip([video_clip, watermark_image.set_duration(video_clip.duration).set_position((0.05, 0.9))])

            # watermarked_output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{video_filename.rsplit('.', 1)[0]}_watermarked.mp4")


            watermarked_output_path = f'app/static/{video_filename.rsplit(".", 1)[0]}_watermarked.mp4'
            # video_clip = VideoFileClip(file_path)
            # audio_clip = video_clip.audio
            # audio_clip.write_audiofile(audio_output_path)
            # audio_clip.close()



            watermarked_clip.write_videofile(watermarked_output_path, codec='libx264', audio_codec='aac')
            watermarked_clip.close()

            # Insert video and watermark information into the database
            video_info.insert_video_info(user, 'watermarking', video_filename)
            
            return {'message': 'Video watermarking successful', 'watermarked_video': watermarked_output_path}

        return {'error': 'Invalid file or format'}

# ...

def allowed_file(filename, allowed_extensions=None):
    if allowed_extensions is None:
        allowed_extensions = ALLOWED_EXTENSIONS
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

api.add_resource(AudioExtraction, '/audio_extraction')
api.add_resource(VideoWatermarking, '/video_watermarking')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)