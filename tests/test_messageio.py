# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest

from tmcpy.messageio import reader, writer
from tmcpy.message import Message


class MessageIOTestCase(unittest.TestCase):

    def test_reader(self):
        data = b'\x02\x01\x04\x00\x01\x00\x00\x00\x05\x00$\x00\x00\x0032e88d28-20b1-40dd-8e2d-abec197277fe\x00\x00'
        msg = reader(data)
        self.assertIsInstance(msg, Message)
        self.assertEqual('32e88d28-20b1-40dd-8e2d-abec197277fe', msg.token)
        self.assertEqual(1, msg.flag)
        self.assertEqual(52, msg.offset)
        self.assertEqual(2, msg.protocol_version)
        self.assertEqual(1, msg.message_type)

    def test_writer(self):
        msg = Message(
            protocol_version=2,
            message_type=1,
            flag=1,
            token='32e88d28-20b1-40dd-8e2d-abec197277fe'
        )
        data = writer(msg)
        expected = b'\x02\x01\x04\x00\x01\x00\x00\x00\x05\x00$\x00\x00\x0032e88d28-20b1-40dd-8e2d-abec197277fe\x00\x00'
        self.assertEqual(expected, data)
