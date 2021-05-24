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
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy({})'.format(u_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(f.getvalue()) == 1)

        """test review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            r_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.show({})'.format(r_id))
            m = f.getvalue()
            self.assertIn('[Review]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Review.destroy({})'.format(r_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Review ({})'.format(r_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)
        """test place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            p_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.show({})'.format(p_id))
            m = f.getvalue()
            self.assertIn('[Place]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Place.destroy({})'.format(p_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show Place ({})'.format(p_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)
        """test ramenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            a_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.show({})'.format(a_id))
            m = f.getvalue()
            self.assertIn('[Amenity]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('Amenity.destroy({})'.format(a_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User ({})'.format(a_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)
        """test state"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            s_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.show({})'.format(s_id))
            m = f.getvalue()
            self.assertIn('[State]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('State.destroy({})'.format(s_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User ({})'.format(s_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)
        """test city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            c_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            m = f.getvalue()
            self.assertTrue(len(m) > 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.show({})'.format(c_id))
            m = f.getvalue()
            self.assertIn('[City]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('City.destroy({})'.format(c_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show City ({})'.format(c_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)

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
            HBNBCommand().onecmd('BaseModel.show({})'.format(b_id))
            m = f.getvalue()
            self.assertIn('[BaseModel]', m)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            s2 = "** instance id missing **\n"
            self.assertEqual(s2, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy({})'.format(b_id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel ({})'.format(b_id))
            s2 = "** no instance found **\n"
            self.assertEqual(f.getvalue(), s2)

if __name__ == '__main__':
    unittest.main()
