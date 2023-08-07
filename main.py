import snscrape.modules.twitter as sntwitter
import pandas as pd
import re

#!!!!!!! the used scraper-implementation does not work any longer since the changes to the Twitter API !!!!!!!
# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:Berliner_Fw').get_items()):
    if i > 20000:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.content])
    
    
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Number of Likes", "Source of Tweet", "Tweets"])
    



v = tweets_df['Tweets'].tolist()

hashtag_list = []

#Text Cleaning:
for text in v:
    text = text.rstrip()
    text = re.sub("\r", " ", text)
    text = re.sub("\n", " ", text)
    text = text.replace('"', ' ')
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    print(text)
    hashtag_list.append(text)



tweets_df = pd.DataFrame({'Tweets': hashtag_list})

#export data
tweets_df.to_csv('Tweets-V2.csv', index=False)




