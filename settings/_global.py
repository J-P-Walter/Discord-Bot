import os

from regex import P

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

#Reddit Config
REDDIT_ENABLED_SUBREDDITS = [
    '2healthbars',
    'BirdsBeingDicks',
    'Catswhoyell',
    'DesirePath'
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'THE_PACK',
]