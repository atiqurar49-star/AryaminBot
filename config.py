import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN=os.getenv('BOT_TOKEN')
CHAT_ID=os.getenv('CHAT_ID')
FOLLOWER_LIMIT=int(os.getenv('FOLLOWER_LIMIT','100'))
CHECK_INTERVAL=int(os.getenv('CHECK_INTERVAL','30'))
