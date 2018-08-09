# import libraries
import praw
import time


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')


def get_data():
    raw_data = []
    for submission in reddit.subreddit('tropicalweather').hot(limit=25):
        if submission.distinguished == 'moderator':
            timestamp = time.time()
            title = submission.title
            url = submission.url
            raw_data.append({'timestamp': timestamp, 'title': title, 'url': url})

    return raw_data


def main(event, context):
    data = get_data()
    return data
