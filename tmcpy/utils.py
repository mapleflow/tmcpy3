# coding: utf-8
from __future__ import absolute_import, unicode_literals
import six

from tmcpy.message import ConfirmMessage, QueryMessage

__all__ = [
    'confirm_message',
    'query_message',
    'to_binary',
]


def confirm_message(message_id, token):
    from tmcpy.messageio import writer

    cm = ConfirmMessage()
    cm.token = token
    cm.update_content({'id': message_id})
    return writer(cm)


def query_message(**kwargs):
    from tmcpy.messageio import writer

    return writer(QueryMessage(**kwargs))


def to_binary(value, encoding='utf-8'):
    """Convert value to binary string, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return six.binary_type(value)
