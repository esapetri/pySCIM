#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Authors: Esa-Petri Tirkkonen (esa.petri.tirkkonen@csit.fi) 2020
#
"""
"""

import os
import json
import logging
from User import User
from Group import Group
from MyUtils import MyUtils
from FSDB import FSDB

#variable
log = logging.getLogger("test")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

PORT = 4555
HOSTNAME = "localhost"
APP_VERSION = 0.1
program_folder_str = str(os.environ['HOME']) + '/' + str("pySCIM")
logs_folder_str = program_folder_str + '/' + str("logs")

utils = MyUtils(log)
log.debug(program_folder_str)
db = FSDB(program_folder_str,log,utils)

#TODO this test should be difided into 3 difernt test
def user_test():
    """
        test users code, this test should be difided into 3 difernt test
    """
    log.info("\n User tests:")
    newUser = User(PORT, HOSTNAME, APP_VERSION)
    data_dump = json.dumps(newUser.dataDump(), indent=4)
    log.debug("User data 1:")
    log.debug(data_dump)
    newUser.dataLoad(json.loads(data_dump))
    log.debug("User data 2:")
    data_dump2=json.dumps(newUser.dataDump())
    log.debug(data_dump2)
    return data_dump == data_dump2

#TODO this test should be difided into 3 difernt test
def group_test():
    """
        test groups code
    """
    log.info("\ngroup test")
    # group test
    newgroup = Group(PORT, HOSTNAME, APP_VERSION)
    newgroup.addMember("1")
    newgroup.addMember("2")
    data_dump = json.dumps(newgroup.dataDump(), indent=4)
    log.debug(data_dump)
    newgroup.dataLoad(json.loads(data_dump))
    data_dump2=json.dumps(newgroup.dataDump())
    log.debug(data_dump2)
    return data_dump == data_dump2

def FSDB_test_get_user_list():
    log.info("FSDB_test_get_user_list()")
    db.get_user_list()

#user_test()
#group_test()
FSDB_test_get_user_list()
