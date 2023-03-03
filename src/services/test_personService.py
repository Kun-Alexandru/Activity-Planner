import unittest
from src.services.personService import *

class ServicePersonTest(unittest.TestCase):
    def test_person_service(self):
        person_repository = Repository_person()
        person_service = PersonService(person_repository)
        person_service.add_person(Person(1,"Andrei","0743322121"))
        person_service.add_person(Person(2, "Oana", "0743322122"))
        self.assertEqual(person_repository[1].person_id,1)
        self.assertEqual(person_repository[2].person_id,2)
        self.assertEqual(person_repository[1].name,"Andrei")
        self.assertEqual(person_repository[2].phone_number,"0743322122")
        self.assertTrue(person_service.is_an_id_in_repo(2))
        person_service.remove_person_by_id(2)
        self.assertTrue(person_service.is_an_id_in_repo(1))
        self.assertFalse(person_service.is_an_id_in_repo(2))

    def test_search_people_by_name(self):
        person_repository = Repository_person()
        person_service = PersonService(person_repository)
        person_service.add_person(Person(1, "Andrei", "0743322121"))
        person_service.add_person(Person(2, "Oana", "0743322122"))
        person_service.add_person(Person(3, "Ana", "0743352121"))
        person_service.add_person(Person(4, "Ioana", "0748322122"))
        listOfPeople = person_repository.get_all_people()
        expectedList = []
        expectedList.append(listOfPeople[1])
        expectedList.append(listOfPeople[3])
        self.assertEqual(person_service.search_people_by_name("oana"),expectedList)

    def test_search_people_by_phone_number(self):
        person_repository = Repository_person()
        person_service = PersonService(person_repository)
        person_service.add_person(Person(1, "Andrei", "0743322121"))
        person_service.add_person(Person(2, "Oana", "0743322122"))
        person_service.add_person(Person(3, "Ana", "0743352121"))
        person_service.add_person(Person(4, "Ioana", "0748322122"))
        listOfPeople = person_repository.get_all_people()
        expectedList = []
        expectedList.append(listOfPeople[2])
        self.assertEqual(person_service.search_people_by_phone_number("0743352121"),expectedList)
        expectedList = []
        expectedList.append(listOfPeople[1])
        self.assertEqual(person_service.search_people_by_phone_number("0743322122"), expectedList)
