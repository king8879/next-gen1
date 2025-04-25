import os

API_ID = os.environ.get("API_ID", "18579024")

API_HASH = os.environ.get("API_HASH", "124981da628d86e21ee492da77cd4037")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7917784797:AAHDtxINKcNkmtwXs_3l3J1TsPufjdgYZPE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 574224129))

LOG = -1002512609919,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[574224129]
    for x in (os.environ.get("ADMINS", "574224129").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
