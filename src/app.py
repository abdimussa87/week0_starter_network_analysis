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
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer


# Initialize DataLoader
data_loader = SlackDataLoader("../anonymized")
all_week_1_path = os.path.join("../anonymized", 'all-week1/')
week1_df = data_loader.slack_parser(all_week_1_path)

db = db_utils.DBWithSchema()
channel_messages =  db.find_all('channel_messages_test')
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

def users_with_the_most_reply_count(data, channel='Random'):
   users_with_the_most_reply_count = data.groupby('sender_name')['reply_count'].mean().sort_values(ascending=False)[:20].to_frame(name='count').reset_index()
   users_with_the_most_reply_count.columns = ['sender_name', 'reply_count']

   st.bar_chart(users_with_the_most_reply_count, x='sender_name', y='reply_count', use_container_width=True)

def show_sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    # run the polarity test on the dataset
    results = {}
    for i, row in week1_df.iterrows():
        message_content = row['msg_content']
        results[message_content] =sia.polarity_scores(message_content)
    

    # generate DataFrame that has been transposed
    vaders = pd.DataFrame(results).T    
    # renaming the index column so that we have a common column when merging
    vaders = vaders.reset_index().rename(columns={'index': 'msg_content'})
    vaders = vaders.merge(week1_df, how='right')
    st.write(vaders.head())



st.set_page_config(
    page_title="10Academy Slack Dashboard",
    page_icon=":robot:",
    layout="wide",
)


st.header('Dashboard')

# All Week 1 Section
with st.container():
    st.write('---')
    st.subheader('All week 1 Channel')
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

st.write('---')

with st.container():
    st.subheader('Users with the most reply count')
    st.write(f'Users with the most reply count in #all-week-1 channel', size=15, fontweight='bold')

    users_with_the_most_reply_count(week1_df, 'all-week-1')

st.write('---')

with st.container():
    st.subheader('Sentiment Analysis')
    st.write('This is the sentiment analysis of the messages in the "all-week-1" channel with the help of nltk library')
    show_sentiment_analysis()