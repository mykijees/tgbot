from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1311253220  # my telegram ID
    OWNER_USERNAME = "chatm3here"  # my telegram username
    API_KEY = "1315893535:AAFlMQFvb_UFCXnPHdqN1Iu9FTczZ3Fu-EU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://ciribot:ciribot@54.254.204.75:5432/ciridata'  # sample db credentials
    MESSAGE_DUMP = '-440523709' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
