# testing
# Project-V
#Video Processing Web Service
This is a Python web service for video processing using Flask, MongoDB, and MoviePy. It provides two main functionalities: audio extraction and video watermarking.


Installation
1. Clone the repository:
git clone https://github.com/your-username/ladaliproj.git

2. Change into the project directory:
cd ladaliproj

3. Install the required dependencies:
pip install -r requirements.txt

4. ImageMagick:
(for windows install the software and add the path to magick.exe in __init__.py and for MACOS do pip install ImageMagick)

How to setup:- 
1. Ensure MongoDB is running on your machine.

2. Run the Flask application:
python run.py

3. Open your browser and go to http://localhost:5000/ to access the web application.

Endpoints
1. Audio Extraction Endpoint
- Endpoint: /audio_extraction
- Method: POST
- Parameters:
    - user (string): User who uploaded the video.
    - video (file): Video file to extract audio from.


2. Video Watermarking Endpoint
- Endpoint: /video_watermarking
- Method: POST
- Parameters:
    - user (string): User who uploaded the video.
    - position (string): Watermark position (e.g., "center", "bottom-left").
    - video (file): Video file to apply watermark to.

Folder Structure
- app/: Contains the Flask application.
    - static/: Static files including CSS.
    - templates/: HTML templates.
- __init__.py: Initialization file for the Flask application.
- config.py: Configuration file for Flask.
- models.py: MongoDB models.
- routes.py: Definition of API endpoints.
- requirements.txt: List of Python libraries required for the project.
- run.py: Script to run the Flask application.

Libraries Used
- Flask: Web framework for Python.
- Flask-RESTful: Extension for quickly building REST APIs with Flask.
- Flask-PyMongo: Integration of Flask with PyMongo (MongoDB driver for Python).
- MoviePy: Video editing library.
- MongoDB: NoSQL database.

Dockerization
To containerize the application using Docker, you can use the provided Dockerfile:

docker build -t ladaliproj .
docker run -p 5000:5000 ladaliproj

Thank You
