from server.client.YelpApiClient import YelpApiClient

if __name__ == "__main__":
    yac = YelpApiClient()
    # businesses = yac.getBusinessesBySearch("food", "wisconsin")
    reviews = yac.getReviewsByBusinessId("p7OwdW-3kzwymVPUEqidiw")
    print()
