import os
import time

from server.exception.BusinessSearchTimeoutError import BusinessSearchTimeoutError
from server.exception.InsufficientNumberOfReviewsError import InsufficientNumberOfReviewsError
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
                tweetText = f'RATING: {self.__STAR_EMOJI * review.rating}\n\n"{review.text}"\n\nBY: {review.user.name}\n\nBUSINESS: {business.name}\n\n{review.url}\n\nLOCATION: {business.location.city} {business.location.state}, {business.location.country}'
                status = TwitterTweeter.createTweet(tweetText, mediaUrls=mediaUrls)
                self.__LOGGER.info(f"TWEETED SUCCESSFULLY: {EnvironmentReader.get('TWEET_BASE_URL')}{status.id}")
            except BusinessSearchTimeoutError as e:
                self.__LOGGER.error(e)
            except InsufficientNumberOfReviewsError as e:
                self.__LOGGER.error(e)
            self.__LOGGER.info(f"SLEEPING FOR {minutesInBetweenTweets} minutes...")
            time.sleep(minutesInBetweenTweets * self.__SECONDS_IN_A_MINUTE)
