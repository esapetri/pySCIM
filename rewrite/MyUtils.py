# -*- coding: utf-8 -*-
#
# Authors: Esa-Petri Tirkkonen (esa.petri.tirkkonen@csit.fi) 2020
#
"""
"""

import logging
import errno
import glob
import os
import shutil
import ntpath

class MyUtils:
    """
    """

    log = logging.getLogger("temp")

    def __init__(self, logIn):
        self.log = logIn

    def setMyUtilsLogger(self,logIn):
        self.log = logIn

    def folder_exist(self, path_string):
        """"check if folder exsist

        Parameters:
        path_string (String): path to file

        return (boolean): does folder exist
        """
        if not os.path.isdir(path_string):
            self.log.info('folderExist(): dir ' + str(path_string) + ' does not exist')
            return False
        return True

    def files_matching_in_folders(self, format_str, folders_list_str):
        """ go trough given folders and check folders for format matching files.

        :param format_str: (str) unix style filtering format, example #format='/filestart*.ending'
        :param folders_list_str: (list[str]) list of full folder paths to be scanned
        :return:
        """
        file_list_str = []

        if not format_str or not folders_list_str:
            self.log.error('files_matching_in_folders(): parameter was None')

        self.log.info('files_matching_in_folders(' + str(format_str) + ',):')

        for dir_temp_str in folders_list_str:
            if not self.folder_exist(dir_temp_str):
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                        dir_temp_str)

        self.log.debug('files_matching_in_folders(): folders:')
        self.log.debug(folders_list_str)
        for dir_temp_str in folders_list_str:
            for name in glob.glob(str(dir_temp_str) + str(format_str)):
                file_list_str.append(name)

        return file_list_str

    def move_file(self, full_file_path_str, destination_folder_path_str):
        """"move file to given folder

        Parameters:
        full_file_path_str (String): path and filename of file to be moved
        destination_folder_path_str (String): full patch and name of target folder

        return (boolean): was operation succesfull
        """
        if not full_file_path_str or not destination_folder_path_str:
            self.log.error('move_file(): parameter was None')
            return
        self.log.info('move_file(): ' + str(full_file_path_str) + ' -> ' + str(destination_folder_path_str))

        # Throw error in failures and log them
        if len(full_file_path_str) < 1:
            self.log.warning('move_file(): file list is empty')
            return False

        if not self.folder_exist(destination_folder_path_str):
            return False

        if os.path.isfile(str(destination_folder_path_str) + "/" + str(ntpath.basename(full_file_path_str))):
            self.log.warning('move_file(): file:'
                        + str(str(destination_folder_path_str) + "/" + ntpath.basename(full_file_path_str))
                        + " already exist, cant move it")
            return False

        if not os.path.isfile(str(full_file_path_str)):
            self.log.error("moveFile(): " + str(full_file_path_str) +
                      " is not a file, failed to move it to " + str(destination_folder_path_str))
            return False
        else:
            # for files in full_file_path_str:
            shutil.move(full_file_path_str, destination_folder_path_str)
            self.log.info("move_file():"+str(full_file_path_str) + ' has been moved.')
            return True
