import unittest

from src.domain.person import Person

class PersonTest(unittest.TestCase):
    def test_person(self):
        person = Person(100, "Vlad", "0745406005")
        self.assertEqual(person.person_id,100)
        self.assertEqual(person.name,"Vlad")
        self.assertEqual(person.phone_number,"0745406005")
        person.name = "Tudor"
        person.person_id = 1000
        person.phone_number = "0755443322"
        self.assertEqual(person.person_id,1000)
        self.assertEqual(person.name,"Tudor")
        self.assertEqual(person.phone_number,"0755443322")
        with self.assertRaises(ValueError):
            person.person_id = "Ana"
