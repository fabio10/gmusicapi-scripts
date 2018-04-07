#!/usr/bin/env python3
# coding=utf-8

import logging
import sys

from gmusicapi import Mobileclient

QUIET = 25
logging.addLevelName(25, "QUIET")

logger = logging.getLogger('gmusicapi')
sh = logging.StreamHandler()
logger.addHandler(sh)

api = Mobileclient()
logged_in = api.login('fabiomariotti@gmail.com', '', Mobileclient.FROM_MAC_ADDRESS)
# logged_in is True if login was successful
if logged_in:
  logger.info("\nAll done!")
