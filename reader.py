import os
from configparser import ConfigParser
path = 'cinfig.ini'
parser = ConfigParser()
parser.read(path)

print(parser.sections())
print(parser['AUTH']['username'])
print(parser['AUTH']['password'])
