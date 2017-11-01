
# coding: utf-8

# In[11]:


import os
import pandas as pd

project_dir = os.path.join(os.path.dirname('__file__'), os.pardir)
output_file = os.path.join(project_dir, 'data', 'internet_speed_test_data.csv')
df = pd.read_csv(output_file)


# In[17]:


first_day = df.datetime.iloc[0].split(' ')[0]
last_day = df.datetime.iloc[-1].split(' ')[0]


# In[3]:


import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
import plotly.figure_factory as ff
print(py.__version__)
init_notebook_mode(connected=True)


# In[22]:


ping_data = [Scatter(x=df.datetime, y=df.ping)]
ping_layout = Layout(
    title=f'Ping Data from {first_day} to {last_day}',
    xaxis=dict(
        title='Time',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Ping in ms',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)

iplot(Figure(data=ping_data, layout=ping_layout))


# In[9]:


download_data = [Scatter(x=df.datetime, y=df.download)]
download_layout = Layout(
    title=f'Download Data from {first_day} to {last_day}',
    xaxis=dict(
        title='Time',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Download Speed in Mbit/s',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)

iplot(Figure(data=download_data, layout=download_layout))


# In[23]:


upload_data = [Scatter(x=df.datetime, y=df.upload)]
upload_layout = Layout(
    title=f'Upload Data from {first_day} to {last_day}',
    xaxis=dict(
        title='Time',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Upload in Mbit/s',
        titlefont=dict(
            size=18,
            color='#7f7f7f'
        )
    )
)

iplot(Figure(data=upload_data, layout=upload_layout))

