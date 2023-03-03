import unittest
from src.repository.repositoryActivity import *
import datetime

class RepositoryActivityTest(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = Repository_activity()


    def test_add__ValidInput__True(self):
        self._repo.add(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        self.assertTrue(self._repo.add(Activity(2, datetime.date(2020, 7, 5), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100])))

    def test_add__ExistingID__RepositoryException(self):
        self._repo.add(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        with self.assertRaises(RepositoryException):
            self._repo.add(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))

    def test_remove_by_id__ExistingID__True(self):
        self._repo.add(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        self.assertTrue(self._repo.remove_by_id(1))

    def test_remove_by_id__NonExistingID__False(self):
        self.assertFalse(self._repo.remove_by_id(1))

    def test_update_repo__NonExistingID__RepositoryException(self):
        with self.assertRaises(RepositoryException):
            self._repo.update_repo(3, datetime.date(2020, 7, 5), datetime.time(18, 00, 00), datetime.time(20, 00, 00),"Baschet", [300, 400, 500])

    def test_repository_activity(self):
        self._repo.add(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200, 300]))
        self._repo.add(Activity(2, datetime.date(2020, 7, 5), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[300, 400, 500]))
        self._repo.update_repo(2, datetime.date(2020, 7, 5), datetime.time(19, 00, 00), datetime.time(20, 30, 00),"Volei", [200, 300, 400])
        self.assertEqual(self._repo[1].activity_id,1)
        self.assertEqual(self._repo[2].date,datetime.date(2020, 7, 5))
        self.assertEqual(self._repo[1].timeStart,datetime.time(16, 15, 00))
        self.assertEqual(self._repo[2].description,"Volei")
        self.assertEqual(self._repo[1].person_id,[100, 200, 300])

