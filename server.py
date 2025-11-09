import socket
import cv2
import numpy as np


HOST = 'localhost'  
PORT = 5000        

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"The server is running on {HOST}:{PORT}. Waiting for connection...")
        
        conn, addr = s.accept()
        print(f"The client is connected: {addr}")
        
        with conn:
            while True:

                size_data = conn.recv(4)
                if not size_data:
                    break
                

                size = int.from_bytes(size_data, byteorder='big')
                

                frame_data = b''
                while len(frame_data) < size:
                    packet = conn.recv(size - len(frame_data))
                    if not packet:
                        break
                    frame_data += packet
                
                frame = cv2.imdecode(
                    np.frombuffer(frame_data, dtype=np.uint8), 
                    cv2.IMREAD_COLOR
                )
                
                if frame is not None:
                    cv2.imshow('Screen Stream', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()