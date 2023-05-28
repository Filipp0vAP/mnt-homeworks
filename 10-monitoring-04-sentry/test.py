#!/usr/bin/env python3

import sentry_sdk
import logging
import random
import time
logging.getLogger().setLevel(logging.INFO)

sentry_sdk.init(
    dsn="",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    environment="dev",
    release="1.0.2"
)


while True:

    number = random.randrange(0, 4)

    if number == 0:
        logging.info('Hello there!!')
    elif number == 1:
        logging.warning('Hmmm....something strange')
    elif number == 2:
        logging.error('OH NO!!!!!!')
    elif number == 3:
        logging.exception(Exception('this is exception'), exc_info=False)

    time.sleep(5)