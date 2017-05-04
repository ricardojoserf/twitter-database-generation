import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import csv
from optparse import OptionParser
import config
import argparse


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-q', '--query', required=True, action='store', help='Query')
  parser.add_argument('-l', '--limit', required=True, action='store', help='Max. number of tweets')
  parser.add_argument('-g', '--geocode', required=True, action='store', help='Geocode. Ex: "40.432,-3.708,10km"')
  parser.add_argument('-o', '--outputFile', required=True, action='store', help='Output file (csv)')
  my_args = parser.parse_args()
  return my_args


def get_tweets(query, count, geocode):

    consumer_key=config.consumer_key
    consumer_secret=config.consumer_secret
    access_token=config.access_token
    access_token_secret=config.access_token_secret

    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        tweets = []

        try:
            for tweet in api.search(q = query,count = count,geocode=geocode):

                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text
                parsed_tweet['time'] = tweet.created_at
                parsed_tweet['rts'] = tweet.retweet_count
                if tweet.place is not None:
                    parsed_tweet['place'] = tweet.place.full_name
                else:
                    parsed_tweet['place'] = "NaN"
                parsed_tweet['user'] = tweet.user.name
                if tweet.coordinates is not None:
                    parsed_tweet['lon'] = tweet.coordinates['coordinates'][0]
                    parsed_tweet['lat'] = tweet.coordinates['coordinates'][1]
                else:
                    parsed_tweet['lon'] = "NaN"
                    parsed_tweet['lat'] = "NaN"

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except ValueError:
            print("Error")

    except ValueError:
        print("Error")

def busqueda(query, count, geocode,csvname):
    print("Topic:        {}".format(query))
    print("Coordinates:  {}".format(geocode))
    tweets = get_tweets(query = query, count = count, geocode = geocode)
    csvFile = open(csvname, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["time","text","user","rts","place","lon","lat"])
    for tweet in tweets:
        csvWriter.writerow([tweet.get("time"),
                            tweet.get("text").encode("utf-8"),
                            tweet.get("user").encode("utf-8"),
                            tweet.get("rts"),
                            tweet.get("place"),
                            tweet.get("lon"),
                            tweet.get("lat")
                            ])
    print(csvname+" generated.")


def main():
    args = get_args()
    busqueda(args.query,args.limit,args.geocode,args.outputFile)


if __name__ == "__main__":
    main()
