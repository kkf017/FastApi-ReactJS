"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for User Controller.

-----------------------------------------------------------------------------------------------------------------"""

from services.database.database import HASH
from services.User.UserModel import *

from typing import Dict



def getUserController(uid:str)->Dict[str, str]:
    """ 
        Function to get a User (in database).
            input:
                uid - id of user
            output:
                User
       opt.
    """
    return getUserModel(uid)


def createUserController(email:str, password:str)->bool:
    """ 
        Function to create a User (in database).
            input:
                email, password - informations of user
            output:
                boolean
       opt.
    """
    if existUserModel(email):
        return False
    # Create account - procedure
    createUserModel(email, password)
    return True


def loginUserController(email:str, password:str)->bool:
    """ 
        Function to login.
            input:
                email, password - informations of user
            output:
                boolean
       opt.
    """
    value = selectUserModel(email)
    if value == {}:
        return False
    if not (value["password"] == HASH(password)):
        return False
    return True
 


def forgetUserController(email:str)->bool:
    """ 
        Function to reset password (if password has been forgotten).
            input:
                email - informations of user
            output:
                boolean
       opt.
    """
    pass


def updateEmailUserController(email:str, value:str)->bool:
    """ 
        Function to update email.
            input:
                email, value - informations of user, email to update
            output:
                boolean
       opt.
    """
    if not existUserModel(email):
        return False
    # Check email - procedure
    updateEmailUserModel(email, value)
    return True


def updatePasswordUserController(email:str, password:str, value:str)->bool:
    """ 
        Function to update password.
            input:
                password - informations of user
            output:
                boolean
       opt.
    """
    if not existUserModel(email):
        return False
    # Check email, password - procedure
    updatePasswordUserModel(email, password, value)
    return True
   


def removeUserController(uid:str)->bool:
    """ 
        Function to suppress account.
            input:
                email, password - informations of user
            output:
                boolean
       opt.
    """
    if getUserModel(uid) == {}:
        return False
    # Check email - procedure
    removeUserModel(uid)
    return True
