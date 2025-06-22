from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv()
find_dotenv()

ADMINS = list(map(int, getenv('ADMINS').split(',')))

FOREMANS = [
    
]