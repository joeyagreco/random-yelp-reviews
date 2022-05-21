from server.service.YelpReviewService import YelpReviewService

if __name__ == "__main__":
    # yac = YelpApiClient()
    # businesses = yac.getBusinessesBySearch("food", "wisconsin")
    # reviews = yac.getReviewsByBusinessId("p7OwdW-3kzwymVPUEqidiw")
    # zips = DataReader.getDataListFromFile(
    #     "C:\\Users\\14143\\PycharmProjects\\random-yelp-reviews\\server\\data\\zip_codes.txt")
    yrs = YelpReviewService()
    review, business = yrs.getRandomReviewAndBusiness()
    print()
