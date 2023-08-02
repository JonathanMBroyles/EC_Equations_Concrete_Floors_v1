#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


# In[2]:


# Define a function to predict the EC for the ten concrete floors for the conceptual design phase
def conceptual_EQs(systems, span_length, units, span_range_type):
    EC_ests = []
    Notes = []
    if units == "Metric":
        if span_range_type == "Full Span Range":
            for i in range(len(systems)):
                if systems[i] == "RC Flat Plate":
                    EC = (0.85 * (span_length ** 2)) + (13.81 * span_length) - 1.1
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Flat Slab":
                    EC = (0.84 * (span_length ** 2)) + (13.84 * span_length) + 0.5
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC One-Way Slab":
                    EC = (1.83 * (span_length ** 2)) - (19.08 * span_length) + 126
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Two-Way Slab with Beams":
                    EC = (0.62 * (span_length ** 2)) - (0.99 * span_length) + 73
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Two-Way Waffle Slab":
                    EC = (0.17 * (span_length ** 2)) + (2.34 * span_length) + 63
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Voided Plate":
                    EC = (1.18 * (span_length ** 2)) + (0.22 * span_length) + 48
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Flat Plate":
                    EC = (0.83 * (span_length ** 2)) + (3.37 * span_length) + 31
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Hollow Core Slab":
                    EC = (0.97 * (span_length ** 2)) - (5.30 * span_length) + 71
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Voided Plate - Ortho":
                    EC = (1.11 * (span_length ** 2)) - (7.78 * span_length) + 77
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Voided Plate - Diag":
                    EC = (1.19 * (span_length ** 2)) - (9.68 * span_length) + 85
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                Notes = "None"
            return EC_ests, Notes
        
        elif span_range_type == "Economic Span Range":
            for i in range(len(systems)):
                if systems[i] == "RC Flat Plate":
                    EC = (1.16 * (span_length ** 2)) + (9.90 * span_length) + 9.8
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 9:
                        Note = "Span Length Outside of Economic Span Range (RC Flat Plate: 3m - 9m)"
                        Notes.append(Note)
                elif systems[i] == "RC Flat Slab":
                    EC = (0.76 * (span_length ** 2)) + (15.44 * span_length) - 7.7
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6 or span_length > 12:
                        Note = "Span Length Outside of Economic Range (RC Flat Slab: 6m - 12m)"
                        Notes.append(Note)
                elif systems[i] == "RC One-Way Slab":
                    EC = (1.32 * (span_length ** 2)) - (11.08 * span_length) + 100
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 9:
                        Note = "Span Length Outside of Economic Range (RC One-Way Slab: 3m - 9m)"
                        Notes.append(Note)
                elif systems[i] == "RC Two-Way Slab with Beams":
                    EC = (0.78 * (span_length ** 2)) - (3.38 * span_length) + 81
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6 or span_length > 12:
                        Note = "Span Length Outside of Economic Range (RC Two-Way Slab with Beams: 6m - 12m)"
                        Notes.append(Note)
                elif systems[i] == "RC Two-Way Waffle Slab":
                    EC = (-1.4 * (span_length ** 2)) + (37.76 * span_length) - 128
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 9:
                        Note = "Span Length Outside of Economic Range (RC Two-Way Waffle Slab: 9m - 15m)"
                        Notes.append(Note)
                elif systems[i] == "RC Voided Plate":
                    EC = (1.37 * (span_length ** 2)) - (2.27 * span_length) + 54
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6 or span_length > 12:
                        Note = "Span Length Outside of Economic Range (RC Voided Plate: 6m - 12m)"
                        Notes.append(Note)
                elif systems[i] == "PT Flat Plate":
                    EC = (0.89 * (span_length ** 2)) + (1.91 * span_length) + 39
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6:
                        Note = "Span Length Outside of Economic Range (PT Flat Plate: 6m - 15m)"
                        Notes.append(Note)
                elif systems[i] == "PT Hollow Core Slab":
                    EC = (1.08 * (span_length ** 2)) - (6.68 * span_length) + 76
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 12:
                        Note = "Span Length Outside of Economic Range (PT Hollow Core Slab: 3m - 12m)"
                        Notes.append(Note)
                elif systems[i] == "PT Voided Plate - Ortho":
                    EC = (1.01 * (span_length ** 2)) - (5.50 * span_length) + 65
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6:
                        Note = "Span Length Outside of Economic Range (PT Voided Plate (Orth): 6m - 15m)"
                        Notes.append(Note)
                elif systems[i] == "PT Voided Plate - Diag":
                    EC = (1.09 * (span_length ** 2)) - (7.52 * span_length) + 74
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 6:
                        Note = "Span Length Outside of Economic Range (PT Voided Plate (Diag): 6m - 15m)"
                        Notes.append(Note)
            return EC_ests, Notes
    elif units == "Imperial":
        if span_range_type == "Full Span Range":
            for i in range(len(systems)):
                if systems[i] == "RC Flat Plate":
                    EC = (0.08 * (span_length ** 2)) + (4.14 * span_length) - 1.1
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Flat Slab":
                    EC = (0.08 * (span_length ** 2)) + (4.15 * span_length) + 0.5
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC One-Way Slab":
                    EC = (0.16 * (span_length ** 2)) - (5.73 * span_length) + 126
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Two-Way Slab with Beams":
                    EC = (0.06 * (span_length ** 2)) - (0.30 * span_length) + 73
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Two-Way Waffle Slab":
                    EC = (0.02 * (span_length ** 2)) + (0.70 * span_length) + 63
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "RC Voided Plate":
                    EC = (0.11 * (span_length ** 2)) + (0.07 * span_length) + 48
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Flat Plate":
                    EC = (0.07 * (span_length ** 2)) + (1.01 * span_length) + 31
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Hollow Core Slab":
                    EC = (0.09 * (span_length ** 2)) - (1.59 * span_length) + 71
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Voided Plate - Ortho":
                    EC = (0.10 * (span_length ** 2)) - (2.34 * span_length) + 77
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                elif systems[i] == "PT Voided Plate - Diag":
                    EC = (0.11 * (span_length ** 2)) - (2.91 * span_length) + 85
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                Notes = "None"
            return EC_ests, Notes
        
        elif span_range_type == "Economic Span Range":
            for i in range(len(systems)):
                if systems[i] == "RC Flat Plate":
                    EC = (0.10 * (span_length ** 2)) + (2.97 * span_length) + 9.8
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 30:
                        Note = "Span Length Outside of Economic Span Range (RC Flat Plate: 10ft - 30ft)"
                        Notes.append(Note)
                elif systems[i] == "RC Flat Slab":
                    EC = (0.07 * (span_length ** 2)) + (4.63 * span_length) - 7.7
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20 or span_length > 40:
                        Note = "Span Length Outside of Economic Range (RC Flat Slab: 20ft - 40ft)"
                        Notes.append(Note)
                elif systems[i] == "RC One-Way Slab":
                    EC = (0.12 * (span_length ** 2)) - (3.32 * span_length) + 100
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 30:
                        Note = "Span Length Outside of Economic Range (RC One-Way Slab: 10ft - 30ft)"
                        Notes.append(Note)
                elif systems[i] == "RC Two-Way Slab with Beams":
                    EC = (0.07 * (span_length ** 2)) - (1.01 * span_length) + 81
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20 or span_length > 40:
                        Note = "Span Length Outside of Economic Range (RC Two-Way Slab with Beams: 20ft - 40ft)"
                        Notes.append(Note)
                elif systems[i] == "RC Two-Way Waffle Slab":
                    EC = (-0.13 * (span_length ** 2)) + (11.33 * span_length) - 128
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 30:
                        Note = "Span Length Outside of Economic Range (RC Two-Way Waffle Slab: 30ft - 50ft)"
                        Notes.append(Note)
                elif systems[i] == "RC Voided Plate":
                    EC = (0.12 * (span_length ** 2)) - (0.68 * span_length) + 54
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20 or span_length > 40:
                        Note = "Span Length Outside of Economic Range (RC Voided Plate: 20ft - 40ft)"
                        Notes.append(Note)
                elif systems[i] == "PT Flat Plate":
                    EC = (0.08 * (span_length ** 2)) + (0.57 * span_length) + 39
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20:
                        Note = "Span Length Outside of Economic Range (PT Flat Plate: 20ft - 50ft)"
                        Notes.append(Note)
                elif systems[i] == "PT Hollow Core Slab":
                    EC = (0.10 * (span_length ** 2)) - (2.00 * span_length) + 76
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length > 40:
                        Note = "Span Length Outside of Economic Range (PT Hollow Core Slab: 10ft - 40ft)"
                        Notes.append(Note)
                elif systems[i] == "PT Voided Plate - Ortho":
                    EC = (0.09 * (span_length ** 2)) - (1.65 * span_length) + 65
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20:
                        Note = "Span Length Outside of Economic Range (PT Voided Plate (Orth): 20ft - 50ft)"
                        Notes.append(Note)
                elif systems[i] == "PT Voided Plate - Diag":
                    EC = (0.10 * (span_length ** 2)) - (2.26 * span_length) + 74
                    EC = round(EC, 2)
                    EC_ests.append(EC)
                    if span_length < 20:
                        Note = "Span Length Outside of Economic Range (PT Voided Plate (Diag): 20ft - 50ft)"
                        Notes.append(Note)
            return EC_ests, Notes


# In[3]:


# create the multi-page web app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

home_page_layout = html.Div([
    html.H1('Estimating the embodied carbon of concrete floor systems for early-stage design',
           style = {'textAlign': 'center'}),
    html.Br(),
    html.P('Welcome to the tool for estimating the EC of concrete floors! :)'),
    html.A('Go to the EC Equations for the Conceptual Design Phase', href='/conceptual_EQs'),
    html.Br(),
    html.A('Go to the EC Equations for the Preliminary Design Phase', href='/preliminary_EQs'),
    html.Div(children='The web application is a service provided by the Pennsylvania State Department of Architectural Engineering, created by Mr. Jonathan M. Broyles, under supervision of Dr. Nathan C. Brown. The equations employed in the web application were developed as part of a publication titled: Equations for early-stage design embodied carbon estimation for concrete floors of varying loading and strength.', 
                 style={'backgroundColor': '#003087', # Penn State Color: #003087
                        'padding': '10px', 
                        'position': 'fixed',
                        'font': 'Courier New',
                        'font-size': "12px",
                        'color': 'white',
                        'bottom': '10px', 
                        'width': '100%'})
], style = {'margin': 20})

# Page 1: Conceptual Design Phase Embodied Carbon Equations
page1_layout = html.Div(
        html.H2('Estimating Embodied Carbon in the Conceptual Design Phase', style={'padding': '10px'})), html.Div([
        html.Br(),
        html.H6("Unit System", style = {"textAlign": "left", 'padding': '10px', 'margin': 0}),
        dcc.RadioItems(
            id="Unit System",
            options=["Imperial", "Metric"],
            value="Imperial", inline=True, inputStyle={"margin-left": "20px", "margin-right": "5px"}),
        html.Br(),
        html.H4("Concrete Floor Systems", style = {"textAlign": "left", 'padding': '10px', 'margin': 0}),
        dcc.Checklist(
            id="Floor System Checklist",
            options=["RC Flat Plate", "RC Flat Slab", "RC One-Way Slab", "RC Two-Way Slab with Beams", "RC Two-Way Waffle Slab", "RC Voided Plate", "PT Flat Plate", "PT Hollow Core Slab", "PT Voided Plate - Ortho", "PT Voided Plate - Diag"],
            value=["RC Flat Plate", "RC Voided Plate", "PT Flat Plate"], 
            inline=True, 
            inputStyle = {'padding': '10px', "margin-left": "20px", "margin-right": "10px"}),
        html.Br(),
        html.H4("Span Length", style = {"textAlign": "left", 'padding': '10px', 'margin': 0}),
#         html.Div(id='Span Length'),
        dcc.Slider(min = 10, max = 50, marks={
                10: '10 ft',
                20: '20 ft',
                30: '30 ft',
                40: '40 ft',
                50: '50 ft '
            }, value = 20,
            tooltip={"placement": "bottom", "always_visible": True},
            updatemode = "drag",
            id = "Span Length"),
        html.Br(),
        html.H6("Consider a broad span range or a floor-specific economic span range?", style = {"textAlign": "left", 'padding': '10px', 'margin': 0}),
        dcc.RadioItems(
            id="Span Length Range",
            options=["Full Span Range", "Economic Span Range"],
            value="Full Span Range", inline=True, inputStyle={"margin-left": "20px", "margin-right": "5px"}),
        html.Div(children='The web application is a service provided by the Pennsylvania State Department of Architectural Engineering, created by Mr. Jonathan M. Broyles, under supervision of Dr. Nathan C. Brown. The equations employed in the web application were developed as part of a publication titled: Equations for early-stage design embodied carbon estimation for concrete floors of varying loading and strength.', 
                     style={'backgroundColor': '#003087', # Penn State Color: #003087
                            'padding': '10px', 
                            'position': 'fixed',
                            'font': 'Courier New',
                            'font-size': "12px",
                            'color': 'white',
                            'bottom': '10px', 
                            'width': '100%'})
    ], style={'width': '50%', 'float': 'left', 'display': 'inline-block'}), html.Div([
        html.Br(),
        html.H4("Estimated Embodied Carbon", style = {"textAlign": "Center", 'padding': '10px', 'margin': 0}),
        dcc.Graph(id='Comparing_EC_Conceptual'),
], style={'width': '50%', 'float': 'right', 'display': 'inline-block'}), html.Div([
        html.Br(),
        html.A('Go to the EC Equations for the Preliminary Design Phase', href='/preliminary_EQs'),
])

# Page 2: Preliminary Design Phase Material Quantity and Embodied Carbon Equations
page2_layout = html.Div([
    html.H1('Estimating Embodied Carbon in the Preliminary Design Phase'), html.Div([
        html.Br(),
        html.A('Go to the EC Equations for the Conceptual Design Phase', href='/conceptual_EQs'),
    ]),
    # Add your components and content here
    html.Div(children='The web application is a service provided by the Pennsylvania State Department of Architectural Engineering, created by Mr. Jonathan M. Broyles, under supervision of Dr. Nathan C. Brown. The equations employed in the web application were developed as part of a publication titled: Equations for early-stage design embodied carbon estimation for concrete floors of varying loading and strength.', 
                 style={'backgroundColor': '#003087', # Penn State Color: #003087
                        'padding': '10px', 
                        'position': 'fixed',
                        'font': 'Courier New',
                        'font-size': "12px",
                        'color': 'white',
                        'bottom': '10px', 
                        'width': '100%'})  
    ])
   
    
# define the callback for the title page
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/conceptual_EQs':
        return page1_layout
    elif pathname == '/preliminary_EQs':
        return page2_layout
    else:
        return home_page_layout
    
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('Comparing_EC_Conceptual', 'figure'),
              [Input('Unit System', 'value'),
               Input('Floor System Checklist', 'value'),
               Input('Span Length', 'value'),
               Input('Span Length Range', 'value')])

# def update_figure(units, systems, slider_type, span_range_type, span_length_imperial, span_length_metric):
def update_figure(units, systems, span_length, span_range_type):
#     if slider_type == "Imperial":
#         span_length = span_length_imperial
#     else:
#         span_length = span_length_metric
    concept_EC_data_live, notes_live = conceptual_EQs(systems, span_length, units, span_range_type)
    d_concept_EQ_live = {'Floor System':systems,'EC':concept_EC_data_live}
    df_concept_EQ_live = pd.DataFrame(d_concept_EQ_live)
    
    fig = px.bar(df_concept_EQ_live, x="EC", y="Floor System", orientation='h', template = "plotly_white", color="EC", color_continuous_scale=px.colors.sequential.Viridis_r)
    fig.update_traces()
    fig.update_layout(
    title=None,
    margin=dict(pad=20),
    xaxis_title="Estimated Total Embodied Carbon (kg CO<sub>2</sub>e/m<sup>2</sup>)", 
    yaxis_title="Floor System",
    font_family="Arial",
    font=dict(size=16, color="black"))
    print(notes_live)
    
    return fig

# run the app
if __name__ == '__main__':
    app.run_server(debug=False, port=8009)


# In[ ]:





# In[ ]:




