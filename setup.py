# coding: utf-8
from setuptools import setup, find_packages

version = '0.3.4'

setup(
    name='tmcpy',
    version=version,
    description="淘宝平台消息服务客户端 for Python",
    long_description="""
tmcpy
=======================

淘宝平台消息服务python版本

Usage:
```python
import logging

from tmcpy import TmcClient

logging.basicConfig(level=logging.DEBUG)

tmc = TmcClient('ws://mc.api.tbsandbox.com/', 'appkey', 'appsecret', 'default',
    query_message_interval=50)


def print1():
    print 'on_open'


tmc.on("open", print1)
try:
    ioloop.IOLoop.instance().start()
except KeyboardInterrupt:
    pass
finally:
    tmc.close()
```

""",
    keywords='taobao tmc python',
    author='baocaixiong,messense',
    author_email='baocaixiong@gmail.com,messense@icloud.com',
    url='https://github.com/messense/tmcpy',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'tornado>=4.1',
        'six>=1.9.0',
        'simplejson>=3.6.5'
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector'
)
