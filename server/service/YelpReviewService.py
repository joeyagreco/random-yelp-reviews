import os
import random
from typing import Tuple

from server.client.YelpApiClient import YelpApiClient
from server.enum.YelpSearchTerm import YelpSearchTerm
from server.enum.YelpSortByTerm import YelpSortByTerm
from server.exception.BusinessSearchTimeoutError import BusinessSearchTimeoutError
from server.exception.InsufficientNumberOfReviewsError import InsufficientNumberOfReviewsError
from server.model.Business import Business
from server.model.Review import Review
from server.util.DataReader import DataReader


class YelpReviewService:

    def __init__(self):
        self.__ZIP_CODES_FULL_PATH = os.path.abspath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"../data/zip_codes.txt"))
        self.__YELP_BUSINESS_REQUEST_LIMIT = 50
        self.__MAX_OFFSET = 10
        self.__MINIMUM_REVIEWS_NEEDED = 3
        self.__SELECT_RANDOM_BUSINESS_MAX_RETRIES = 50
        self.__BUSINESS_SEARCH_MAX_RETRIES = 5

        self.__yelpApiClient = YelpApiClient()

    def getRandomReviewAndBusiness(self) -> Tuple[Review, Business]:
        businessList = list()
        businessSearchRetriesRemaining = self.__BUSINESS_SEARCH_MAX_RETRIES
        while len(businessList) == 0:
            # first, find a random business
            # get a random search term
            searchTerm = random.choice(YelpSearchTerm.list()).name
            # get a random zip code
            zipCode = random.choice(DataReader.getDataListFromFile(self.__ZIP_CODES_FULL_PATH))
            # sort by businesses with the most reviews
            sortBy = YelpSortByTerm.REVIEW_COUNT
            # limit result count
            limit = self.__YELP_BUSINESS_REQUEST_LIMIT
            # set offset of results
            offset = random.randint(1, self.__MAX_OFFSET + 1)
            businessList = self.__yelpApiClient.getBusinessesBySearch(searchTerm, zipCode, sortBy=sortBy, limit=limit,
                                                                      offset=offset)
            if len(businessList) > 0:
                break
            businessSearchRetriesRemaining -= 1
            if businessSearchRetriesRemaining == 0:
                raise BusinessSearchTimeoutError("COULD NOT FIND BUSINESSES!")
        business = None
        selectRandomBusinessRetiresRemaining = self.__SELECT_RANDOM_BUSINESS_MAX_RETRIES
        while business is None:
            business = random.choice(businessList)
            if business.reviewCount >= self.__MINIMUM_REVIEWS_NEEDED:
                break
            selectRandomBusinessRetiresRemaining -= 1
            if selectRandomBusinessRetiresRemaining == 0:
                raise InsufficientNumberOfReviewsError("SELECTED BUSINESS DOES NOT HAVE ")
        # get a review from this business
        reviewList = self.__yelpApiClient.getReviewsByBusinessId(business.id)
        return random.choice(reviewList), business
