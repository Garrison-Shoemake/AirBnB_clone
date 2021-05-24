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

fs = FileStorage()

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

    def test_quit(self):
        """test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            m = f.getvalue()
            self.assertTrue(len(m) == 0)

    def test_space(self):
        """test space"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            s2 = ""
            self.assertEqual(s2, f.getvalue())

    def test_create_error(self, *args):
         """test create"""
         with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}")
            s2 = "** class doesn't exist **\n"
            self.assertEqual(s2, f.getvalue())

    def test_destroy_error(self, *args):
         """test create"""
         with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}")
            s2 = "** class doesn't exist **\n"
            self.assertEqual(s2, f.getvalue())


if __name__ == '__main__':
    unittest.main()
