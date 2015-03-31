# coding: utf-8

from tmcpy.message import ConfirmMessage, QueryMessage
from tmcpy.messageio import writer


def confirm_message(message_id, token):
    cm = ConfirmMessage()
    cm.token = token
    cm.update_content({'id': message_id})
    return writer(cm)


def query_message(**kwargs):
    return writer(QueryMessage(**kwargs))
