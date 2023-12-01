import os, sys
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# Add parent directory to path to import modules from src
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
import pprint

from src.loader import SlackDataLoader
import src.utils as utils
import src.db_utils as db_utils

# Initialize DataLoader
data_loader = SlackDataLoader("../anonymized")
all_week_1_path = os.path.join("../anonymized", 'all-week1/')
week1_df = data_loader.slack_parser(all_week_1_path)

db = db_utils.DBWithSchema()
channel_messages =  db.find_all('channel_messages')
channel_messages_cleaned=[]

for channel in channel_messages:
    channel['_id']=str(channel.get('_id'))
    channel_messages_cleaned.append(channel)



def get_top_20_message_senders(data, channel='Random'):
    """get user with the highest number of message sent to any channel"""

    top_20_senders = data['sender_name'].value_counts()[:20].to_frame(name='count').reset_index()
    top_20_senders.columns = ['sender_name', 'message_count']
    st.write(f'Top 20 Message Senders in #{channel} channel', size=15, fontweight='bold')
    st.bar_chart(top_20_senders, x='sender_name', y='message_count', use_container_width=True)

def get_bottom_20_message_senders(data, channel='Random'):
    """get user with the lowest number of message sent to any channel"""

    bottom_20_senders = data['sender_name'].value_counts()[-20:].to_frame(name='count').reset_index()
    bottom_20_senders.columns = ['sender_name', 'message_count']
    st.write(f'Bottom 20 Message Senders in #{channel} channel', size=15, fontweight='bold')
    st.bar_chart(bottom_20_senders, x='sender_name', y='message_count', use_container_width=True)


st.set_page_config(
    page_title="10Academy Slack Dashboard",
    page_icon=":robot:",
    layout="wide",
)


st.subheader('Dashboard')

# All Week 1 Section
with st.container():
    st.write('---')
    st.title('All week 1 Channel')
    st.write("This is the data loaded for the 'all-week-1' channel slack messages")
    st.dataframe(channel_messages_cleaned)

st.write('---')
col_1 , col_2 = st.columns(2)
with col_1:
    
    st.subheader('Top 20 Message Senders')
    get_top_20_message_senders(week1_df, 'all-week-1')
with col_2:
    st.subheader('Bottom 20 Message Senders')
    get_bottom_20_message_senders(week1_df, 'all-week-1')