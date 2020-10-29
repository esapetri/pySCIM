#!/usr/bin/python
import uuid
import datetime
import json


class User:
    """
    class that defines user
    """
    port = 0
    hostname = ""

    # meta data, these are either constant or automatic
    schema = "schemas:[urn:ietf:params:scim:schemas:core:2.0:User]"
    resourceType = "User"
    created = str(datetime.datetime.now())
    lastModified = str(datetime.datetime.now())
    version = 0

    # user id
    id = str(uuid.uuid4())
    externalId = ""  # id used in external system

    # default constructor
    def __init__(self, portIn=0, hostNameIn="", appVersionIn=0):
        """

        :param portIn:
        :param hostNameIn:
        :param appVersionIn:
        """
        self.port = portIn
        self.hostname = hostNameIn
        self.version = appVersionIn

    # location metadata
    location = "http://" + hostname + ":" + str(port) + "/v2/Users/" + str(id)

    # user data
    username = ""  # admin,root,keijo
    socialSecurityCode = ""  # 221079-123A
    familyName = ""  # Koskinen
    firstNames = ""  # Keijo Esko Petri
    nickName = ""  # kamu
    address = ""  # Jaakonkatu 12 A 3
    postalCode = ""  # 52100
    PostalDistrict = ""  # Helsinki

    LanguageCode = ""  # FI
    LanguageCodeDescription = ""  # FINLAND

    # work period data
    workPeriodId = str(uuid.uuid4())
    workPeriodDescription = ""  # Osaston siivooja
    OficialJobDescription = ""  # Siivooja
    workDepartment = ""  # osaston nimi

    workPeriodStartDate = ""
    workPeriodEndDate = ""
    workPeriodStatus = False  # true = working, false = period ended

    isSupervisor = False  # is this person supervisor to somebody
    idOfSupervisor = ""  # uuid of supervisor

    def dataLoad(self, data):
        """
        dataLoad
        :param data:
        """
        self.id = data['id']
        self.externalId = data['externalId']

        self.resourceType = data['meta']['resourceType']
        self.created = data['meta']['created']
        self.lastModified = data['meta']['lastModified']
        self.location = data['meta']['location']
        self.version = data['meta']['version']

        self.username = data['username']
        self.socialSecurityCode = data['socialSecurityCode']
        self.familyName = data['familyName']
        self.firstNames = data['firstNames']
        self.nickName = data['nickName']
        self.address = data['address']
        self.postalCode = data['postalCode']
        self.PostalDistrict = data['PostalDistrict']
        self.LanguageCode = data['LanguageCode']
        self.LanguageCodeDescription = data['LanguageCodeDescription']
        self.workPeriodId = data['workPeriodId']
        self.workPeriodDescription = data['workPeriodDescription']
        self.OficialJobDescription = data['OficialJobDescription']
        self.workDepartment = data['workDepartment']
        self.workPeriodStartDate = data['workPeriodStartDate']
        self.workPeriodEndDate = data['workPeriodEndDate']
        self.workPeriodStatus = data['workPeriodStatus']
        self.isSupervisor = data['isSupervisor']
        self.idOfSupervisor = data['idOfSupervisor']

    def dataDump(self):
        """
        dataDump
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
            "username": self.username,
            "socialSecurityCode": self.socialSecurityCode,
            "familyName": self.familyName,
            "firstNames": self.firstNames,
            "nickName": self.nickName,
            "address": self.address,
            "postalCode": self.postalCode,
            "PostalDistrict": self.PostalDistrict,
            "LanguageCode": self.LanguageCode,
            "LanguageCodeDescription": self.LanguageCodeDescription,
            "workPeriodId": self.workPeriodId,
            "workPeriodDescription": self.workPeriodDescription,
            "OficialJobDescription": self.OficialJobDescription,
            "workDepartment": self.workDepartment,
            "workPeriodStartDate": self.workPeriodStartDate,
            "workPeriodEndDate": self.workPeriodEndDate,
            "workPeriodStatus": self.workPeriodStatus,
            "isSupervisor": self.isSupervisor,
            "idOfSupervisor": self.idOfSupervisor
        }
        return data


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


# TODO link to main program
PORT = 4555
HOSTNAME = "localhost"
APP_VERSION = 0.1

print("\nuser test")
# user test
newUser = User(PORT, HOSTNAME, APP_VERSION)
data_dump = json.dumps(newUser.dataDump(), indent=4)
print(data_dump)
newUser.dataLoad(json.loads(data_dump))
print(json.dumps(newUser.dataDump()))

print("\ngroup test")
# group test
newgroup = Group(PORT, HOSTNAME, APP_VERSION)
newgroup.addMember("1")
newgroup.addMember("2")
data_dump = json.dumps(newgroup.dataDump(), indent=4)
print(data_dump)
newgroup.dataLoad(json.loads(data_dump))
print(json.dumps(newgroup.dataDump()))
