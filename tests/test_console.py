#!/usr/bin/python3
"""test for console"""
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
from models.engine.file_storage import Filestorage
import sys
from io import StringIO

f = Filestorage()


class TestConsole(unittest.TestCase):

    """"tests for console"""

    def test_help(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
"""
        self.assertEqual(s, f.getvalue())

if __name__ == '__main__':
    unittest.main()
