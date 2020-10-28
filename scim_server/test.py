#!/usr/bin/python
import uuid
import datetime
import json

# class that defines user
class User:
    port = 0
    hostname = ""

    #meta data, these are either constant or automatic
    schema = "schemas:[urn:ietf:params:scim:schemas:core:2.0:User]"
    resourceType = "User"
    created = str(datetime.datetime.now())
    lastModified= str(datetime.datetime.now())
    version = 0

    #user id
    id = str(uuid.uuid4())
    externalId = "" #id used in external system

    # default constructor
    def __init__(self,portIn=0,hostNameIn="",appVersionIN=0):
        self.port = portIn
        self.hostname = hostNameIn
        self.version = appVersionIn

    #location metadata
    location = "http://"+self.hostname+":"+str(self.port)+"/v2/Users/"+str(self.id)

    #user data
    socialSecurityCode = "" #221079-123A
    familyName = "" #Koskinen
    firstNames = "" #Keijo Esko Petri
    nickName = ""   #kamu
    address = ""    #Jaakonkatu 12 A 3
    postalCode = "" #52100
    PostalDistrict = "" #Helsinki

    LanguageCode = "" #FI
    LanguageCodeDescription = "" #FINLAND

    #work period data
    workPeriodId = str(uuid.uuid4())
    workPeriodDescription = "" #Osaston siivooja
    OficialJobDescription = "" #Siivooja
    workDepartment = "" #osaston nimi

    workPeriodStartDate = ""
    workPeriodEndDate = ""
    workPeriodStatus = False #true = working, false = period ended

    isSupervisor= False # is this person supervisor to somebody
    idOfSupervisor = "" # uuid of supervisor

    def dataLoad(self,data):
            self.id = data['id']
            self.externalId = data['externalId']

            self.resourceType = data['meta']['resourceType']
            self.created = data['meta']['created']
            self.lastModified = data['meta']['lastModified']
            self.location = data['meta']['location']
            self.version = data['meta']['version']

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
        data ={
            "schema": self.schema,
            "id":  self.id,
            "externalId":  self.externalId,
            "meta":{
                "resourceType":  self.resourceType,
                "created":  self.created,
                "lastModified":  self.lastModified,
                "location":  self.location,
                "version":  self.version,
            },
            "socialSecurityCode":  self.socialSecurityCode,
            "familyName":  self.familyName,
            "firstNames":  self.firstNames,
            "nickName":  self.nickName,
            "address":  self.address,
            "postalCode":  self.postalCode,
            "PostalDistrict":  self.PostalDistrict,
            "LanguageCode":  self.LanguageCode,
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

# class that defines groups
class group:
    port = 0
    hostname = ""

    #meta data, these are either constant or automatic
    schema = "schemas:[urn:ietf:params:scim:schemas:core:2.0:Group]"
    resourceType = "User"
    created = str(datetime.datetime.now())
    lastModified= str(datetime.datetime.now())
    version = 0

    #user id
    id = str(uuid.uuid4())
    externalId = "" #id used in external system

    # default constructor
    def __init__(self,portIn=0,hostNameIn="",appVersionIN=0):
        self.port = portIn
        self.hostname = hostNameIn
        self.version = appVersionIn

    #location metadata
    location = "http://"+self.hostname+":"+str(self.port)+"/v2/Groups/"+str(self.id)

    displayName = "" # "Sales Reps",
    members = [] #List of users in this group

    """
    Check if user is allready in members list
    """
    def IsMemeber(self,id):
        if id in self.members:
            return True
        return False

    """
    add user to members list
    """
    def addMember(self,id):
        if IsMemeber(id):
            return False
        else
            self.members.append(id)
        return True

    """
    remove user from members list
    """
    def dellMember(self):
        if IsMemeber(id):
            return False
        else
            self.members.append(id)
        return True

    """
    create coma separated string from members list
    """
    def membersToString(self)
        strOut = ""
        for m in self.members:
            strOut = strOut + "," + str(m)
        return strOut

    def dataDump(self):
        data ={
            "schema": self.schema,
            "id":  self.id,
            "externalId":  self.externalId,
            "meta":{
                "resourceType":  self.resourceType,
                "created":  self.created,
                "lastModified":  self.lastModified,
                "location":  self.location,
                "version":  self.version,
            },
            "displayName": self.displayName,
            "members":[self.membersToString()]
        }
        return data



#TODO link to main program
PORT=4555
HOSTNAME="localhost"
APP_VERSION=0.1

#user test
newUser = User(PORT,HOSTNAME,APP_VERSION)
data_dump = json.dumps(newUser.dataDump(), indent=4)
print(data_dump)

newUser.dataLoad(json.loads(data_dump))
print( json.dumps(newUser.dataDump()) )


#group test
newgroup = Group(PORT,HOSTNAME,APP_VERSION)
data_dump = json.dumps(newUser.dataDump(), indent=4)
print(data_dump)
