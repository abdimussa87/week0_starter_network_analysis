import os, sys
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# Add parent directory to path to import modules from src
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader
import src.utils as utils

# Initialize DataLoader
data_loader = SlackDataLoader("../anonymized")
all_week_1_path = os.path.join("../anonymized", 'all-week1/')
week1_df = utils.slack_parser(all_week_1_path)
week1_df.head()

def get_top_20_user(data, channel='Random'):
    """get user with the highest number of message sent to any channel"""

    data['sender_name'].value_counts()[:20].plot.bar(figsize=(15, 7.5))
    plt.title(f'Top 20 Message Senders in #{channel} channels', size=15, fontweight='bold')
    plt.xlabel("Sender Name", size=18); plt.ylabel("Frequency", size=14);
    plt.xticks(size=12); plt.yticks(size=12);
    plt.show()

st.set_page_config(
    page_title="ChatGPT",
    page_icon=":robot:"
)


st.subheader('Dashboard')

# All Week 1 Section
with st.container():
    st.write('---')
    st.title('All week 1 Channel')
    st.dataframe(week1_df)
