import unittest
import datetime
from src.domain.activity import Activity

class activityTest(unittest.TestCase):
    def test_activity(self):
        listOfID = [100, 200, 300]
        activity = Activity(100, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal", listOfID)
        self.assertEqual(activity.activity_id, 100)
        self.assertEqual(activity.date, datetime.date(2020, 7, 5))
        self.assertEqual(activity.timeStart,datetime.time(16, 15, 00))
        self.assertEqual(activity.description,"Fotbal")
        self.assertEqual(activity.person_id,listOfID)