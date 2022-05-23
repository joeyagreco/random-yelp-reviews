from datetime import datetime
from typing import List, Optional

import requests

from server.model.Business import Business
from server.model.Category import Category
from server.model.Location import Location
from server.model.Review import Review
from server.model.User import User
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader


class YelpApiClient:
    """
    https://www.yelp.com/developers/documentation/v3
    """

    def __init__(self):
        self.__LOGGER = CustomLogger.getLogger()
        self.__BASE_URL = EnvironmentReader.get("YELP_API_BASE_URL")
        self.__SEARCH_ROUTE = EnvironmentReader.get("YELP_API_SEARCH_ROUTE")
        self.__REVIEWS_ROUTE = EnvironmentReader.get("YELP_API_REVIEWS_ROUTE")
        self.__API_KEY = EnvironmentReader.get("YELP_API_API_KEY")

    def __objectifyBusinessList(self, businessDictList: List[dict]) -> List[Business]:
        businessObjList = list()
        for businessDict in businessDictList:
            businessObjList.append(self.__objectifyBusiness(businessDict))
        return businessObjList

    def __objectifyBusiness(self, businessDict: dict) -> Optional[Business]:
        businessObj = None
        if businessDict is not None:
            businessObj = Business(id=businessDict["id"],
                                   name=businessDict["name"],
                                   imageUrl=businessDict["image_url"],
                                   url=businessDict["url"],
                                   reviewCount=businessDict["review_count"],
                                   categories=self.__objectifyCategoriesList(businessDict["categories"]),
                                   rating=businessDict["rating"],
                                   location=self.__objectifyLocation(businessDict["location"]),
                                   phone=businessDict["phone"])
        return businessObj

    def __objectifyLocation(self, locationDict: dict) -> Optional[Location]:
        locationObj = None
        if locationDict is not None:
            locationObj = Location(address1=locationDict["address1"],
                                   address2=locationDict["address2"],
                                   address3=locationDict["address3"],
                                   city=locationDict["city"],
                                   zipCode=locationDict["zip_code"],
                                   country=locationDict["country"],
                                   state=locationDict["state"],
                                   displayAddress=locationDict["display_address"])
        return locationObj

    def __objectifyCategoriesList(self, categoriesDictList: List[dict]) -> List[Category]:
        categoriesList = list()
        for categoriesDict in categoriesDictList:
            categoriesList.append(Category(alias=categoriesDict["alias"],
                                           title=categoriesDict["title"]))
        return categoriesList

    def __objectifyUser(self, userDict: dict) -> Optional[User]:
        userObj = None
        if userDict is not None:
            userObj = User(id=userDict["id"],
                           profileUrl=userDict["profile_url"],
                           imageUrl=userDict["image_url"],
                           name=userDict["name"])
        return userObj

    def __objectifyReview(self, reviewDict: dict) -> Optional[Review]:
        reviewObj = None
        if reviewDict is not None:
            reviewObj = Review(id=reviewDict["id"],
                               url=reviewDict["url"],
                               text=reviewDict["text"],
                               rating=reviewDict["rating"],
                               timeCreated=datetime.strptime(reviewDict["time_created"], "%Y-%m-%d %H:%M:%S"),
                               user=self.__objectifyUser(reviewDict["user"]))
        return reviewObj

    def __objectifyReviewList(self, reviewDictList: List[dict]) -> List[Review]:
        reviewList = list()
        for reviewDict in reviewDictList:
            reviewList.append(self.__objectifyReview(reviewDict))
        return reviewList

    def getBusinessesBySearch(self, term: str, location: str, **kwargs) -> List[Business]:
        # https://www.yelp.com/developers/documentation/v3/business_search
        limit = kwargs.pop("limit", 1)
        offset = kwargs.pop("offset", 0)
        businesses = list()
        try:
            url = f"{self.__BASE_URL}{self.__SEARCH_ROUTE}?term={term}&location={location}&limit={limit}&offset={offset}"
            headers = {
                'Authorization': 'Bearer %s' % self.__API_KEY,
            }
            response = requests.get(url, headers=headers).json()
            businesses = self.__objectifyBusinessList(response["businesses"])
        except Exception as e:
            self.__LOGGER.error(e)
        return businesses

    def getReviewsByBusinessId(self, businessId: str) -> List[Review]:
        # https://www.yelp.com/developers/documentation/v3/business_reviews
        reviews = list()
        try:
            url = f"{self.__BASE_URL}/{businessId}{self.__REVIEWS_ROUTE}"
            headers = {
                'Authorization': 'Bearer %s' % self.__API_KEY,
            }
            response = requests.get(url, headers=headers).json()
            reviews = self.__objectifyReviewList(response["reviews"])
        except Exception as e:
            self.__LOGGER.error(e)
        return reviews
