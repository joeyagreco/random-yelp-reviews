from typing import List, Optional

import requests

from server.model.Business import Business
from server.model.Category import Category
from server.model.Location import Location
from server.util.EnvironmentReader import EnvironmentReader


class YelpApiClient:
    """
    https://www.yelp.com/developers/documentation/v3
    """

    def __init__(self):
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

    def getBusinessesBySearch(self, term: str, location: str, **kwargs) -> List[Business]:
        # https://www.yelp.com/developers/documentation/v3/business_search
        limit = kwargs.pop("limit", 1)
        offset = kwargs.pop("offset", 0)

        url = f"{self.__BASE_URL}{self.__SEARCH_ROUTE}?term={term}&location={location}&limit={limit}&offset={offset}"
        headers = {
            'Authorization': 'Bearer %s' % self.__API_KEY,
        }
        response = requests.get(url, headers=headers).json()
        return self.__objectifyBusinessList(response["businesses"])
