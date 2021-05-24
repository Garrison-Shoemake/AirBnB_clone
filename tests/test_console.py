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

    def test_all(self):
        """test all, starting with user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            u_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.show({})'.format(u_id))
            m = f.getvalue()
            self.assertIn('[User]', m)

        """test review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        """test place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        """test ramenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        """test state"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        """test city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)

    def test_basemodel(self, *args):
        """test create basemodel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            b_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        """test show basemodel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            s2 = "** instance id missing **\n"
            self.assertEqual(s2, f.getvalue())
        """test basemodel count"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            s2 = "** instance id missing **\n"
            self.assertEqual(s2, f.getvalue())


if __name__ == '__main__':
    unittest.main()
