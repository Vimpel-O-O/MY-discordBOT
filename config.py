def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

POST_ID = 761579822697676832

ROLES = {
    '💪': 761562204943679499,  # cs:go
    '🦾': 761562313177432085,  # valorant
    '⚽': 761562385462067200,  # rocket leagua
    '🛸': 761562568400830484,  # gta v
    '🔪': 761562638483324988,  # among us
    '🌱': 761562821439782912,  # minecraft
    '🔫': 761562908541845514,  # pubg
    '🔨': 761563042059780106,  # fortnite
    '🎼': 761563444313980978,  # osu!
    '💻': 761563530943135746,  # watch dogs
    '🏹': 761576654589919252,  # warcraft
    '📱': 761576657924390922,  # standoff
}

EXCROLES = ()

MAX_ROLES_PER_USER = 20


