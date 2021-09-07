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
