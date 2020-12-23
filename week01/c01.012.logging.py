#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(filename=r'd:/log/test.log',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s.%(msecs)d %(levelname)s  %(name)s  [line: %(lineno)d] %(message)s')

logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')

