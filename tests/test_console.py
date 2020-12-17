#!/usr/bin/python3
"""Unittest for Console"""
import unittest
import sys
import contextlib
import os
import models
from console import HBNBCommand
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from unittest.mock import patch
import MySQLdb

tbl_cls = {"states": State, "cities": City, "places": Place,
           "amenities": Amenity, "users": User, "reviews": Review}


class TestConsole(unittest.TestCase):
    """Unittest for console"""

    def test_quit(self):
        """Testing quit method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("quit")
            self.assertEqual(buf.getvalue(), "")

    def test_EOF(self):
        """Testing EOF method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(buf.getvalue(), "")

    def test_emptyline(self):
        """Testing emptyline input"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("")
            self.assertEqual(buf.getvalue(), "")
            HBNBCommand().onecmd("      ")
            self.assertEqual(buf.getvalue(), "")

    def test_create(self):
        """Testing create method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("create")
            expected = "** class name missing **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("create Hello")
            expected = "** class doesn't exist **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create State name="Texas"')
            st_id = buf.getvalue()
            self.assertNotEqual(st_id, "")

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create City name="Houston" state_id={}'.
                                 format(st_id))
            ct_id = buf.getvalue()
            self.assertNotEqual(ct_id, "")

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create User email="al@al.com" password="pd"')
            u_id = buf.getvalue()
            self.assertNotEqual(u_id, "")

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create Place name="R" city_id={} user_id={}'
                                 .format(ct_id, u_id))
            pl_id = buf.getvalue()
            self.assertNotEqual(pl_id, "")

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create Amenity name="Kitchen"')
            self.assertNotEqual(buf.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd('create Review place_id={} user_id={}\
            text="ok"'.format(pl_id, u_id))
            self.assertNotEqual(buf.getvalue(), "")

    def test_show(self):
        """Testing show method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("show")
            expected = "** class name missing **\n"
            self.assertEqual(buf.getvalue(), expected)
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("show Hola")
            expected = "** class doesn't exist **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("show BaseModel")
            expected = "** instance id missing **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("show BaseModel hola")
            expected = "** no instance found **\n"
            self.assertEqual(buf.getvalue(), expected)
        ls = models.storage.all().values()
        if len(ls) > 0:
            obj_id = str(list(ls)[0].id)
            obj_class = list(ls)[0].__class__.__name__
            arg = "show " + obj_class + " " + obj_id
            with patch('sys.stdout', new=StringIO()) as buf:
                HBNBCommand().onecmd(arg)
                self.assertNotEqual(buf.getvalue(), "")

    def test_destroy(self):
        """Testing destroy method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("destroy")
            expected = "** class name missing **\n"
            self.assertEqual(buf.getvalue(), expected)
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("destroy Hola")
            expected = "** class doesn't exist **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("destroy BaseModel")
            expected = "** instance id missing **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("destroy BaseModel hola")
            expected = "** no instance found **\n"
            self.assertEqual(buf.getvalue(), expected)
        ls = models.storage.all().values()
        if len(ls) > 0:
            obj_id = str(list(ls)[0].id)
            obj_class = list(ls)[0].__class__.__name__
            arg = "destroy " + obj_class + " " + obj_id
            key = obj_class + "." + obj_id
            with patch('sys.stdout', new=StringIO()) as buf:
                HBNBCommand().onecmd(arg)
                self.assertEqual(buf.getvalue(), "")
                self.assertNotIn(key, models.storage.all())

    def test_all(self):
        """Testing method all"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("all Hola")
            expected = "** class doesn't exist **\n"
            self.assertEqual(buf.getvalue(), expected)

    def test_update(self):
        """Testing update method"""
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("update")
            expected = "** class name missing **\n"
            self.assertEqual(buf.getvalue(), expected)
        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("update Hola")
            expected = "** class doesn't exist **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("update BaseModel")
            expected = "** instance id missing **\n"
            self.assertEqual(buf.getvalue(), expected)

        with patch('sys.stdout', new=StringIO()) as buf:
            HBNBCommand().onecmd("update BaseModel hola")
            expected = "** no instance found **\n"
            self.assertEqual(buf.getvalue(), expected)

        ls = models.storage.all().values()
        if len(ls) > 0:
            obj_id = str(list(ls)[0].id)
            obj_class = list(ls)[0].__class__.__name__
            arg = "update " + obj_class + " " + obj_id
            key = obj_class + "." + obj_id
            with patch('sys.stdout', new=StringIO()) as buf:
                HBNBCommand().onecmd(arg)
                expected = "** attribute name missing **\n"
                self.assertEqual(buf.getvalue(), expected)
            with patch('sys.stdout', new=StringIO()) as buf:
                arg2 = arg + " " + "Age"
                HBNBCommand().onecmd(arg2)
                expected = "** value missing **\n"
                self.assertEqual(buf.getvalue(), expected)

            with patch('sys.stdout', new=StringIO()) as buf:
                arg3 = arg2 + " " + "30"
                HBNBCommand().onecmd(arg3)
                self.assertEqual(buf.getvalue(), "")

    def test_count(self):
        """Testing count method"""
        ls = models.storage.all().values()
        if len(ls) > 0:
            obj_id = str(list(ls)[0].id)
            obj_class = list(ls)[0].__class__.__name__
            arg = "count " + obj_class
            key = obj_class + "." + obj_id
            with patch('sys.stdout', new=StringIO()) as buf:
                HBNBCommand().onecmd(arg)
                self.assertNotEqual(buf.getvalue(), 0)
