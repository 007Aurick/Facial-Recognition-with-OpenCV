Yep — here’s a clean README you can use for that project:

# Real-Time Face Detection with OpenCV

This project uses **OpenCV** and a **Haar Cascade Classifier** to perform real-time face detection through a webcam. It detects faces in each video frame, draws bounding boxes around them, and displays messages showing whether no face, one face, or multiple faces are detected.

## Features

- Real-time webcam face detection
- Uses Haar Cascade for frontal face recognition
- Displays:
  - **Facial Recognition** title
  - **FPS**
  - **No Face Detected**
  - **One Face Detected**
  - **Multiple Faces Detected**
- Draws rectangles around detected faces
- Allows saving a frame as an image

## Technologies Used

- Python
- OpenCV

## How It Works

1. Loads the Haar Cascade XML file for frontal face detection
2. Opens the webcam feed
3. Reads each frame from the webcam
4. Converts the frame to grayscale
5. Detects faces using `detectMultiScale()`
6. Draws rectangles and labels around detected faces
7. Displays the live video feed until the user quits or saves an image

## Requirements

Make sure you have Python installed, then install OpenCV:

```bash
pip install opencv-python
```
You also need the Haar Cascade XML file:

haarcascade_frontalface_default.xml

Place it in the same folder as your Python script.

How to Run
python your_script_name.py
Controls
Press q to quit the program
Press s to save the current frame as image.jpg and exit
Example Output
If no face is visible, the screen shows: No Face Detected
If one face is visible, the screen shows: One Face Detected
If more than one face is visible, the screen shows the total number of faces detected
Project Structure
face-detection-project/
│── your_script_name.py
│── haarcascade_frontalface_default.xml
│── README.md
Code Overview
Face Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Loads the pretrained Haar Cascade model for frontal face detection.

Video Capture
video = cv2.VideoCapture(0)

Starts webcam input.

Grayscale Conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Converts the frame to grayscale, which helps the Haar Cascade work more efficiently.

Face Detection
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

Detects faces in the frame.

Saving an Image
cv2.imwrite('image.jpg', img)

Saves the current frame when s is pressed.

Possible Improvements
Add eye detection
Add smile detection
Improve FPS display formatting
Save images with unique filenames
Add face counting history
Switch from Haar Cascades to a more advanced model like DNN or MediaPipe
Author

Made by Aurick Anwar
