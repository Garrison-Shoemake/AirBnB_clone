#!/usr/bin/python3
""" Handling persistence"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
