# Random Yelp Reviews

This uses the [Yelp API](https://www.yelp.com/developers/documentation/v3/get_started) to find random reviews from
random businesses and [tweets them out](https://twitter.com/RandomYelp).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Setup

The following environment variables must be defined before running the script:

```dotenv
# Yelp API

YELP_API_BASE_URL=https://api.yelp.com/v3/businesses
YELP_API_API_KEY=...
YELP_API_SEARCH_ROUTE=/search
YELP_API_REVIEWS_ROUTE=/reviews

# Twitter

TWITTER_API_KEY=...
TWITTER_API_KEY_SECRET=...
TWITTER_BEARER_TOKEN=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...
TWEET_BASE_URL=https://twitter.com/{account_@_name}/status/

# GENERAL

MINUTES_IN_BETWEEN_TWEETS=60
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credit

Zip code data provided by [simplemaps.com](https://simplemaps.com/data/us-zips)
