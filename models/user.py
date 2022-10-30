#!/usr/bin/env python 3

"""This module has a sub-class __user__
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
