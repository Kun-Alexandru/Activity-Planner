class Person:
    """
    -person_id, name, phone_number
    """
    def __init__(self, _id, name="", phoneNumber=""):
        """
        Create a new person
        :param _id: id of the person
        :param name: name of the person
        :param phoneNumber: phone number of the person
        """
        self.__person_id = _id
        self.__name = name
        self.__phone_number = phoneNumber

    def __str__(self):
        return 'ID - {}, nume - {}, phone number - {}'.format(self.person_id, self.name, self.phone_number)

    @property
    def person_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @property
    def phone_number(self):
        return self.__phone_number

    @name.setter
    def name(self, newName):
        if(type(newName) != str):
            raise ValueError("Name should be a string!")
        self.__name = newName

    @phone_number.setter
    def phone_number(self, newPhoneNumber):
        if (type(newPhoneNumber) != str):
            raise ValueError("Phone number should be a string!")
        self.__phone_number = newPhoneNumber

    @person_id.setter
    def person_id(self, newPersonID):
        if (type(newPersonID) != int):
            raise ValueError("Person id should be a int type")
        self.__person_id = newPersonID

