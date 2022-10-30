<<<<<<< HEAD
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
=======
#!/usr/bin/python3
"""file contains User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
