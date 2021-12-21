import dash
import dash_core_components as dcc
import dash_html_components as html

from main import make_dfs

"""Make Dashboard at http://127.0.0.1:8050/"""
app = dash.Dash(__name__)

def serve_layout():

    figures = []

    for df in make_dfs():
        figure = {
            "data": [
                {
                    "x": df["created_at"],
                    "y": df["price"],
                    "type": "lines",
                },
            ],
            "layout": {"title": df['title'][0]},
        }

        figures.append(figure)

    children = [html.H1(children="Instrument prices",)] + \
            [dcc.Graph(figure=f) for f in figures]

    return html.Div(children=children)

# Refresh layout by pressing the refresh button
app.layout = serve_layout
   
if __name__ == "__main__":
    app.run_server(debug=True)
