#!/usr/bin/env python
from twython import Twython
import config

api = Twython(config.api_key,config.api_secret,config.access_key,config.access_secret)


status = ''
if (config.mentions): status += ' '.join(config.mentions) + ' '
status += 'hey, someone just rang your doorbell'

api.update_status(status=status)
