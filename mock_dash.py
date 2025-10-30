from dash_extensions import WebSocket
from dash_extensions.enrich import DashProxy, Input, Output, dcc, html
import time
import json

INTERVAL_FREQUENCY = 1000
def default_figure(t: str):
    return dict(
        data=[{'x':[],'y':[]}],
        layout=dict(
            yaxis=dict(range=[0,10]),
            title={'text': t}
            )
        )


empty_data = (dict(x=[[]], y=[[]]), [0], 100)

app = DashProxy(__name__)
app.layout = html.Div([
        WebSocket(id="ws", url="ws://127.0.0.1:5000/data"),
        html.H1(id="text", style={'textAlign': 'center'}),
        dcc.Graph(id="graph_Voltage", 
                  figure=default_figure("Voltage"), 
                  style={ 'width': '50%', 'height': '50%', 'float': 'left' },
                  mathjax=True),
        dcc.Graph(id="graph_Amperage",
                  figure=default_figure("Amperage"), 
                  style={ 'width': '50%', 'height': '50%', 'float': 'left' },
                  mathjax=True),
        dcc.Graph(id="graph_Torque",
                  figure=default_figure("Torque"), 
                  style={ 'width': '50%', 'height': '50%', 'float': 'left' },
                  mathjax=True),
        dcc.Graph(id="graph_Temperature",
                  figure=default_figure("Temperature"), 
                  style={ 'width': '50%', 'height': '50%', 'float': 'left' },
                  mathjax=True),
        dcc.Interval(id="update", interval=INTERVAL_FREQUENCY)
    ])

@app.callback(
        Output("graph_Voltage", "extendData"),
        Output("graph_Amperage", "extendData"), 
        Output("graph_Torque", "extendData"), 
        Output("graph_Temperature", "extendData"), 
        Output("text", "children"), 
        Input("ws", "message")
        )
def parse_response(e):
    if e == None:
        return empty_data, empty_data, empty_data, empty_data, f"UConn Formula SAE Sample Dashboard"
    response = json.loads(e['data'])
    delta_time = time.time()
    volt = (dict(x=[[delta_time]], y=[[response['Voltage']]]), [0], 100)
    amps = (dict(x=[[delta_time]], y=[[response['Amperage']]]), [0], 100)
    torq = (dict(x=[[delta_time]], y=[[response['Torque']]]), [0], 100)
    temp = (dict(x=[[delta_time]], y=[[response['Temperature']]]), [0], 100)

    return volt, amps, torq, temp, f"UConn Formula SAE Sample Dashboard"

if __name__ == "__main__":
    app.run(debug=True)
