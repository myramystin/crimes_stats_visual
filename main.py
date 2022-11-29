from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from prepare_data import df

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.Div([
        html.Div([
            dcc.Dropdown(options={"population": "Population", "medIncome": "Median Income",
                                  "pctDiv": "Percentage Divorced",
                                  "pctNotSpeakEnglWell": "Percentage Not Speaking English Well",
                                  "pctUnemployed": "Percentage Unemployed",
                                  "pctUrban": "Percentage Urban"}, value="population", id="feature")],
            style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown([i for i in df["state"].unique()], "AK", id="state")], style={'width': '49%',
                                                                                       'float': 'right',
                                                                                       'display': 'inline-block'}),
        dcc.Graph(id='graphic')
    ]),
    html.Div([
        dcc.Graph(id='full-graphic'),
        html.Div("Choose maximum median Income"),
        dcc.Slider(id="medincome_range",
                   min=df["medIncome"].min(),
                   max=df["medIncome"].max(),
                   step=10000),

        html.Div("Choose maximum Urban Percentage"),
        dcc.Slider(id="pcturban_range",
                   min=df["pctUrban"].min(),
                   max=df["pctUrban"].max(),
                   step=10
                   ),

        html.Div("Choose maximum Unemployed Percentage"),
        dcc.Slider(id="pctunemp_range",
                   min=df["pctUnemployed"].min(),
                   max=df["pctUnemployed"].max(),
                   step=10
                   ),
        html.Div("Choose maximum Not Speak English Well Percentage"),
        dcc.Slider(id="pctnoeng_range",
                   min=df["pctNotSpeakEnglWell"].min(),
                   max=df["pctNotSpeakEnglWell"].max(),
                   step=10
                   ),

        html.Div("Choose maximum divorce Percentage"),
        dcc.Slider(id="pctdiv_range",
                   min=df["pctDiv"].min(),
                   max=df["pctDiv"].max(),
                   step=10
                   ),
    ])
])


@app.callback(
    Output('graphic', 'figure'),
    Input('feature', 'value'),
    Input('state', 'value'))
def update_graph(feature_value, state_value):
    df_filtered = df[df["state"] == state_value]

    fig = px.histogram(
        df_filtered,
        y=["murders", "rapes", "robberies", "assaults", "burglaries", "larcenies", "autoTheft", "arsons"],
        x=feature_value,
        nbins=50)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 30, 'r': 40},
                      hovermode='closest',
                      xaxis_title=feature_value,
                      yaxis_title="Crimes Count",
                      title="Crimes Count by Different Features")

    return fig


@app.callback(
    Output('full-graphic', 'figure'),
    Input('medincome_range', 'value'),
    Input('pcturban_range', 'value'),
    Input('pctunemp_range', 'value'),
    Input('pctnoeng_range', 'value'),
    Input('pctdiv_range', 'value'))
def update_full_graph(med_income, pct_urban, pct_unemp, pct_noeng, pct_div):
    local_df = df[df["medIncome"] <= med_income]
    local_df = local_df[local_df["pctUrban"] <= pct_urban]
    local_df = local_df[local_df["pctUnemployed"] <= pct_unemp]
    local_df = local_df[local_df["pctNotSpeakEnglWell"] <= pct_noeng]
    local_df = local_df[local_df["pctDiv"] <= pct_div]

    fig = px.histogram(local_df,
                       x="population",
                       y=["murders", "rapes", "robberies", "assaults", "burglaries", "larcenies", "autoTheft",
                          "arsons"])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 30, 'r': 40}, hovermode='closest',
                      xaxis_title="Population",
                      yaxis_title="Crimes Count")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)

"""
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
"""
