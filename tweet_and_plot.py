import matplotlib.pyplot as plt
from wordcloud import WordCloud

def extract_tags(tweet):
    itemIsHashtag = lambda e: e[0] == "#"
    hashtagWithoutPound = lambda e: e[1:]
    return list(map(hashtagWithoutPound, filter(itemIsHashtag, tweet.split())))


stream = open('tweets.txt', 'r')
tweets = stream.readlines()
stream.close()

hashtags_in_file = []
for tweet in tweets:
    for hashtag in extract_tags(tweet):
        hashtags_in_file.append(hashtag)
print(hashtags_in_file)

stream = open('tweets.txt', 'r')
wordcloud = WordCloud(max_font_size=40).generate(stream.read())
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
stream.close()
