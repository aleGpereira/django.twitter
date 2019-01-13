from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from twitter import Api
from twitter_stuff.settings import TWITTER_SETTINGS

from .models import Tweet
from .serializers import TweetSerializer
from django.shortcuts import get_object_or_404


class TwitterApi(object):
    """Singleton class that connects to twitter account."""

    api = None
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(TwitterApi, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self.api is None:
            self.api = Api(*TWITTER_SETTINGS)

    def _get_tweet_user_name(self, tweet):
        """Return the screen name of tweet author."""
        return tweet.user.screen_name

    def get_home_tweets(self):
        """Return a dictionary of all the tweets with their users."""
        home_tweets = self.api.GetHomeTimeline()
        tweets = [(
            tweet.id,
            self._get_tweet_user_name(tweet),
            unicode(tweet.text)) for tweet in home_tweets]
        return tweets


class UpdateTweets(APIView):
    """Fetch tweets and stores new ones."""

    def get(self, request, format=None):
        """Return a list of all users."""
        api = TwitterApi()
        try:
            tweets = api.get_home_tweets()
        except Exception as e:
            tweets = None
        if tweets:
            # Fetch all new tweets
            for tweet in tweets:
                tweet_id, author, text = tweet
                try:
                    tweet_obj = Tweet.objects.get(pk=tweet_id)
                except Tweet.DoesNotExist as e:
                    tweet_obj = None
                if tweet_obj is None:
                    tweet_obj = Tweet.objects.create(id=tweet_id, author=author, text=text)
                del tweet_obj

        all_tweets = Tweet.objects.all()
        return Response({'total_tweets': len(all_tweets)})


class TweetList(generics.ListCreateAPIView):
    """Fetch all the latest tweets return all the list of tweets."""

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_objects(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj
