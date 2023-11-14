# app/config.py

class Config:
    MONGO_URI = 'mongodb://localhost:27017/video_processing_db'
    UPLOAD_FOLDER = 'uploads'
    # IMAGEMAGICK_BINARY = "C:\Windows\System32\\convert.exe"

# # Set the path to the ImageMagick 'convert' executable
# # Update 'path/to/convert' with the actual path to the 'convert' executable


# change_settings({"IMAGEMAGICK_BINARY": r"C:\Windows\System32\\convert.exe"})