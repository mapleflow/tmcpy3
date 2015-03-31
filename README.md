tmcpy
=======================

淘宝平台消息服务客户端 for Python

Usage:
```python
import logging

from tmcpy import TmcClient

logging.basicConfig(level=logging.DEBUG)


tmc = TmcClient(
    'ws://mc.api.tbsandbox.com/',
    'appkey',
    'appsecret',
    'default',
    query_message_interval=50
)


def print1():
    print 'on_open'


tmc.on("on_open", print1)
try:
    ioloop.IOLoop.instance().start()
except KeyboardInterrupt:
    pass
finally:
    tmc.close()
```
