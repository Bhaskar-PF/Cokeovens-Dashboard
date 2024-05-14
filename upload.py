import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css 4']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Upload(
    id='upload-data',
    children=html.Div([
    'Drag and Drop or ',
    html.A('Select Files') 
    ]),
    style={
    'width': '100%',
    'height': '60px',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin': '10px'
    },
    # Allow multiple files to be uploaded
    multiple=True
    ),
    html.Div(id='output-data-upload'),
    dbc.Button("Download",
    color='danger',
    # className='btn_schedule_button',
    # outline=True,
    id='download_sch',
    n_clicks=0),
    dcc.Download(id='download_file'),
    ])


def convert(df):

    df1=df.iloc[12:,:].reset_index(drop=True)
    a=2
    temp=[]
    while a<df1.shape[0]:
        temp.append(int(df1.iloc[a,0]))
        a+=4
    b=0
    status=[]
    while b<df1.shape[0]:
        status.append(df1.iloc[b,0])
        b+=4

    c=1
    Emissivity=[]
    while c<df1.shape[0]:
        Emissivity.append(float(df1.iloc[c,0]))
        c+=4

    d=3
    Thermocouple=[]
    while d<df1.shape[0]:
        Thermocouple.append(int(df1.iloc[d,0]))
        d+=4
    # df=pd.read_excel('sample1.xls', engine='xlrd')
    df_main=pd.DataFrame({'No':[i for i in range(1, len(status)+1)], 'Status':status, 'Emissivity':Emissivity, 'Thermometer': temp, 'Thermocouple':Thermocouple})
    df_main.to_excel('output.xlsx', index=False)

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            convert(df)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            convert(df)
        else:
            print(filename)
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

@app.callback(Output('output-data-upload', 'children'),
[Input('upload-data', 'contents')],
[State('upload-data', 'filename'),
State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        print(111111111111111111111111111111111111111)
        children = [
        parse_contents(c, n, d) for c, n, d in
        zip(list_of_contents, list_of_names, list_of_dates)]
        # return children
        return 'Success'


@app.callback(
    Output('download_file','data'),
    Input('download_sch','n_clicks'),
)
def download(download):
    if download>0:
        return dcc.send_file('./output.xlsx')
    else:
        return None

if __name__ == '__main__':
    app.run_server(debug=True, host='10.10.10.10', port=8090)
