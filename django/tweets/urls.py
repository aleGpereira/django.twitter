from django.conf.urls import url
from tweets.views import TweetList
from tweets.views import UpdateTweets


urlpatterns = [
    url(r'^tweets/?$', TweetList.as_view(), name='tweets'),
    url(r'^tweets/update$', UpdateTweets.as_view(), name='update_tweets'),
]
