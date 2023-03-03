import datetime

from src.repository.repositoryActivity import *

class ServiceException(Exception):
    pass

from src.IterrableDS.sort_filter_iterable_data import *


def date_compare(activity1, activity2):
    # ascending order
    if activity1.date < activity2.date:
        return True
    else:
        return False

def year_higher_2022_function_filter(objectt):
    if objectt.date.year >= 2022:
        return True
    else:
        return False

def time_start_compare(activity1, activity2):
    if activity1.timeStart < activity2.timeStart:
        return True
    else:
        return False

class ActivityService:
    # TODO Fill in this skeleton class
    def __init__(self, activity_repository):
        self.__repository = activity_repository

    def add_activity(self, activity):
        """
        Function that adds a new activity in repository
        :param activity: new activity
        :return:
        """
        self.__repository.add(activity)

    def add_person_to_activities(self,givenPersonID,listOfActivitiesID):
        self.__repository.add_person_to_activities(givenPersonID,listOfActivitiesID)


    def get_all_activities(self):
        """
        Function that returns all the activities as a list
        :return: list of activities
        """
        return self.__repository.get_all_activities()

    def remove_activity_by_id(self, activityID):
        """
        Function that removes an activity by id
        :param activityID: given id
        :return:
        """
        self.__repository.remove_by_id(activityID)

    def update_activity_by_id(self, givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID):
        """
        A function that updates the activity with a given id, if there is one in the repository
        :param givenID: given id of activity in order to update it
        :param givenDate: new date of the activity
        :param givenTimeStart: new time start of the activity
        :param givenTimeEnd: new time end of the activity
        :param givenDescription: new description of the activity
        :param givenPersonID: new list of ppl that take part in the activity
        :return:
        """
        try:
            self.__repository.update_repo(givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription,
                                          givenPersonID)
        except RepositoryException as re:
            raise ServiceException("Id is not in repo")



    def remove_person_id_from_list_of_activities(self, givenID):
        """
        A function that removes the person with the given id from ALL the activities (used when we delete a person from the repository, because if he is deleted he cannot take part in any activites)
        :param givenID: given id of the person that we want to remove
        :return:
        """
        self.__repository.remove_person_id_from_list_of_participants(givenID)

    def is_an_id_in_repo(self, givenID):
        """
        A function that checks if a given id is already in the repository, or not
        :param givenID:
        :return: True if id is in repostiry or False otherwise
        """
        data = self.__repository.data
        if givenID in data:
            return True
        else:
            return False

    def is_already_in_a_specific_time_frame(self,givenID, givenDate, givenTimeStart, givenTimeEnd,activityID):
        """
        A function that checks if a person has free time in a given interval in. Used to check if he can be added in an activity or not
        :param givenID: person id
        :param givenDate: date of the activity
        :param givenTimeStart: time start of the activity
        :param givenTimeEnd: time end of the activity
        :param activityID: activity id (used when updating the activity in order to exclude the updated activity from the available time frame)
        :return: True if he is free in the given time frame or False otherwise
        """
        data = self.__repository.data
        time1Start = givenTimeStart
        time1End = givenTimeEnd
        for elements in data:
            if givenDate == data[elements].date and activityID != data[elements].activity_id: #are activitate in ziua respectiva
                if int(givenID) in data[elements].person_id: #este in lista cu participantii la activitate
                    time2Start = data[elements].timeStart
                    time2End = data[elements].timeEnd
                    if time2Start > time1Start and time2Start < time1End or time1Start > time2Start and time1Start < time2End or time1End > time2Start and time1End < time2End or time2End > time1Start and time2End < time1End:
                        return False

        return True


    def search_activity_by_date(self, givenYear, givenMonth, givenDay):
        data = self.__repository.data
        date = datetime.date(givenYear,givenMonth,givenDay)
        listOfActivities = []
        for elements in data:
            if date == data[elements].date:
                listOfActivities.append(data[elements])

        return listOfActivities

    def search_activity_by_time_start(self, givenHour, givenMinute):
        data = self.__repository.data
        time = datetime.time(givenHour,givenMinute)
        listOfActivities = []
        for elements in data:
            if time == data[elements].timeStart:
                listOfActivities.append(data[elements])

        return listOfActivities

    def search_activity_by_time_end(self, givenHour, givenMinute):
        data = self.__repository.data
        time = datetime.time(givenHour,givenMinute)
        listOfActivities = []
        for elements in data:
            if time == data[elements].timeEnd:
                listOfActivities.append(data[elements])

        return listOfActivities

    def search_activity_by_description(self, givenDescription):
        data = self.__repository.data
        listOfActivities = []
        givenDescription = givenDescription.strip(",. ")
        for elements in data:
            if givenDescription.lower() in data[elements].description.lower():
                listOfActivities.append(data[elements])

        return listOfActivities

    def activities_for_a_given_date(self, givenYear,givenMonth,givenDay):
        listOfActivties = self.search_activity_by_date(givenYear,givenMonth,givenDay)
        listOfActivties = ArrayOperations.gnomeSort(listOfActivties, time_start_compare)
        return listOfActivties

    def activities_for_a_given_person(self,givenID):
        data = self.__repository.data
        listOfActivities = []
        for elements in data:
            if givenID in data[elements].person_id:
                listOfActivities.append(data[elements])

        return listOfActivities

    def sort_activities_by_date(self):
        data = self.__repository.data
        listOfActivities = []
        for elements in data:
            listOfActivities.append(data[elements])

        # for i in range (0,len(listOfActivities)-1):
        #     for j in range (i+1, len(listOfActivities)):
        #         if(listOfActivities[i].date > listOfActivities[j].date):
        #             helpingList = listOfActivities[i]
        #             listOfActivities[i] = listOfActivities[j]
        #             listOfActivities[j] = helpingList

        listOfActivities = ArrayOperations.gnomeSort(listOfActivities,date_compare)
        return listOfActivities
    #============================================

    def days_with_atleast_1_activity(self):
        listOfActivities = self.sort_activities_by_date()
        listOfDates = []
        for i in range(0, len(listOfActivities)-1):
            if(listOfActivities[i].date != listOfActivities[i+1].date):
                listOfDates.append(listOfActivities[i].date)
        if listOfActivities[-1].date not in listOfDates:
            listOfDates.append(listOfActivities[-1].date)

        return listOfDates

    def statistic_days_least_free_time(self):
        listOfDatesWhichHaveAtleast1Activity = self.days_with_atleast_1_activity()
        listWithAllFinalData = []
        for i in range(0,len(listOfDatesWhichHaveAtleast1Activity)): #take all dates 1 by 1 and make the free intervals
            freeTimeIntervalList = [] #list in which i store the intervals with free time
            allActivitiesInACertainDay = self.search_activity_by_date(listOfDatesWhichHaveAtleast1Activity[i].year,listOfDatesWhichHaveAtleast1Activity[i].month,listOfDatesWhichHaveAtleast1Activity[i].day) #get all the activities in
            #a certain day
            listOfActivityTimeInADay = [] #times in which there is an activity

            self.build_activity_time_list(allActivitiesInACertainDay, listOfActivityTimeInADay)
            self.arrange_list_by_starting_time_and_then_ending_time(listOfActivityTimeInADay)

            buildingList = []
            buildingList.append(datetime.time(0, 0))
            buildingList.append(listOfActivityTimeInADay[0][0])
            freeTimeIntervalList.append(buildingList[:]) #add the free time interval starting from 00 at night to the 1st activity in that day

            self.get_free_time_list_intervals(freeTimeIntervalList, listOfActivityTimeInADay)

            lastActivityFinalTime = datetime.time(0,0) #get the ending time of the activity that ends the last in that day
            for i3 in range(0,len(listOfActivityTimeInADay)):
                if listOfActivityTimeInADay[i3][1] > lastActivityFinalTime:
                    lastActivityFinalTime = listOfActivityTimeInADay[i3][1]

            # add in the free time interval the interval strating from the last activity ending time to 00 at night
            buildingList = []
            buildingList.append(lastActivityFinalTime)
            buildingList.append(datetime.time(23, 59,59))
            freeTimeIntervalList.append(buildingList)

            freeTimeIntervalList.append(listOfDatesWhichHaveAtleast1Activity[i])
            listWithAllFinalData.append(freeTimeIntervalList[:])

        freeTimeInHoursAndMinutesForEachActivityDay = self.get_free_time_in_a_day(listWithAllFinalData)

        self.arrange_the_list_based_on_how_much_free_time(freeTimeInHoursAndMinutesForEachActivityDay,listWithAllFinalData)

        return listWithAllFinalData,freeTimeInHoursAndMinutesForEachActivityDay

    def arrange_the_list_based_on_how_much_free_time(self, freeTimeInHoursAndMinutesForEachActivityDay,listWithAllFinalData):
        for i in range(0,
                       len(listWithAllFinalData) - 1):  # ordonate the activities based on how much free time is in that activity day, ascending from lowest time to most time
            for j in range(i + 1, len(listWithAllFinalData)):
                if freeTimeInHoursAndMinutesForEachActivityDay[i] > freeTimeInHoursAndMinutesForEachActivityDay[j]:
                    help = freeTimeInHoursAndMinutesForEachActivityDay[i]
                    freeTimeInHoursAndMinutesForEachActivityDay[i] = freeTimeInHoursAndMinutesForEachActivityDay[j]
                    freeTimeInHoursAndMinutesForEachActivityDay[j] = help
                    help = listWithAllFinalData[i]
                    listWithAllFinalData[i] = listWithAllFinalData[j]
                    listWithAllFinalData[j] = help

    def get_free_time_in_a_day(self, listWithAllFinalData):
        date = datetime.date(1, 1, 1)
        freeTimeInHoursAndMinutesForEachActivityDay = []
        for i in range(0, len(listWithAllFinalData)):  # calculate the free time in each activity day
            freeTime = datetime.timedelta(seconds=0)
            for j in range(0, len(listWithAllFinalData[i]) - 1):
                datetime1 = datetime.datetime.combine(date, listWithAllFinalData[i][j][0])
                datetime2 = datetime.datetime.combine(date, listWithAllFinalData[i][j][1])
                freeTimeInterval = datetime2 - datetime1
                freeTime = freeTime + freeTimeInterval
            freeTimeInHoursAndMinutesForEachActivityDay.append(freeTime)
        return freeTimeInHoursAndMinutesForEachActivityDay

    def get_free_time_list_intervals(self, freeTimeIntervalList, listOfActivityTimeInADay):
        for i2 in range(0, len(listOfActivityTimeInADay) - 1):  # algorith which gets all the "free time intervals"
            date = datetime.date(1, 1, 1)
            datetime1 = datetime.datetime.combine(date, listOfActivityTimeInADay[i2 + 1][0])
            datetime2 = datetime.datetime.combine(date, listOfActivityTimeInADay[i2][1])
            if (datetime1 - datetime2 < datetime.timedelta(seconds=0)):
                pass
            else:
                buildingList = []
                buildingList.append(listOfActivityTimeInADay[i2][1])
                buildingList.append(listOfActivityTimeInADay[i2 + 1][0])
                freeTimeIntervalList.append(buildingList[:])

    def arrange_list_by_starting_time_and_then_ending_time(self, listOfActivityTimeInADay):
        for i1 in range(0,len(listOfActivityTimeInADay) - 1):  # arrange the list of activity time in ascending order based on starting time, and then after ending time
            for j1 in range(i1 + 1, len(listOfActivityTimeInADay)):
                if listOfActivityTimeInADay[i1][0] > listOfActivityTimeInADay[j1][0] or listOfActivityTimeInADay[i1][
                    0] == listOfActivityTimeInADay[j1][0] and listOfActivityTimeInADay[i1][1] > \
                        listOfActivityTimeInADay[j1][1]:
                    helpingList = listOfActivityTimeInADay[i1][:]
                    listOfActivityTimeInADay[i1] = listOfActivityTimeInADay[j1][:]
                    listOfActivityTimeInADay[j1] = helpingList[:]

    def build_activity_time_list(self, allActivitiesInACertainDay, listOfActivityTimeInADay):
        for j in range(0,len(allActivitiesInACertainDay)):  # build the list with all the activity times ex : [[(16,30),(18,00)],[(19,00),(20,30)]]
            buildingList = []  # used to build a list in a list
            buildingList.append(allActivitiesInACertainDay[j].timeStart)
            buildingList.append(allActivitiesInACertainDay[j].timeEnd)
            listOfActivityTimeInADay.append(buildingList[:])


    def get_activities_year_higher_2022(self):
        data = self.__repository.data
        listOfActivities = []
        for elements in data:
                listOfActivities.append(data[elements])

        listOfActivities = ArrayOperations.selfFilter(listOfActivities,year_higher_2022_function_filter)
        return  listOfActivities