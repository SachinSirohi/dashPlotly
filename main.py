# -*- coding: utf-8 -*-

import altair as alt
from vega_datasets import data
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc

# Data import

barley = data.barley()
chart1 = barley.groupby(['site', 'year'])[['yield']].median().reset_index()
chart2 = barley.groupby(['site', 'variety'])[['yield']].sum().reset_index()

# Graph1

fig1 = px.line(
    chart1,
    x='year',
    y='yield',
    color='site',
    labels='site',
    width=800,
    height=800,
    )
fig1.update_yaxes(
    range=[0, max(chart1['yield'])],
    title='Median of yield',
    showline=True,
    linewidth=0.5,
    linecolor='gray',
    showgrid=True,
    gridwidth=0.5,
    gridcolor='grey',
    mirror=True,
    )
fig1.update_xaxes(type='category', showline=True, linewidth=0.5,
                  linecolor='gray', mirror=True)
fig1.layout.plot_bgcolor = '#fff'
fig1.layout.paper_bgcolor = '#fff'

# fig1.show()

# Graph2

fig2 = px.bar(
    chart2,
    x='variety',
    y='yield',
    color='site',
    width=800,
    height=800,
    )
fig2.update_yaxes(
    range=[0, 500],
    title='Sum of yield',
    showline=True,
    linewidth=0.5,
    linecolor='gray',
    showgrid=True,
    gridwidth=0.5,
    gridcolor='grey',
    mirror=True,
    )
fig2.update_xaxes(
    type='category',
    showline=True,
    linewidth=0.5,
    linecolor='gray',
    tickangle=90,
    mirror=True,
    )
fig2.layout.plot_bgcolor = '#fff'
fig2.layout.paper_bgcolor = '#fff'

# fig2.show()

app = dash.Dash()
app.layout = html.Div(children=[dcc.Graph(id='g1', figure=fig1, style={
    'display': 'inline-block',
    'height': '50%',
    'width': '50%',
    'textAlign': 'center',
    }), dcc.Graph(id='g2', figure=fig2, style={
        'display': 'inline-block',
        'height': '50%',
        'width': '50%',
        'textAlign': 'center'})],
    style={'textAlign': 'center'})

app.css.append_css(
    {'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
