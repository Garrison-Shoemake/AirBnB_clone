#!/usr/bin/python3
"""test for console"""

import os
import sys
import unittest
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

f = FileStorage()

s = ("\nDocumented commands (type help <topic>):\n"
     "========================================\n"
     "EOF  all  create  destroy  help  quit  show  update\n\n")


class TestConsole(unittest.TestCase):

    """"tests for console"""

    def test_help(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(s, f.getvalue())

    def test_EOF(self):
        """test EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            m = f.getvalue()
            self.assertTrue(len(m) == 1)

if __name__ == '__main__':
    unittest.main()
