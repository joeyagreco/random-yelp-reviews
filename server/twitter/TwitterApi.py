import tweepy
from tweepy import API, OAuthHandler

from server.util.EnvironmentReader import EnvironmentReader


class TwitterApi:
    __API_KEY = EnvironmentReader.get("TWITTER_API_KEY")
    __API_KEY_SECRET = EnvironmentReader.get("TWITTER_API_KEY_SECRET")
    __BEARER_TOKEN = EnvironmentReader.get("TWITTER_BEARER_TOKEN")
    __ACCESS_TOKEN = EnvironmentReader.get("TWITTER_ACCESS_TOKEN")
    __ACCESS_TOKEN_SECRET = EnvironmentReader.get("TWITTER_ACCESS_TOKEN_SECRET")

    @classmethod
    def __getOAuthHandler(cls) -> OAuthHandler:
        handler = tweepy.OAuthHandler(cls.__API_KEY, cls.__API_KEY_SECRET)
        handler.set_access_token(cls.__ACCESS_TOKEN, cls.__ACCESS_TOKEN_SECRET)
        return handler

    @classmethod
    def getApi(cls) -> API:
        return tweepy.API(cls.__getOAuthHandler())
