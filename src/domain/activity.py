import datetime

class Activity:
    """
    -activity_id, person_id - list, date, time, description
    """

    def __init__(self, _activity_id, date, timeStart, timeEnd, description, person_id):
        """
        Create a new activity
        :param _activity_id: activity id
        :param date: date date in which the activity takes place
        :param timeStart: the start time of the activity
        :param timeEnd: the ending time of the activity
        :param description: short description of activity
        :param person_id: list with the id of people that take part in the activity
        """
        self.__activity_id = _activity_id
        self.__date = date
        self.__timeStart = timeStart
        self.__timeEnd = timeEnd
        self.__description = description
        self.__person_id = person_id[:]

    def __str__(self):
        return 'Activity ID - {},  date - {}, timeStart - {}, timeEnd - {}, description - {}, participants - {}'.format(self.activity_id, self.date, self.timeStart, self.timeEnd, self.description,self.person_id)

    @property
    def activity_id(self):
        return self.__activity_id

    @property
    def date(self):
        return self.__date

    @property
    def timeStart(self):
        return self.__timeStart

    @property
    def timeEnd(self):
        return self.__timeEnd

    @property
    def description(self):
        return self.__description

    @property
    def person_id(self):
        return self.__person_id


    @person_id.setter
    def person_id(self, newParticipantsList):
        if(type(newParticipantsList) != list):
            raise ValueError("Person id should be type list")
        self.__person_id = newParticipantsList[:]

    @activity_id.setter
    def activity_id(self, newActivityID):
        if(type(newActivityID) != int):
            raise ValueError("Activity id should be int type")
        self.__activity_id = newActivityID

    @date.setter
    def date(self,newDate):
        if(type(newDate) != datetime.date):
            raise ValueError("Date type should be datetime.date type")
        self.__date = newDate

    @timeStart.setter
    def timeStart(self, newTime):
        if (type(newTime) != datetime.time):
            raise ValueError("Time type should be datetime.time type")
        self.__timeStart = newTime

    @timeEnd.setter
    def timeEnd(self, newTime):
        if (type(newTime) != datetime.time):
             raise ValueError("Time type should be datetime.time type")
        self.__timeEnd = newTime

    @description.setter
    def description(self,newDescription):
        if(type(newDescription) != str):
            raise ValueError("Description type should be str type")
        self.__description = newDescription

