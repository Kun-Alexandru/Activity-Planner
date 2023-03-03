import unittest
from src.services.activityService import *
import datetime

class ActivityServiceTest(unittest.TestCase):
    def test_activity_service(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)

        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 5), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet", [100]))
        self.assertEqual(activity_repository[1].activity_id,1)
        self.assertEqual(activity_repository[2].date,datetime.date(2020, 7, 5))
        self.assertEqual(activity_repository[1].person_id,[100, 200])
        self.assertTrue(activity_service.is_an_id_in_repo(1))
        activity_service.remove_activity_by_id(1)
        self.assertTrue(activity_service.is_an_id_in_repo(2))

    def test_search_activity_by_date(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 8), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(17, 00, 00), "Baschet",[100,200,300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[0])
        expectedList.append(listOfActivities[2])
        self.assertEqual(activity_service.search_activity_by_date(2020,7,5),expectedList)
        expectedList = []
        expectedList.append(listOfActivities[1])
        self.assertEqual(activity_service.search_activity_by_date(2020,7,8),expectedList)

    def test_search_activity_by_time_start(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 8), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(17, 00, 00), "Baschet",[100, 200, 300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[1])
        self.assertEqual(activity_service.search_activity_by_time_start(18,00),expectedList)
        expectedList = []
        expectedList.append(listOfActivities[0])
        self.assertEqual(activity_service.search_activity_by_time_start(16, 15), expectedList)

    def test_search_activity_by_time_end(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 8), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(17, 00, 00), "Baschet",[100, 200, 300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[1])
        self.assertEqual(activity_service.search_activity_by_time_end(20, 00), expectedList)
        expectedList = []
        expectedList.append(listOfActivities[2])
        self.assertEqual(activity_service.search_activity_by_time_end(17, 00), expectedList)

    def test_search_activity_by_description(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 8), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(17, 00, 00), "Baschet",[100, 200, 300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[1])
        expectedList.append(listOfActivities[2])
        self.assertEqual(activity_service.search_activity_by_description("Baschet"),expectedList)
        expectedList = []
        expectedList.append(listOfActivities[0])
        self.assertEqual(activity_service.search_activity_by_description("Fotbal"), expectedList)

    def test_activities_for_a_given_person(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 8), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(17, 00, 00), "Baschet",[100, 200, 300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[0])
        expectedList.append(listOfActivities[1])
        expectedList.append(listOfActivities[2])
        self.assertEqual(activity_service.activities_for_a_given_person(100),expectedList)
        expectedList = []
        expectedList.append(listOfActivities[0])
        expectedList.append(listOfActivities[2])
        self.assertEqual(activity_service.activities_for_a_given_person(200), expectedList)
        expectedList = []
        self.assertEqual(activity_service.activities_for_a_given_person(500), expectedList)

    def test_activities_for_a_given_date(self):
        activity_repository = Repository_activity()
        activity_service = ActivityService(activity_repository)
        activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(18, 15, 00), datetime.time(19, 00, 00), "Fotbal",[100, 200]))
        activity_service.add_activity(Activity(2, datetime.date(2020, 7, 5), datetime.time(15, 00, 00), datetime.time(20, 00, 00), "Baschet",[100]))
        activity_service.add_activity(Activity(3, datetime.date(2020, 7, 5), datetime.time(17, 00, 00), datetime.time(17, 00, 00), "Baschet",[100, 200, 300]))
        listOfActivities = activity_service.get_all_activities()
        expectedList = []
        expectedList.append(listOfActivities[1])
        expectedList.append(listOfActivities[2])
        expectedList.append(listOfActivities[0])
        self.assertEqual(activity_service.activities_for_a_given_date(2020,7,5), expectedList)
        expectedList = []
        self.assertEqual(activity_service.activities_for_a_given_date(2021, 7, 5), expectedList)
