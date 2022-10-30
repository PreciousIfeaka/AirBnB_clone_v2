#!/usr/bin/env python3
"""This deserializes json file"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
