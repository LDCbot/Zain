import os
import asyncio
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

__version__ = "v0.1"

if os.path.exists(".env"):
    load_dotenv(".env")
    

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "20504580"))
API_HASH = os.getenv("API_HASH", "e6fee2a8a86d209e96ec08dcd7f9a988")
SESSION = os.getenv("SESSION", "AQCXJ4wocgSkRhGtgIWRIptCeTx_4swU7Q8De0WFzzRwTA4KnYEgW4SQiwRId4xScCSBvwbSIgbAQDtaQC8iE63MalQCnBnktI0F4eE574VjJY44vAZcJzdxhvWU1WwYw8OSL5KBTVXtbfwVFkAlvpPGB6hhRZmQgbr60iwe5ehtjDz1X7jad6038-EiH4miTMFolh-z9KBGc6_0wCv7t9RHKfikdRcaYwCcz9wnzx_kSrwfqeCCOe0P9CoWZqzt_Cb4GKHE7ybniZWIYan9VwlLX6ABsyTrdzX_FhVvgqjv76YCjqKAH_ul8s9hBwMpp8j8H-lJiHMy1taXnkHoJSL9AAAAAWH8guEA")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
ALIVE_PIC = os.getenv("ALIVE_PIC", "https://te.legra.ph/file/e1c0e0a907e5d72229f53.jpg")
ALIVE_MSG = os.getenv("ALIVE_MSG", "https://te.legra.ph/file/e1c0e0a907e5d72229f53.jpg")
PING_MSG = os.getenv("PING_MSG", "https://te.legra.ph/file/e1c0e0a907e5d72229f53.jpg")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)
# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Modules"))
call_py = PyTgCalls(bot)

# Terms
# Privacy
# Security

hl = HNDLR[0]
start_time = time.time()

