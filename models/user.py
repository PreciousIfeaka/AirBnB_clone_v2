#!/usr/bin/env python 3

"""This module has a sub-class __user__
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
