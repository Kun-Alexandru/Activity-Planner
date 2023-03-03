import datetime
import pickle
import os
from src.domain.activity import *
from src.IterrableDS.sort_filter_iterable_data import *


class RepositoryException(Exception):
    pass

class Repository_activity():
    def __init__(self):
        self._data = ItterableDataStructure()

    @property
    def data(self):
        return self._data

    def add(self, entity):
        """
        Function that adds a new activity in the repository
        :param entity: activity that is added in the repository
        :return:
        """
        if entity.activity_id in self._data:
            raise RepositoryException("Activity with ID " + str(entity.activity_id) + " already in repo")
        else:
            self._data[entity.activity_id] = entity
            return True

    def __getitem__(self, id):
        """
        A function that returns the activty whith a certain id
        :param id: given id
        :return: the activity with the given id (if there is one)
        """
        return self._data[id]

    def remove_by_id(self, givenID):
        """
        A function that removes the activity with the given id
        :param givenID: given id
        :return:
        """
        if givenID in self._data:
            self._data.pop(givenID)
            return True
        else:
            return False

    def add_person_to_activities(self,givenPersonID, listOfActvityID):

        for i in range(0, len(listOfActvityID)):
            if givenPersonID not in self._data[listOfActvityID[i]].person_id:
                self._data[listOfActvityID[i]].person_id.append(givenPersonID)

    def remove_person_id_from_list_of_participants(self, givenID):
        """
        A function that removes the person with the given id from ALL the activities (used when we delete a person from the repository, because if he is deleted he cannot take part in any activites)
        :param givenID: given id of the person that we want to remove
        :return:
        """
        for elements in self._data:
            if givenID in self._data[elements].person_id:
                self._data[elements].person_id.remove(givenID)

    def get_all_activities(self):
        """
        returns all the activities as a list
        :return:
        """
        return list(self._data.values())


    def update_repo(self, givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID):
        """
        A function that updates the activity with a given id, if there is one
        :param givenID: given id of activity in order to update it
        :param givenDate: new date of the activity
        :param givenTimeStart: new time start of the activity
        :param givenTimeEnd: new time end of the activity
        :param givenDescription: new description of the activity
        :param givenPersonID: new list of ppl that take part in the activity
        :return:
        """
        if givenID in self._data:
            self._data[givenID].date = givenDate
            self._data[givenID].timeStart = givenTimeStart
            self._data[givenID].timeEnd = givenTimeEnd
            self._data[givenID].description = givenDescription
            self._data[givenID].person_id = givenPersonID
        else:
            raise RepositoryException("Activity with ID " + str(givenID) + " is not in repo")


class ActivityTextFileRepository(Repository_activity):
    def __init__(self, inputFileName):
        super().__init__()
        self._save_file_name = "files/activity.txt"
        self._input_file_name = inputFileName
        self._load_file()

    def _load_file(self):
        if (self._input_file_name != ""):
            file = open(self._input_file_name, "rt")
            for line in file.readlines():
                id,Date,TimeStart,TimeEnd,Description,PersonList = line.split(",")
                id = int(id)
                Date = Date.split(".")
                usableDate = datetime.date(int(Date[0]),int(Date[1]),int(Date[2]))
                TimeStart = TimeStart.split(".")
                usableTimeStart = datetime.time(int(TimeStart[0]),int(TimeStart[1]))
                TimeEnd = TimeEnd.split(".")
                usableTimeEnd = datetime.time(int(TimeEnd[0]),int(TimeEnd[1]))
                PersonList = PersonList.split(".")
                usablePersonList = []
                for i in range(0,len(PersonList)-1):
                    usablePersonList.append(int(PersonList[i]))
                PersonList[-1].strip("\n")
                usablePersonList.append(int(PersonList[-1]))


                activity = Activity(id, usableDate, usableTimeStart, usableTimeEnd, Description, usablePersonList)
                self.add(activity)
            file.close()

    def _save_file(self):
        file = open(self._save_file_name, "wt")
        for activity in self._data.values():
            file.write(str(activity.activity_id) + "," + str(activity.date.year) + "." + str(activity.date.month) + "." + str(activity.date.day) + "," + str(activity.timeStart.hour) + "." + str(activity.timeStart.minute) + "," + str(activity.timeEnd.hour) + "." + str(activity.timeEnd.minute) + "," + activity.description + ",")
            for i in range (0,len(activity.person_id)-1):
                file.write(str(activity.person_id[i]) + ".")
            file.write(str(activity.person_id[-1]))
            file.write("\n")


    def add(self, entity):
        super(ActivityTextFileRepository, self).add(entity)
        self._save_file()

    def remove_by_id(self, givenID):
        super(ActivityTextFileRepository,self).remove_by_id(givenID)
        self._save_file()

    def update_repo(self, givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID):
        super(ActivityTextFileRepository,self).update_repo(givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID)
        self._save_file()

    def remove_person_id_from_list_of_participants(self, givenID):
        super(ActivityTextFileRepository,self).remove_person_id_from_list_of_participants(givenID)
        self._save_file()

    def add_person_to_activities(self, givenPersonID, listOfActvityID):
        super(ActivityTextFileRepository,self).add_person_to_activities(givenPersonID,listOfActvityID)
        self._save_file()

def test_activity_text_file_repo():
    repo = ActivityTextFileRepository()
    repo.add_person_to_activities(100,[1,4])

class ActivityBinaryFileRepository(Repository_activity):
    def __init__(self,inputFileName):
        super().__init__()
        self._save_file_name = "files/activity.bin"
        self._input_file_name = inputFileName
        self._load_file()

    def _load_file(self):
        if (self._input_file_name != ""):
            if os.path.getsize(self._input_file_name) > 0:
                file = open(self._input_file_name, "rb")
                self._data = pickle.load(file)
                file.close()

    def _save_file(self):
        file = open(self._save_file_name, "wb")
        pickle.dump(self._data,file)
        file.close()

    def add(self, entity):
        super(ActivityBinaryFileRepository, self).add(entity)
        self._save_file()

    def remove_by_id(self, givenID):
        super(ActivityBinaryFileRepository,self).remove_by_id(givenID)
        self._save_file()

    def update_repo(self, givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID):
        super(ActivityBinaryFileRepository,self).update_repo(givenID, givenDate, givenTimeStart, givenTimeEnd, givenDescription, givenPersonID)
        self._save_file()

    def remove_person_id_from_list_of_participants(self, givenID):
        super(ActivityBinaryFileRepository,self).remove_person_id_from_list_of_participants(givenID)
        self._save_file()

    def add_person_to_activities(self, givenPersonID, listOfActvityID):
        super(ActivityBinaryFileRepository,self).add_person_to_activities(givenPersonID,listOfActvityID)
        self._save_file()

