import os
import time

from server.exception.BusinessSearchTimeoutError import BusinessSearchTimeoutError
from server.exception.InsufficientNumberOfReviewsError import InsufficientNumberOfReviewsError
from server.model.Business import Business
from server.model.Review import Review
from server.service.YelpReviewService import YelpReviewService
from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader
from server.util.ImageDownloader import ImageDownloader


class BotRunner:

    def __init__(self):
        self.__LOGGER = CustomLogger.getLogger()
        self.__STAR_EMOJI = "\u2B50"
        self.__TMP_DIRECTORY_NAME = "tmp"
        self.__TMP_USER_PROFILE_PIC_FILE_NAME = "tmp_user_profile.jpg"
        self.__TMP_BUSINESS_PIC_FILE_NAME = "tmp_business_profile.jpg"
        self.__SECONDS_IN_A_MINUTE = 60
        self.__MAX_TWEET_CHARACTERS = 270
        self.__SHORTENED_URL_LENGTH = 23  # https://help.twitter.com/en/using-twitter/how-to-tweet-a-link#:~:text=Post%20the%20Tweet.,-Step%201&text=Step%201-,Type%20or%20paste%20the%20URL,Tweet%20box%20on%20twitter.com.&text=A%20URL%20of%20any%20length,character%20count%20will%20reflect%20this.

    def run(self, minutesInBetweenTweets: int):
        while True:
            try:
                yelpReviewService = YelpReviewService()
                review, business = yelpReviewService.getRandomReviewAndBusiness()
                tmpFolderDirectory = os.path.abspath(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"../{self.__TMP_DIRECTORY_NAME}"))
                # create the tmp directory if it doesn't already exist
                if not os.path.exists(tmpFolderDirectory):
                    os.makedirs(tmpFolderDirectory)
                # delete old images from tmp folder if there are any
                fullImagePath = os.path.join(tmpFolderDirectory, self.__TMP_USER_PROFILE_PIC_FILE_NAME)
                if os.path.exists(fullImagePath):
                    os.remove(fullImagePath)
                fullImagePath = os.path.join(tmpFolderDirectory, self.__TMP_BUSINESS_PIC_FILE_NAME)
                if os.path.exists(fullImagePath):
                    os.remove(fullImagePath)
                # will hold images we will send with tweet
                mediaUrls = list()
                # download user profile image locally to tmp folder
                if review.user.imageUrl:
                    ImageDownloader.downloadImageByUrl(review.user.imageUrl, self.__TMP_USER_PROFILE_PIC_FILE_NAME,
                                                       tmpFolderDirectory)
                    mediaUrls.append(os.path.join(tmpFolderDirectory, self.__TMP_USER_PROFILE_PIC_FILE_NAME))
                # download business profile image locally to tmp folder
                if business.imageUrl:
                    ImageDownloader.downloadImageByUrl(business.imageUrl, self.__TMP_BUSINESS_PIC_FILE_NAME,
                                                       tmpFolderDirectory)
                    mediaUrls.append(os.path.join(tmpFolderDirectory, self.__TMP_BUSINESS_PIC_FILE_NAME))
                status = TwitterTweeter.createTweet(self.__buildTweet(review, business), mediaUrls=mediaUrls)
                self.__LOGGER.info(f"TWEETED SUCCESSFULLY: {EnvironmentReader.get('TWEET_BASE_URL')}{status.id}")
            except BusinessSearchTimeoutError as e:
                self.__LOGGER.error(e)
            except InsufficientNumberOfReviewsError as e:
                self.__LOGGER.error(e)
            self.__LOGGER.info(f"SLEEPING FOR {minutesInBetweenTweets} minutes...")
            time.sleep(minutesInBetweenTweets * self.__SECONDS_IN_A_MINUTE)

    def __buildTweet(self, review: Review, business: Business) -> str:
        ratingStr = f"RATING: {self.__STAR_EMOJI * review.rating}\n\n"
        reviewStr = f'"{review.text}"\n\n'
        byStr = f"- {review.user.name}\n\n"
        businessStr = f"{business.name}\n\n"
        locationStr = f"{business.location.city}, {business.location.state}\n\n"
        urlStr = review.url
        fullTweet = f"{ratingStr}{reviewStr}{byStr}{businessStr}{locationStr}{urlStr}"
        remainingCharacters = self.__MAX_TWEET_CHARACTERS \
                              - (len(ratingStr)
                                 + len(reviewStr)
                                 + len(byStr)
                                 + len(businessStr)
                                 + len(locationStr)
                                 + self.__SHORTENED_URL_LENGTH)
        if remainingCharacters < 0:
            # shorten review to get tweet to allowed number of characters
            # we know that reviews will always end with "...", so remove and re-add that
            reviewStr = f'"{review.text[:(remainingCharacters - 3)]}..."\n\n'
            fullTweet = f"{ratingStr}{reviewStr}{byStr}{businessStr}{locationStr}{urlStr}"
        return fullTweet
