# Import required libraries
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd

# Load sample data for migration patterns
data = {
    "Source": ["Asia", "Asia", "Africa", "Europe", "South America"],
    "Destination": ["North America", "Europe", "Europe", "North America", "Europe"],
    "Migrants": [10500000, 5000000, 6200000, 7800000, 4500000],
    "Year": [2015, 2016, 2017, 2018, 2019]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = Dash(__name__)

# Create visualizations
# Sankey Diagram for migration flow
fig_sankey = px.sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.5),
        label=list(set(df['Source'].tolist() + df['Destination'].tolist())),
    ),
    link=dict(
        source=df['Source'].apply(lambda x: list(set(df['Source'])).index(x)),
        target=df['Destination'].apply(lambda x: list(set(df['Destination'])).index(x)),
        value=df['Migrants'],
    ),
    title="Migration Flow Between Regions"
)

# Time-series trend
fig_line = px.line(
    df,
    x="Year",
    y="Migrants",
    color="Source",
    title="Migration Trends Over Time",
    labels={"Migrants": "Number of Migrants", "Year": "Year"},
    markers=True
)

# Layout for the app
app.layout = html.Div([
    html.Header([
        html.H1("Migration Patterns Dashboard", style={"textAlign": "center", "padding": "10px", "backgroundColor": "#f4f4f9", "color": "#4a4e69"}),
    ], style={"marginBottom": "20px"}),

    # Section for Sankey Diagram
    html.Div([
        html.H3("Migration Flow Visualization", style={"textAlign": "center"}),
        dcc.Graph(id="sankey_diagram", figure=fig_sankey, config={"displayModeBar": False}),
    ], style={"marginBottom": "30px", "padding": "20px", "backgroundColor": "#f7f7f7", "borderRadius": "8px"}),

    # Section for Line Chart
    html.Div([
        html.H3("Migration Trends Over Time", style={"textAlign": "center"}),
        dcc.Graph(id="line_chart", figure=fig_line, config={"displayModeBar": False}),
    ], style={"marginBottom": "30px", "padding": "20px", "backgroundColor": "#f7f7f7", "borderRadius": "8px"}),

    # Data Table Section
    html.Div([
        html.H3("Raw Data Table", style={"textAlign": "center"}),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center", "padding": "10px", "border": "1px solid #ccc"},
            style_header={"backgroundColor": "#4a4e69", "color": "white", "fontWeight": "bold"},
            style_data={"backgroundColor": "#f4f4f9"},
        ),
    ], style={"padding": "20px", "backgroundColor": "#f7f7f7", "borderRadius": "8px"}),
], style={"fontFamily": "Arial, sans-serif", "margin": "0 auto", "maxWidth": "1200px", "padding": "20px"})

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
