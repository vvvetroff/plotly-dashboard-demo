# Plotly Dash(board) Demo
A ""quick"" demo demonstrating the real-time data visualization capabilities of Dash by Plotly using WebSockets.

## Overview
This demo simulates a dashboard that receives and plots incoming data from the DMS via WebSocket connection.

## Contents
**`mock_dms.py`**:
- Represents all the incoming data from the FSAE, as if it was coming from the Duck Management System
- Generates and sends four data points via WebSocket as a dictionary:
  - Voltage, Amperage, Torque, and Temperature

**`mock_dash.py`**:
- Receives WebSocket data and updates graphs in real-time
- Uses server-side callbacks with `extendData` for incremental graph updates
- Note: Could be optimized with client-side callbacks if performance becomes an issue (see [dash-extensions docs](https://www.dash-extensions.com/components/websocket))

**`requirements.txt`**:
- Python dependencies required to run the project
- Gotta love it.

## Setup & Usage

1. **Clone the repository:**
```bash
   git clone <url>
   cd <repo-name>
```

2. **Create and activate virtual environment:**
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
```

3. **Run both services** (requires two terminals):
```bash
   # Terminal 1: Start the WebSocket server (port 5000)
   python3 mock_dms.py
   
   # Terminal 2: Start the Dash app (port 8050)
   python3 mock_dash.py
```
   
   *Tip: If you use tmux, create a split window for convenience*

4. **View the dashboard:**
   Open your browser to `http://localhost:8050`
