from server.service.YelpReviewService import YelpReviewService
from server.twitter.TwitterTweeter import TwitterTweeter


class BotRunner:

    def __init__(self):
        self.__STAR_EMOJI = "*"

    def run(self):
        yelpReviewService = YelpReviewService()
        review, business = yelpReviewService.getRandomReviewAndBusiness()
        tweetText = f'RATING: {self.__STAR_EMOJI * review.rating}\n\n"{review.text}"\n\nBY: {review.user.name}\n\n{review.url}'
        status = TwitterTweeter.createTweet(tweetText)
