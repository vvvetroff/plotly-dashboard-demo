from random import randint
import re
import json
import asyncio
import subprocess
from quart import websocket, Quart

app = Quart(__name__)

DATAPOINTS = 4

@app.websocket("/data")
async def time_data():
    while True:
        # process = subprocess.Popen(['ping', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        # for line in process.stdout:
        #     # dont want the first line of ping
        #     if re.search(r'PING', line): continue
        #     data = float(re.split(r'\s+', line)[6].removeprefix("time="))
        random_sample = [randint(0, 10) for _ in range(DATAPOINTS)]
        data = {"Voltage": random_sample[0], "Amperage": random_sample[1], "Torque": random_sample[2], "Temperature": random_sample[3]}
        packet = json.dumps(data)

        await websocket.send(packet)
        await asyncio.sleep(1)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
