"""
    @file        cam_stream.py
    @author      Mowibox (Ousmane THIONGANE)
    @brief       Live camera stream display
    @version     1.0
    @date        2024-10-24
    
"""

# Includes
import cv2
import time
import subprocess
from flask import Flask, Response

app = Flask(__name__)

def get_cpu_temp() -> str:
    """
    Returns the Raspberry Pi CPU temperature
    """
    temp_cmd = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    temp_str = temp_cmd.stdout
    temp = temp_str.split('=')[1].split("'")[0]
    return temp


def generate_frames():
    """
    Generates the frames for the camera stream
    """
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640//2)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480//2)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    # Variables for FPS
    prev_frame_time = 0
    new_frame_time = 0

    while True:
        success, frame = camera.read()

        # Necessary regarding the actual Chromapi's camera setup
        frame = cv2.flip(frame, 0)
        frame = cv2.flip(frame, 1)
        if not success:
            break
        
        new_frame_time = time.time()
        fps = 1/(new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps_text = f"FPS: {int(fps)}"
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (65, 55, 255), 2, cv2.LINE_AA)
        
        cpu_temp = get_cpu_temp()
        cpu_temp_text = f"T = {cpu_temp}"
        cv2.putText(frame, cpu_temp_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (65, 55, 255), 2, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
        if not ret:
            continue
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
