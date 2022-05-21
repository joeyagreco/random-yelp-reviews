from tweepy.models import Status

from server.twitter.TwitterApi import TwitterApi


class TwitterTweeter:

    @classmethod
    def createTweet(cls, text: str, **kwargs) -> Status:
        mediaUrls = kwargs.pop("mediaUrls", list())
        api = TwitterApi.getApi()
        medias = list()
        for url in mediaUrls:
            medias.append(api.media_upload(url))
        return api.update_status(status=text, media_ids=[m.media_id for m in medias])
