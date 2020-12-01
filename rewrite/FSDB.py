"""
FSDB = Filesytem Database
name comes from fact that data is stored to filesystem directly,
and datbasefunctionality is inreality just file manipulation.
This is because it was fastest way to implement DB in our lazy
planing session
"""

import logging
import os
from User import User
from Group import Group
from MyUtils import MyUtils

class FSDB:
    """

    """

    #variables
    log = logging.getLogger("temp")
    utils = None
    folder = ''
    users_folder_str = ''
    groups_folder_str = ''

    def __init__(self, folderIn, logIn, utilsIN):
        self.log = logIn
        self.utils = utilsIN
        self.folder = folderIn
        self.users_folder_str = str(folderIn) + '/' + str("users")
        self.groups_folder_str = str(folderIn) + '/' + str("groups")

        if not self.utils.folder_exist(self.users_folder_str):
            self.log.info("init(): users folder" + str(self.users_folder_str) + " Doesn't Exist. Creating new folder")
            os.makedirs(self.users_folder_str)

        if not self.utils.folder_exist(self.groups_folder_str):
            self.log.info("init(): groups folder" + str(self.groups_folder_str) + " Doesn't Exist. Creating new folder")
            os.makedirs(self.groups_folder_str)

    def get_user_list(self):
        """
        return list of all users in system
        """

        self.utils.files_matching_in_folders( "*.json", [self.users_folder_str])



    def is_user(self, id = '', username = '', name = ''):
        """
        Check if user exist
        """

        return False


    # print("\nuser test")
    # # user test
    # newUser = User(PORT, HOSTNAME, APP_VERSION)
    # data_dump = json.dumps(newUser.dataDump(), indent=4)
    # print(data_dump)
    # newUser.dataLoad(json.loads(data_dump))
    # print(json.dumps(newUser.dataDump()))
    #
    # print("\ngroup test")
    # # group test
    # newgroup = Group(PORT, HOSTNAME, APP_VERSION)
    # newgroup.addMember("1")
    # newgroup.addMember("2")
    # data_dump = json.dumps(newgroup.dataDump(), indent=4)
    # print(data_dump)
    # newgroup.dataLoad(json.loads(data_dump))
    # print(json.dumps(newgroup.dataDump()))
