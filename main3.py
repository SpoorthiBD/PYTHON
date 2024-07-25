import socket
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt
 

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
 
if __name__ == "__main__":
    print("IP Address of the system:", get_ip_address())

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Feed")
        self.setGeometry(100, 100, 640, 480)
       
        # Set up the camera
        available_cameras = QCameraInfo.availableCameras()
        if not available_cameras:
            print("No camera found.")
            return
       
        self.camera = QCamera(available_cameras[0])
        self.viewfinder = QCameraViewfinder(self)
        self.camera.setViewfinder(self.viewfinder)
       
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)
        self.setLayout(layout)
       
        self.camera.start()
 
    def closeEvent(self, event):
        self.camera.stop()
        event.accept()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CameraApp()
    win.show()
    sys.exit(app.exec_())