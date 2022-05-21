from server.client.YelpApiClient import YelpApiClient

if __name__ == "__main__":
    yac = YelpApiClient()
    businesses = yac.getBusinessesBySearch("food", "wisconsin")
    print()