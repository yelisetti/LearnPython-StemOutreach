import datetime

import dash.html
import dash
from dash.dependencies import Input, Output
import yfinance as yf

# Get the live price of a stock, ex: AAPL
# print(si.get_live_price("AAPL"))
# ______________________________________________________________________________________________________________________

# Input for stock price
# stock = input("Enter a stock: ")
# print(si.get_live_price(stock))
# ______________________________________________________________________________________________________________________________________

app = dash.Dash()
app.title = "Stock Dashboard"

app.layout = dash.html.Div(
    children=[
        dash.html.H1("Stock Dashboard"),
        dash.html.H4("Enter a stock ticker:"),
        dash.dcc.Input(id="input-ticker", value="GOOGL", type="text"),
        dash.html.Div(id="output-graph"),
        dash.html.H4("Current Price:"),
        dash.dcc.Input(id="current_price", value=""),
        dash.html.H4("EBITDA:"),
        dash.dcc.Input(id="ebitda", value=""),
    ]
)

#callback decorator
@app.callback(
    Output(component_id="output-graph", component_property="children"),
    [Input(component_id="input-ticker", component_property="value")],
)
def update_graph(input_data):
    start = datetime.datetime(2023,1,1)
    end = datetime.datetime.now()

    try:
        df = yf.download(input_data, start, end)

        graph = dash.dcc.Graph(
            id="example", figure={
                "data": [
                    {"x": df.index, "y": df.Close, "type": "line", "name": input_data}],
                "layout": {
                    "title": input_data
                }
            })
    except:
        graph = dash.html.Div("Stock not found, Error generating graph.")

    return graph

@app.callback(
    Output(component_id="current_price", component_property="value"),
    [Input(component_id="input-ticker", component_property="value")],
)
def update_current_price(input_data):
    current_price = str(yf.Ticker(input_data).info["currentPrice"])
    return current_price

@app.callback(
    Output(component_id="ebitda", component_property="value"),
    [Input(component_id="input-ticker", component_property="value")],
)
def update_ebitda(input_data):
    ebitda = '${}'.format(f'{yf.Ticker(input_data).info["ebitda"]:,}')
    return ebitda

if __name__ == "__main__":
    app.run_server(debug=True)