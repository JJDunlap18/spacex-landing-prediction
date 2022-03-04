import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Reading the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
spacex_df.head()

# Creating a dash application
app = dash.Dash(__name__)

# Creating an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # Adding a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown', options=[{'label': 'All Sites', 'value': 'ALL'},
                                                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                                                        value='ALL',
                                                                        placeholder="place holder here",
                                                                        searchable=True),
                                html.Br(),

                                # Adding a pie chart to show the total successful launches count for all sites
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # Adding a slider to select payload range
                                dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, marks={0: '0',100: '100'},
                                value=[min_payload, max_payload]),

                                # Adding a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# Adding a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', names='Launch Site', title='title')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df1 = filtered_df.groupby(['Launch Site', 'class']).size().reset_index(name= 'class count')
        filtered_df2 = filtered_df1[filtered_df1['Launch Site'] == entered_site] 
        
        fig = px.pie(filtered_df2, values= 'class count', names='class', title='title')
        return fig

# Adding a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))
def get_scatter_chart(entered_site, slider):
    a, b = slider
    filtered_df = spacex_df
    filtered_df = filtered_df[filtered_df['Payload Mass (kg)'].between(a,b)]
    # filtered_df = filtered_df.groupby(['Payload Mass (kg)', 'class']).size().reset_index(name= 'class count')
    # filtered_df2 = filtered_df[filtered_df['Payload Mass (kg)'] == entered_site]
    if entered_site == 'ALL':
        scatter_fig =px.scatter(filtered_df, x='Payload Mass (kg)', y='class', title='Correlation between Payload nad Success for all Sites', color='Booster Version Category')
        return scatter_fig
    else:
        # return the outcomes piechart for a selected site
        # filtered_df = filtered_df.groupby(['Payload Mass (kg)', 'class', 'Booster Version Category']).size().reset_index(name= 'class count')
        # filtered_df2 = filtered_df[filtered_df['Payload Mass (kg)'] == entered_site]
        # filtered_df1 = filtered_df.groupby(['Launch Site', 'class', 'Booster Version Category']).size().reset_index(name= 'class count')
        filtered_df2 = filtered_df[filtered_df['Launch Site'] == entered_site]
        
        scatter_fig = px.scatter(filtered_df2, x='Payload Mass (kg)', y='class', title='Correlation between Payload nad Success for all Sites', color='Booster Version Category')
        return scatter_fig


# Run the app
if __name__ == '__main__':
    app.run_server()
