import facebook
import json
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    return ' '.join(tokens)

access_token = "EAAOS1oxIZA78BO8EmRYDidBLdwU7bTLYbtK3St8FgzT2pvq2VUF5sAMoJcZBq4KuPQjEZCd3gIhAr30llXfKkvmfOpI59QsbxLsKJuCeTMmI8LVnSAuU1dmsTVIjMNjgPpP4bJXaZBfGzzVQk2IVahHHmARn7Ojz8EI8SOVr6LD9ZCtkAhs5G4AjHVMWbYrRPnq2cT8kPxsrDnarQ9UWEZBySq7MXMpDQ0GzYjQJ3lCZCPqzxXZCbKMUcdjmoxXcty4ZD"

graph = facebook.GraphAPI(access_token)

posts = graph.get_connections(id='me', connection_name='posts')

with open('posts.json', 'w') as f:
    json.dump(posts, f, indent=4)

with open('posts.json', 'r') as f:
    posts = json.load(f)['data']

preprocessed_data = []
for post in posts:
    if 'message' in post:
        preprocessed_text = preprocess_text(post['message'])
        preprocessed_data.append(preprocessed_text)

sentiment_data = []
for text in preprocessed_data:
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    sentiment_data.append(sentiment)

plt.hist(sentiment_data, bins=10)
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Analysis of Facebook Posts')
plt.show()
