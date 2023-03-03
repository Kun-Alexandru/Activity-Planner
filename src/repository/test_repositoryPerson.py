import unittest
from src.repository.repositoryPerson import *

class RepositoryPersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repository_person()

    def test_add_validInput_True(self):
        self._repo.add(Person(1,"Tudor","0745406005"))
        self.assertTrue(self._repo.add(Person(2,"Mirel","0743215236")))


    def test_add_existing__Id__RepositoryException(self):
        self._repo.add(Person(1, "Tudor", "0745406005"))
        with self.assertRaises(RepositoryException):
            self._repo.add(Person(1, "Mirel", "0743215236"))

    def test_remove_by_id__NonExistingID__False(self):
        self.assertFalse(self._repo.remove_by_id(10))

    def test_update_repo__NonExisitingID__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._repo.update_repo(1000,"Mihai","0783433212")

    def test_repository_person(self):
        self._repo.add(Person(15, "Alex", "0745406005"))
        self._repo.add(Person(25, "Tudor", "0744444444"))

        self.assertEqual(self._repo[15].person_id,15)
        self.assertEqual(self._repo[25].name,"Tudor")
        self.assertEqual(self._repo[25].phone_number,"0744444444")