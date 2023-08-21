import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29877145"))
    API_HASH = os.environ.get("API_HASH", "85c320b142b7482589fff61da6370b07")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5825009313:AAHVCMjJ2vgqhpsRbPm2VzKDNfK9Lc1f5i8)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIEBu1lvpo3gzibKjrehHT7LGjoiBdkkw7iNd8YffdwAecC9IkGV2RNTeHDj71UEPHm8Vat09sZW0HGwqPUjUWBfmA0Pf4tIWkRcGjCUSsmQJlYOKpH4GPYWs_34M3_BDhLOz6YRPBs6Rain1juBJEJ8JWAvTCR1qPtLU6kjSBnWkG8aso5ha9JrOjSB36VK_2MXtwO5GlIjj4e_85W9J03rcXN_r1Z4BvoPJ5t5cIudYFnXXT4_5mk4LAwn_zUItbMkn_tVoXI8R11yaXIZHBbAoeZFni5qanMf2fUaNl9nKqZQyhHMDnzbdPvKaFJm0MaTuhhYHdNaJ4MBkyeH6h_QkJw=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", Biharisongmusic_bot"")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", 5999149323"")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
