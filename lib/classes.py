import redis, socket, os

RED = '\033[91m'
YELLOW = '\033[93m'
GREY = '\033[90m'
BLACK = '\033[0m'
BOLD = '\033[1m'

try:
    from .config import config as co
except:
    from config import config as co

r = redis.Redis(host=co['host'], port=co['port'], unix_socket_path=co['unix_socket_path'], db=co['db'])

def clear():
    """
    clear the window
    """
    try:
        os.system('clear')
    except:
        os.system('cls')

class PersonalError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
