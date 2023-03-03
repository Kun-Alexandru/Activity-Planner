from src.repository.repositoryPerson import *
from src.services.undo import *
from src.services.handlers import *
class PersonService:
    # TODO Fill in this skeleton class
    def __init__(self, person_repository):
        self.__repository = person_repository

    def add_person(self, person):
        """
        A function that adds a new person in the repository
        :param person: new person
        :return:
        """
        self.__repository.add(person)

    def get_all_people(self):
        """
        A function that retunrs all the people as a list
        :return: list of people
        """
        return self.__repository.get_all_people()

    def remove_person_by_id(self, givenPersonID):
        """
        A function that removes the person with a given id from the repository (if there is one)
        :param givenPersonID:  given id
        :return:
        """
        self.__repository.remove_by_id(givenPersonID)

    def update_person_by_id(self,givenID, givenName, givenPhoneNumber):
        """
        A function that updated the peprson with a given id
        :param givenID: given id
        :param givenName:  new name
        :param givenPhoneNumber: new phone number
        :return:
        """
        self.__repository.update_repo(givenID, givenName, givenPhoneNumber)

    def is_an_id_in_repo(self, givenID):
        """
        A function that checks if an id is in repository or not
        :param givenID: given id
        :return: True if the id is in repo or False otherwise
        """
        data = self.__repository.data
        if givenID in data:
            return True
        else:
            return False

    def search_people_by_name(self, givenName):
        data = self.__repository.data
        listOfPeople = []
        givenName = givenName.strip(",. ")
        for elements in data:
            if givenName.lower() in data[elements].name.lower():
                listOfPeople.append(data[elements])

        return listOfPeople

    def search_people_by_phone_number(self, givenPhoneNumber):
        data = self.__repository.data
        listOfPeople = []
        givenPhoneNumber = givenPhoneNumber.strip(",. ")
        for elements in data:
            if givenPhoneNumber in data[elements].phone_number:
                listOfPeople.append(data[elements])
        return listOfPeople




