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
