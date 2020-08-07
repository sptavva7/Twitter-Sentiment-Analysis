import tweepy
import csv
auth = tweepy.OAuthHandler( "InffwZlMjZu7wiAoMo5VTYT94" ,
"6pAqdEXNKK3JC27qtHvA2f28v5XuziHgnmBs6MuCELbnr3t5tZ" )
auth.set_access_token("2357974296-8JAOlPqiDpHVpAawqasX6mm3c1m6oNTX7DyBqkU",
"IzoyJDQX1PApuMlEBEq5piGXEZxepEWX7mdMxOVa4VakI" )
api = tweepy.API(auth, wait_on_rate_limit=True)
File = open('india.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#india -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('world.csv', 'w')
writer = csv.writer(File)
print("Started")

for tweet in tweepy.Cursor(api.search, q="#world -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('UN.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#UN -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('UNESCO.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#UNESCO -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('UNICEF.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#UNICEF -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('WHO.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#WHO -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('BLOGGING.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#BLOGGING -filter:retweets",count=50
,lang="en", since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File = open('lifestyle.csv', 'w')
writer = csv.writer(File)
print("Started")
for tweet in tweepy.Cursor(api.search, q="#lifestyle -filter:retweets",count=50 ,lang="en",
since="2019-10-12", result_type="popular").items(500):
 print(tweet.created_at,tweet.text)
 writer.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.id])
print("done")
File.close()
