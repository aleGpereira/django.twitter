import mock

from django.test import TestCase
from tweets.models import Tweet


class TweetTestCase(TestCase):
    """Simple testing of Tweet model."""

    def setUp(self):
        self.tweet = Tweet.objects.create(
            id=123456789,
            author='test_author',
            text='Test tweet'
        )

    def test_tweet_creation(self):
        tweet = Tweet.objects.get(id=self.tweet.id)
        self.assertEqual(tweet.author, 'test_author')
        self.assertEqual(tweet.text, 'Test tweet')


class UpdateViewTestCase(TestCase):
    """Test case to test /api/v1/tweets/update."""

    def setUp(self):
        self.fake_tweets = [(
            i,
            u'user{}'.format(i),
            u'User{} tweet text'.format(i)) for i in range(3)
        ]

    def test_store_new_tweets(self):
        stored_tweets = Tweet.objects.all()
        self.assertEqual(len(stored_tweets), 0)

        with mock.patch('tweets.views.TwitterApi.get_home_tweets') as fake_home:
            conf = {'return_value': self.fake_tweets}
            fake_home.configure_mock(**conf)
            response = self.client.get('/api/v1/tweets/update')
            self.assertEqual(response.status_code, 200)
            fake_home.assert_called_once_with()

        # We should have 3 more items in the DB
        stored_tweets = Tweet.objects.all()
        self.assertEqual(len(stored_tweets), 3)
        for index, tweet in enumerate(stored_tweets):
            tweet_id = tweet.id
            author = tweet.author
            text = tweet.text
            self.assertEqual(tweet_id, index)
            self.assertEqual(author, u'user{}'.format(index))
            self.assertEqual(text, u'User{} tweet text'.format(index))

    def test_store_only_new_tweets(self):
        stored_tweets = Tweet.objects.all()
        self.assertEqual(len(stored_tweets), 0)

        # We manually store a tweet
        tweet_id, author, text = self.fake_tweets[0]
        Tweet.objects.create(id=tweet_id, author=author, text=text)

        with mock.patch('tweets.views.TwitterApi.get_home_tweets') as fake_home:
            conf = {'return_value': self.fake_tweets}
            fake_home.configure_mock(**conf)
            # In this context first tweet is already stored
            stored_tweets = Tweet.objects.all()
            self.assertEqual(len(stored_tweets), 1)
            response = self.client.get('/api/v1/tweets/update')
            self.assertEqual(response.status_code, 200)
            fake_home.assert_called_once_with()

        # We should have 3 more items in the DB
        stored_tweets = Tweet.objects.all()
        self.assertEqual(len(stored_tweets), 3)
        for index, tweet in enumerate(stored_tweets):
            tweet_id = tweet.id
            author = tweet.author
            text = tweet.text
            self.assertEqual(tweet_id, index)
            self.assertEqual(author, u'user{}'.format(index))
            self.assertEqual(text, u'User{} tweet text'.format(index))

    @mock.patch('tweets.views.TwitterApi.get_home_tweets')
    def test_serializer(self, fake_home):
            conf = {'return_value': self.fake_tweets}
            fake_home.configure_mock(**conf)
            response = self.client.get('/api/v1/tweets/update')
            data = response.data
            self.assertEqual(response.status_code, 200)
            self.assertEqual('total_tweets' in data, True)
            self.assertEqual(data.get('total_tweets'), 3)
            fake_home.assert_called_once_with()


class TweetListViewTestCase(TestCase):
    """Test case to test /api/v1/tweets."""

    def setUp(self):
        self.fake_tweets = [(
            i,
            u'user{}'.format(i),
            u'User{} tweet text'.format(i)) for i in range(3)
        ]
        for tweet_id, author, text in self.fake_tweets:
            Tweet.objects.create(id=tweet_id, author=author, text=text)
        stored_tweets = Tweet.objects.all()
        self.assertEqual(len(stored_tweets), 3)

    def test_serializer(self):
        response = self.client.get('/api/v1/tweets/')
        self.assertEqual(response.status_code, 200)
        data = response.data
        for index, item in enumerate(data):
            self.assertEqual(item.get('id'), index)
            self.assertEqual(item.get('author'), u'user{}'.format(index))
            self.assertEqual(item.get('text'), u'User{} tweet text'.format(index))
