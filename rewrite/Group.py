# -*- coding: utf-8 -*-
#
# Authors: Esa-Petri Tirkkonen (esa.petri.tirkkonen@csit.fi) 2020
#
"""
"""

import uuid
import datetime
import json

class Group:
    port = 0
    hostname = ""

    # meta data, these are either constant or automatic
    schema = "schemas:[urn:ietf:params:scim:schemas:core:2.0:Group]"
    resourceType = "User"
    created = str(datetime.datetime.now())
    lastModified = str(datetime.datetime.now())
    version = 0

    # user id
    id = str(uuid.uuid4())
    externalId = ""  # id used in external system

    def __init__(self, portIn=0, hostNameIn="", appVersionIn=0):
        """
        default constructor
        :param portIn:
        :param hostNameIn:
        :param appVersionIn:
        """
        self.port = portIn
        self.hostname = hostNameIn
        self.version = appVersionIn

    # location metadata
    location = "http://" + hostname + ":" + str(port) + "/v2/Groups/" + str(id)

    displayName = ""  # "Sales Reps",
    members = []  # List of users in this group

    def IsMemember(self, id):
        """

        Check if user is allready in members list
        :param id:
        :return:
        """
        if id in self.members:
            return True
        return False

    def addMember(self, id):
        """
        add user to members list
        :param id:
        :return:
        """
        if self.IsMemember(id):
            return False
        else:
            self.members.append(id)
        return True

    def dellMember(self):
        """
        remove user from members list
        :return:
        """
        if self.IsMemember(id):
            self.members.remove(id)
        else:
            return False
        return True

    def membersToString(self):
        """
        members list into string
        :return:
        """
        strOut = ""
        i = 0
        for m in self.members:
            if i > 0:
                strOut = strOut + "," + str(m)
            else:
                strOut = str(m)
            i = i + 1
        return strOut

    def dataDump(self):
        """
        dataDump
        :return:
        """
        data = {
            "schema": self.schema,
            "id": self.id,
            "externalId": self.externalId,
            "meta": {
                "resourceType": self.resourceType,
                "created": self.created,
                "lastModified": self.lastModified,
                "location": self.location,
                "version": self.version,
            },
            "displayName": self.displayName,
            "members": self.members
        }
        return data

    def dataLoad(self, data):
        """
        dataload
        :rtype: object
        """
        self.schema = data['schema']
        self.id = data['id']
        self.externalId = data['externalId']
        self.resourceType = data['meta']['resourceType']
        self.created = data['meta']['created']
        self.lastModified = data['meta']['lastModified']
        self.location = data['meta']['location']
        self.version = data['meta']['version']
        self.displayName = data['displayName']
        self.members = data['members']
