# tropicalweather-api-python
Simple PRAW script to get the top 25 posts of Hot on the /r/TropicalWeather subreddit and filter by moderator

Works well with AWS Lambda as long as packages are included in the upload

If you want to run your own version, fill these variables with Reddit API credentials:

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')
