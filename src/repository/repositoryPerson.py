import pickle
import os
from src.domain.person import *
from src.IterrableDS.sort_filter_iterable_data import *


class RepositoryException(Exception):
    pass


class Repository_person():
    def __init__(self):
        self._data = ItterableDataStructure()

    @property
    def data(self):
        return self._data

    def add(self, entity):
        """
        Function that adds a new person in the repository
        :param entity: person that is added in the repository
        :return:
        """
        if entity.person_id in self._data:
            raise RepositoryException("Person with ID " + str(entity.person_id) + " already in repo")
        else:
            self._data[entity.person_id] = entity
            return True

    def __getitem__(self, id):
        """
        A function that returns the person whith a certain id
        :param id: given id
        :return: the person with the given id (if there is one)
        """
        return self._data[id]

    def remove_by_id(self, givenID):
        """
         A function that removes the person with the given id
        :param givenID: given id
        :return:
        """
        if givenID in self._data:
            self._data.pop(givenID)
            return True
        else:
            return False

    def update_repo(self, givenID, givenName, givenPhoneNumber):
        """
        A function that updates the person with a given id
        :param givenID: given id of a person to update
        :param givenName: new name of the person
        :param givenPhoneNumber: new phone number of a person
        :return:
        """
        if givenID in self._data:
            self._data[givenID].name = givenName
            self._data[givenID].phone_number = givenPhoneNumber
            return True
        else:
            raise RepositoryException("Person with ID " + str(givenID) + " is not in repo")

    def get_all_people(self):
        """
        returns all the people as a list
        :return:
        """
        return list(self._data.values())


class PersonTextFileRepository(Repository_person):

    def __init__(self,inputFileName):
        super().__init__()
        self._save_file_name = "files/person.txt"
        self._input_file_name = inputFileName
        self._load_file()

    def _load_file(self):
        if(self._input_file_name != ""):
            file = open(self._input_file_name, "rt")
            for line in file.readlines():
                person_data = line.split(",")
                person = Person(int(person_data[0]),person_data[1],person_data[2].strip("\n"))
                self.add(person)
            file.close()

    def _save_file(self):
        file = open(self._save_file_name, "wt")
        for person in self._data.values():
            file.write(str(person.person_id) + "," + person.name + "," + person.phone_number + "\n")

    def add(self, entity):
        super(PersonTextFileRepository, self).add(entity)
        self._save_file()

    def remove_by_id(self, givenID):
        super(PersonTextFileRepository,self).remove_by_id(givenID)
        self._save_file()

    def update_repo(self, givenID, givenName, givenPhoneNumber):
        super(PersonTextFileRepository,self).update_repo(givenID,givenName,givenPhoneNumber)
        self._save_file()

class PersonBinaryFileRepository(Repository_person):
    def __init__(self,inputFileName):
        super().__init__()
        self._save_file_name = "files/person.bin"
        self._input_file_name = inputFileName
        self._load_file()

    def _load_file(self):
        if (self._input_file_name != ""):
            if os.path.getsize(self._input_file_name) > 0:
                file = open(self._input_file_name,"rb")
                self._data = pickle.load(file)
                file.close()

    def _save_file(self):
        file = open(self._save_file_name, "wb")
        pickle.dump(self._data,file)
        file.close()

    def add(self, entity):
        super(PersonBinaryFileRepository, self).add(entity)
        self._save_file()

    def remove_by_id(self, givenID):
        super(PersonBinaryFileRepository, self).remove_by_id(givenID)
        self._save_file()

    def update_repo(self, givenID, givenName, givenPhoneNumber):
        super(PersonBinaryFileRepository, self).update_repo(givenID, givenName, givenPhoneNumber)
        self._save_file()

