from server.service.BotRunner import BotRunner
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader

if __name__ == "__main__":
    MINUTES_IN_BETWEEN_TWEETS = EnvironmentReader.get("MINUTES_IN_BETWEEN_TWEETS", int)
    LOGGER = CustomLogger.getLogger()
    LOGGER.info("STARTING BOT...")
    botRunner = BotRunner()
    botRunner.run(MINUTES_IN_BETWEEN_TWEETS)
