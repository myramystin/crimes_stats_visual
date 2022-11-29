from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

from prepare_data import df_income, df_population, df_pct_unemp, df_pct_urban

"""
selectors -- 
    * state name - dropdown
    * population - slider 
    * what crimes to include - checkbox
    * medIncome - slider
    * pct urban - slider
    * pct unemployed - slider
"""



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(["Population", "Median Income", "Urban Percentage",
                  "Unemployed Percentage"], "Population", id="feature"),
    dcc.Graph(id='graphic'),
])


@app.callback(
    Output('graphic', 'figure'),
    Input('feature', 'value'))
def update_graph(feature_value):
    fig = None
    if feature_value == "Population":
        fig = px.scatter(
            x=df_population["population"],
            y=df_population["arsons"])
    elif feature_value == "Median Income":
        fig = px.scatter(
            x=df_income["rounded_income"],
            y=df_income["arsons"])
    elif feature_value == "Urban Percentage":
        fig = px.scatter(
            x=df_pct_urban["rounded_pct"],
            y=df_pct_urban["arsons"])
    else:
        fig = px.scatter(
            x=df_pct_urban["rounded_pct"],
            y=df_pct_urban["arsons"])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                      hovermode='closest')


    return fig





if __name__ == '__main__':
    app.run_server(debug=True, port=8000)

"""
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
"""