import streamlit as st
import praw
import pandas as pd
import re
import matplotlib.pyplot as plt
import altair as alt

# Initialize PRAW
reddit = praw.Reddit(client_id='JkfJB2XfxEgfzy30JDEJCg',
                     client_secret='qrhKm0KamdR9Zo-sxsZNBq1wsSv4NA',
                     user_agent='Dapper_Echo1667',
                     read_only = True)

def Extract(limit):

    # define regular expressions to match keywords related to telecom fraud
    fraud_keywords = [
        re.compile(r'telecom scam', re.IGNORECASE),
        re.compile(r'phone fraud', re.IGNORECASE),
        re.compile(r'billing fraud', re.IGNORECASE),
        re.compile(r'identity theft', re.IGNORECASE)
    ]

    # Define subreddit and search query
    subreddit = reddit.subreddit('All')
    search_query = 'telecom fraud'

    # Get posts from subreddit
    posts = subreddit.search(search_query, limit= limit)

    # Create list of dictionaries for each post
    post_list = []
    for post in posts:
        title_matches = any(keyword.search(post.title) for keyword in fraud_keywords)
        body_matches = any(keyword.search(post.selftext) for keyword in fraud_keywords)
        post_dict = {
            'title': post.title,
            'created_utc': post.created_utc,
            'username':post.author.name,
            'post text':post.selftext
        }
        #If key words are detected append the list
        if title_matches or body_matches:
            post_list.append(post_dict)

    # Create pandas DataFrame from list of dictionaries
    df = pd.DataFrame(post_list)
    return df

st.set_page_config(page_title="Ubo G", page_icon="favico.ico")

st.sidebar.title('Reddit Data Analysis')

limit = st.sidebar.slider('Select number of posts to analyze:', 1, 1000, 10)

# Get data from Reddit API
df = Extract(limit = None)



# Convert created_utc  column to datetime format
df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')

# Resample DataFrame to count number of posts per day
df_resampled = df.resample('D', on='created_utc').count()

st.header('Line Chart of Telecom Fraud Daily Posts')
# # Create line chart with Streamlit
st.line_chart(df_resampled['title'])


# Set dataframe height and width
height = 200
width = 500

st.header('Top Posts')
st.write(df, height = height, width = width)

# Check frequency of username column
username = df['username'].value_counts().reset_index()
username.columns = ['Username','count']

fig, ax = plt.subplots()
ax.bar(username['Username'], username['count'])
ax.set_xlabel('Usernames')
ax.set_ylabel('Number')
ax.set_title('Number of Posts Per Username')

# Display the plot in Streamlit
height = 50
width = 50
st.header('Number of posts  Per Username')
st.pyplot(fig,height = height,width =width)