import sqlite3
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db_connection()
data_db = conn.execute('SELECT * FROM table_1').fetchall()
data_db_2 = conn.execute('SELECT * FROM table_2').fetchall()
data_db_3 = conn.execute('SELECT * FROM table_3').fetchall()
columns = conn.execute('SELECT * FROM table_1')
columns_2 = conn.execute('SELECT * FROM table_2')
columns_3 = conn.execute('SELECT * FROM table_3')

conn.close()

columns = list(map(lambda x: x[0], columns.description))
columns_2 = list(map(lambda x: x[0], columns_2.description))
columns_3 = list(map(lambda x: x[0], columns_3.description))

colors = ["#23F0E5", "#FF4500"]

labels = [label["labels"] for label in data_db]
values_digits = [value["values_digits"] for value in data_db]

labels_two = [label["labels"] for label in data_db_2]
values_digits_two = [value["values_digits"] for value in data_db_2]

labels_three = [label["labels"] for label in data_db_3]
values_digits_three = [value["Column_1"] for value in data_db_3]
values_digits_two_three = [value["Column_2"] for value in data_db_3]


df = pd.DataFrame({
    "Labels": labels,
    "Values": values_digits,
    "Labels_legend": labels
})
df_two = pd.DataFrame({
    "Labels_two": labels_two,
    "Values_two": values_digits_two,
    "Labels_legend_two": labels_two
})
df_three = pd.DataFrame({
    "Labels_three": labels_three,
    "Values_three": values_digits_three,
    "Values_three_two": values_digits_two_three,
    "Labels_legend_three": labels_three
})

fig = px.line(df, x="Labels", y="Values", title='Life expectancy in Canada', markers=True)
fig_two = px.line(df_two, x="Labels_two", y="Values_two", title='Life expectancy in Canada', markers=True)
fig_three = px.line(df_three, x="Labels_three", y=df_three.columns[1:3], title='Life expectancy in Canada', markers=True)


app.layout = html.Div(children=[

    html.Div([
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'width': '100%', 'height': '700px'}
    )
    ]),

    html.Div([
    html.H1(children='Hello Dash_two'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph_2',
        figure=fig_two,
        style={'width': '100%', 'height': '700px'}
    )
    ]),

    html.Div([
    html.H1(children='Hello Dash_three'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph_3',
        figure=fig_three,
        style={'width': '100%', 'height': '700px'}
    )
    ])

])


if __name__ == '__main__':
    app.run_server(debug=True)
