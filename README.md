# Twitter-Sentiment-Analysis

## 1. Setting up software:
Tweepy is a Python framework used to access the Twitter API. We start off by installing
python v3.7.1. Using pip (python installation package) module for python we install
the Tweepy framework.
Login in to twitter development section and create an App.
Fill the details of the Application to be created (which in this case is the analysis module
we are going to create).
On clicking the “create your Twitter Application”, details of the new app will be
shown alongside the consumer key and consumer secret.
The consumer key is the API key associated with Twitter that identifies the client.
The consumer secret is the password used by the client to authenticate the API calls.
To generate the access token the “create my access token” button is pressed. The token
is then generated. Access token is what is issued to the client successfully
authenticates itself.
A python code is written to verify if tweepy has been installed correctly and to check if
the Twitter API can be accessed.
TextBlob is also another python library that needs to be installed. It is used for
processing text data. This can be installed using pip (the same way as mentioned
earlier).

## 2. Collecting data:
Using various # filters on Twitter with the help of tweepy and the Twitter API, datasets
are collected.
These datasets will be selected in such a way that the noise levels will be low.
The different filters used are:
#Climate
#India
#UN
#WHO
#World

## 3. Analysing Data:
Different parameters will be used to analyse the data collected.
The data is split into tokens which makes it easier to recognize the sentiment the data
is carrying. Ex: “The sun is very bright today and it is hot” will be split into
{“Sun”,”bright”,”today”, “hot”}. Tokenization will also remove duplicate letters in a
word. Ex: “Happpyyy” will be converted to “Happy”.
Data will be classified based on a three point scale:
● Positive
● Neutral
● Negative
A sorting algorithm is used to classify the data.
Finding the sentiment of the tweet:

### Positive:
Tweets containing the following emoticons:
:-) :) :o) :] :3 :c) XD :D :P
Tweets containing the following hashtags:
#great #best #happy #lol #feelingblessed #blessed #success #amazing #bestfeeling
#wonderful #thankfulfor #TGIF #holiday #vacation #music #fun #dance #memories

### Neutral:
Tweets containing the follow emoticons:
:| {u+1F636} {u+1F644}
Tweets containing the following hashtags:
#job #news #listeningto #ok #facts #hiring #currentaffairs #world

### Negative:
Tweets containing the following emoticons:
:-( :( :o( :c( DX D:
Tweets containing the following hashtags:
#bored #boredatwork #sad #worst #wrong #angry #messedup #fail #ihate
#nevertrust #worstfeeling

For the analysis segment of the tweets we acquire, we have used the textblob library. This is
an in-built library in Python that is used for text processing. It has several applications apart
from sentiment analysis, too. These include several tasks of Natural Language Processing.
These tasks range from translation and classification to noun phrase extraction.
The output procured is in the form of bar charts, pie charts and graph charts. The first bar
chart would indicate how many tweets belong to each category i.e. Positive, Negative or
Neutral that relate to that particular #. For example, Climate. Another bar chart is presented
that displays the trending hastags related to the chosen topic. And finally, there is a pie
chart that displays how much percentage of the tweets are positive, how much are negative
and how much are neutral.
