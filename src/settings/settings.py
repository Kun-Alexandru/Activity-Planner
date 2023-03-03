from configparser import ConfigParser
from src.repository.repositoryPerson import *
from src.repository.repositoryActivity import *

class Settings:
    def __init__(self):
        parser = ConfigParser()
        parser.read("settings/settings.properties")
        repository_type = parser.get("main",'repository')
        peopleFileInputName = parser.get("main",'people')
        activitiesFileInputName = parser.get("main","activities")

        if repository_type == "inmemory":
            self.personRepository = Repository_person()
            self.activityRepository = Repository_activity()
        elif repository_type == "CSV":
            self.personRepository = PersonTextFileRepository(peopleFileInputName)
            self.activityRepository = ActivityTextFileRepository(activitiesFileInputName)
        elif repository_type == "binary":
            self.personRepository = PersonBinaryFileRepository(peopleFileInputName)
            self.activityRepository = ActivityBinaryFileRepository(activitiesFileInputName)

    def get_repositories(self):
        return self.personRepository,self.activityRepository
