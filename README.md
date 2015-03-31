tmcpy
=======================

淘宝平台消息服务客户端 for Python

## 安装

推荐使用 pip 进行安装：

    pip install tmcpy

升级版本：

    pip install -U tmcpy

## 用法示例

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


## 官方文档

请查阅淘宝开放平台消息服务官方文档:

http://open.taobao.com/doc/detail.htm?id=101663

## License

The MIT License (MIT)

Copyright (c) 2015 messense

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
