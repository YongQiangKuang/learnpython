# coding=utf-8
# -*- coding: utf-8 -*-
import sys

import orm, asyncio
from models import User, Blog, Comment

'''/*
@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='root', db='python_1')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
    
print("%015d" % 5)
*/
'''
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

logging.info('info')
logging.error('error')
logging.debug('debug')
logging.warning('warn')
