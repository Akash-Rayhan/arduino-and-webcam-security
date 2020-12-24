import serial
import cv2
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


serial_monitor = serial.Serial('/dev/ttyACM0', 9600)
webcam = cv2.VideoCapture(0)
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def read_filtered_sensor_data():
    sensor_data = serial_monitor.readline()
    return sensor_data.decode('utf-8').replace('\r', '').replace('\n', '')


def capture_webcam_image():
    now = datetime.now().strftime("%H:%M:%S")
    image_name = "opencv_frame_{}.png".format(now)
    cv2.imwrite(image_name, frame)

    return image_name


def upload_file_to_google_drive(image_name):
    file1 = drive.CreateFile({'title': image_name})
    file1.SetContentFile(image_name)
    file1.Upload()


if __name__ == "__main__":
    while True:
        ret, frame = webcam.read()
        filtered_sensor_data = read_filtered_sensor_data()

        if filtered_sensor_data == "1":
            filename = capture_webcam_image()
            upload_file_to_google_drive(filename)
