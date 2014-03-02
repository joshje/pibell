#!/usr/bin/env python
import sys
from twython import Twython
import config

api = Twython(config.api_key,config.api_secret,config.access_key,config.access_secret) 

api.update_status('I\'m alive!')
