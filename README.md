# ScreenStreamTCP
A lightweight Python utility for streaming your screen to a remote machine via TCP socket. Uses [Tuna](https://tuna.am/) for public tunneling, making it accessible from anywhere without complex network setup.

## How It Works

1. **Server** listens on a local port (default: 5000).
2. **Tuna** creates a public TCP tunnel to that port.
3. **Client** captures the screen using `mss`, encodes frames as JPEG, and sends them over the tunnel.
4. **Server** decodes and displays frames in real time using OpenCV.
5. Connection closes cleanly on `Ctrl+C` or `Q` key press.

---

##  Prerequisites

### General
- Python 3.8+
- Required packages: `opencv-python`, `numpy`, `mss`

### For Public Access
- Installed `tuna` CLI client (see [Tuna Documentation](https://tuna.am/))

---

## 📦 Installation

Install dependencies:

```bash
pip install opencv-python numpy mss
```

### Download and install tuna for your OS:
* Windows: Use winget or download from Tuna Downloads
* macOS/Linux: Follow platform-specific instructions on the site.

---

## Setup & Usage

### Step 1:  Create a Public Tunnel with Tuna
In a separate terminal, start the Tuna tunnel:
 
 ```bash
tuna tcp 5000
```

### Step 2: Start the Server
Run the server locally:

 ```bash
python3 server.py
```

You will see output similar to this:

```bash
INFO[09:46:10] Welcome to Tuna
INFO[09:46:10] Account: user_account (Paid till 08.07.2025)
INFO[09:46:11] Forwarding tcp://ru.tuna.am:29498 -> 127.0.0.1:5000
```

Note: The dynamically assigned port (29498 in the example) is critical — you must use this number when launching the client. 

### Step 3: Launch the Client
On the machine whose screen you want to stream:

 ```bash
python3 server.py
```

You will need to enter the public port assigned by Tuna (e.g., 29498).

Once connected, the server will begin displaying the live screen feed.
Important: The client connects to the public endpoint created by Tuna, which forwards traffic to your local server. 

---

## Architecture Overview

### Server (server.py)
* Listens for TCP connections on localhost.
* Receives frame size (4 bytes), then the full frame data.
* Decodes JPEG buffer into OpenCV image and displays it.
* Terminates on q key press or connection loss.

### Client (client.py)
* Captures screen via mss (cross-platform).
* Encodes each frame as JPEG (quality: 60%).
* Sends frame size + data over TCP.
* Handles connection errors gracefully.

---

## Limitations & Notes

* No Encryption: Data is sent unencrypted. Not suitable for sensitive content.
* Latency: Depends on network speed and CPU performance. Adjust JPEG quality for better FPS.
* Tuna Limits: Free tunnels may have bandwidth/time restrictions. Paid accounts recommended for extended use.
* Platform Support: Tested on Windows, macOS, Linux. 

---

## This project is licensed under the MIT License. See LICENSE for details.
