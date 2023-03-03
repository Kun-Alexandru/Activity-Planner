from src.services.activityService import *
from src.services.personService import *
from random import *
from src.services.handlers import *
from src.services.undo import *
from src.services.redo import *
import os

class UI:
    def __init__(self, personService, activityService):
        self.__person_service = personService
        self.__activity_service = activityService
    def __add_person(self):
        self.__person_service.add_person(Person(100,"Vlad","0745406005"))
        self.__person_service.add_person(Person(200,"Ion","0745406005"))

    def __add_activity(self):
        self.__activity_service.add_activity(Activity(1, datetime.date(2020, 7, 5), datetime.time(16, 15, 00), datetime.time(18, 00, 00), "Fotbal",[100, 200]))
        self.__activity_service.add_activity(Activity(2, datetime.date(2020, 7, 5), datetime.time(18, 00, 00), datetime.time(20, 00, 00), "Baschet", [100]))

    def __print_all_activities(self):
        listOfActivities = self.__activity_service.get_all_activities()
        self.__print_list(listOfActivities)

    def __print_all_people(self):
        listOfPeople = self.__person_service.get_all_people()
        self.__print_list(listOfPeople)

    def __print_list(self, listOfPeople):
        for element in listOfPeople:
            print(element)



    def generate_starting_people(self):
        self.__person_service.add_person(Person(1,"Me","0777777777"))
        listOfNames = ["Ana","Joe","Daniel","Oana","Tudor","Ionel","Mircea","Alex","Ioana","Dana","George","Radu","Cristina","Liam","Olivia","Yoo","Elijah"]
        listOfPhoneNumbers = ["0745406005","0711223344","0722334455","0744556677","0712121212","0713131313","0714141414","0715151515","0731313131","0788888888","0799999999","0761616161","0763735331","0761215321","0721978123","0781513171"]
        nameAppearences = []
        phoneNumberApperences = []
        id = 2
        stillRunning = True
        while stillRunning == True:
            nameIndex = randint(0,15)
            phoneNumberIndex = randint(0,15)
            if nameIndex not in nameAppearences and phoneNumberIndex not in phoneNumberApperences:
                nameAppearences.append(int(nameIndex))
                phoneNumberApperences.append(int(phoneNumberIndex))
                self.__person_service.add_person(Person(id,listOfNames[nameIndex],listOfPhoneNumbers[phoneNumberIndex]))
                id += 1
            if id == 18:
                stillRunning = False

    def generate_starting_activities(self):
        stillRunning = True
        id = 1
        while stillRunning == True:
            yearDate = randint(2022,2024)
            monthDate = randint(1,12)
            dayDate = randint(1,27)
            date = datetime.date(yearDate,monthDate,dayDate)

            hourTimeStart = randint(8,20)
            minuteTimeStart = randint(0,29)
            timeStart = datetime.time(hourTimeStart,minuteTimeStart)

            hourTimeEnd = hourTimeStart+1
            minuteTimeEnd = minuteTimeStart+30
            timeEnd = datetime.time(hourTimeEnd,minuteTimeEnd)

            description = "Games"

            listOfPeople = []
            numberOfPeople = randint(1,8)
            apperingPeople = []
            if self.__activity_service.is_already_in_a_specific_time_frame(1, date, timeStart,timeEnd, id) == True:
                listOfPeople.append(1)

            for i in range(0,numberOfPeople+1):
                idParticipant = randint(2,17)
                if idParticipant not in apperingPeople:
                    apperingPeople.append(idParticipant)
                    if self.__activity_service.is_already_in_a_specific_time_frame(idParticipant, date, timeStart,timeEnd, id) == True:
                        listOfPeople.append(int(idParticipant))

            self.__activity_service.add_activity(Activity(id, date, timeStart, timeEnd, description, listOfPeople))
            id+=1
            if id==5:
                stillRunning = False


    def print_menu(self):
        print("1. Add a new person")
        print("2. Add a new activity")
        print("3. Delete a person by id")
        print("4. Delete an activity by id")
        print("5. List the people")
        print("6. List the activities")
        print("7. Update a person by id")
        print("8. Update an activity by id")
        print("9. Search people/activities")
        print("10.All activties in a given date")
        print("11.All the activities with a certain person")
        print("12.All the days with free time in intervals, in order of how much free time is in the day")
        print("Undo")
        print("Redo")

        print("Exit")
        print("\n")

    def print_second_menu(self):
        print("1. Search people by name")
        print("2. Search people by phone number")
        print("3. Search activities by date")
        print("4. Search activities by time start")
        print("5. Search activities by time end")
        print("6. Search activities by description")
        print("7. Back")
        print("Exit")
        print("")


    def start(self):
        #self.generate_starting_people()
        #self.generate_starting_activities()
        numberOfPossibleRedos = 0
        numberOfPossibleUndos = -1
        isRunning = True
        while isRunning == True:
            self.print_menu()
            command = input()
            if command == "1":
                try:
                    try:
                        personID = int(input("Give the id"))
                        personName = input("Give the name")
                        phone_number = input("Give the phone number")
                        self.__person_service.add_person(Person(personID,personName,phone_number))
                        UndoManager.register_operation(self.__person_service, UndoHandler.ADD_PERSON, personID,self.__activity_service)
                        RedoManager.register_operation(self.__person_service,RedoHandler.ADD_PERSON,personID, personName,phone_number,[],self.__activity_service)
                        numberOfPossibleUndos += 1
                    except ValueError as ve:
                        print(ve)
                except RepositoryException as re:
                    print("")
                    print("ID given is already in repository")
                    print("")
            elif command =="2":
                try:
                    try:
                        activityID = int(input("Give activity id"))

                        yearDate = int(input("Give the year of the activity"))
                        monthDate = int(input("Give the month of the activity"))
                        dayDate = int(input("Give the day of the activity"))
                        date = datetime.date(yearDate,monthDate,dayDate)

                        hourTimeStart = int(input("Give the starting hour of the activity (0-24)"))
                        minuteTimeStart = int(input("Give the starting minute of the activity (0-59)"))
                        timeStart = datetime.time(hourTimeStart,minuteTimeStart)

                        hourTimeEnd = int(input("Give the ending hour of the activity (0-24)"))
                        minuteTimeEnd = int(input("Give the ending minute of the activity (0-59)"))
                        timeEnd = datetime.time(hourTimeEnd, minuteTimeEnd)

                        description = input("Give a description of the activity")
                        listOfPersons = []
                        print("Choose which people (by id) will take part of the activity, stops when 0 is read")
                        elementRead = ""
                        while elementRead != "0":
                            elementRead = input()
                            if int(elementRead) != 0:
                                if self.__person_service.is_an_id_in_repo(int(elementRead)) == True:
                                    if int(elementRead) not in listOfPersons:
                                        if  self.__activity_service.is_already_in_a_specific_time_frame(elementRead,date,timeStart,timeEnd,activityID) == True:
                                            listOfPersons.append(int(elementRead))
                                        else :
                                            print("The person with the given id is not available")
                                    else:
                                        print("Id already in the current activity")
                                else:
                                    print("Given id is not in the list of people")
                        if(date.today()<date):

                            self.__activity_service.add_activity(Activity(activityID,date,timeStart,timeEnd,description,listOfPersons))
                            UndoManager.register_operation(self.__activity_service, UndoHandler.ADD_ACTIVITY, activityID)
                            RedoManager.register_operation(self.__activity_service,RedoHandler.ADD_ACTIVITY,activityID,date,timeStart,timeEnd,description,listOfPersons)
                            numberOfPossibleUndos += 1
                        else:
                            print("This date has already passed")
                    except ValueError as ve:
                        print(ve)
                except RepositoryException as re:
                    print("")
                    print("ID given is already in repository")
                    print("")
            elif command == "3":
                try:
                    givenID = int(input("Give person id"))
                    listOfPeople = self.__person_service.get_all_people()
                    for i in range(0,len(listOfPeople)):
                        if listOfPeople[i].person_id == givenID:
                            if givenID != 1:
                                listOfActivities = self.__activity_service.get_all_activities()

                                listOfActivityToAddPersonBack = []

                                for i in range(0, len(listOfActivities)):
                                    if givenID in listOfActivities[i].person_id:
                                        listOfActivityToAddPersonBack.append(listOfActivities[i].activity_id)

                                listOfPeople = self.__person_service.get_all_people()
                                for i in range(0, len(listOfPeople)):
                                    if listOfPeople[i].person_id == givenID:
                                        UndoManager.register_operation(self.__person_service,UndoHandler.DELETE_PERSON,givenID,listOfPeople[i].name,listOfPeople[i].phone_number,listOfActivityToAddPersonBack,self.__activity_service)

                                RedoManager.register_operation(self.__person_service,RedoHandler.DELETE_PERSON,givenID,self.__activity_service)


                                self.__activity_service.remove_person_id_from_list_of_activities(givenID)
                                self.__person_service.remove_person_by_id(givenID)
                                numberOfPossibleUndos += 1
                            else:
                                print("You cannot remove yourself from the list")
                except ValueError as ve:
                    print(ve)

            elif command == "4":
                try:
                    listOfActivities = self.__activity_service.get_all_activities()
                    givenID = int(input("Give activity id"))
                    for i in range(0, len(listOfActivities)):
                        if listOfActivities[i].activity_id == givenID:
                            listOfActivities = self.__activity_service.get_all_activities()
                            for i in range(0,len(listOfActivities)):
                                if listOfActivities[i].activity_id == givenID:
                                    UndoManager.register_operation(self.__activity_service,UndoHandler.DELETE_ACTIVITY,givenID\
                                    ,listOfActivities[i].date,listOfActivities[i].timeStart,listOfActivities[i].timeEnd,listOfActivities[i].description,listOfActivities[i].person_id)
                            RedoManager.register_operation(self.__activity_service,RedoHandler.DELETE_ACTIVITY, givenID)
                            self.__activity_service.remove_activity_by_id(givenID)
                            numberOfPossibleUndos += 1
                except ValueError as ve:
                    print(ve)

            elif command == "5":
                self.__print_all_people()

            elif command == "6":
                self.__print_all_activities()

            elif command == "7":
                try:
                    try:
                        personID = int(input("Give the id"))
                        listOfPeople = self.__person_service.get_all_people()
                        for i in range(0, len(listOfPeople)):
                            if listOfPeople[i].person_id == personID:
                                UndoManager.register_operation(self.__person_service,UndoHandler.UPDATE_PERSON,personID,listOfPeople[i].name,listOfPeople[i].phone_number)
                        personName = input("Give the name")
                        phone_number = input("Give the phone number")
                        RedoManager.register_operation(self.__person_service,RedoHandler.UPDATE_PERSON,personID,personName,phone_number)
                        self.__person_service.update_person_by_id(personID,personName,phone_number)
                        numberOfPossibleUndos += 1
                    except ValueError as ve:
                        print(ve)
                except RepositoryException as re:
                    print("")
                    print("ID given is not in repository")
                    print("")

            elif command == "8":
                try:
                    activityID = int(input("Give activity id"))

                    yearDate = int(input("Give the year of the activity"))
                    monthDate = int(input("Give the month of the activity"))
                    dayDate = int(input("Give the day of the activity"))
                    date = datetime.date(yearDate, monthDate, dayDate)

                    hourTimeStart = int(input("Give the starting hour of the activity (0-24)"))
                    minuteTimeStart = int(input("Give the starting minute of the activity (0-59)"))
                    timeStart = datetime.time(hourTimeStart, minuteTimeStart)

                    hourTimeEnd = int(input("Give the ending hour of the activity (0-24)"))
                    minuteTimeEnd = int(input("Give the ending minute of the activity (0-59)"))
                    timeEnd = datetime.time(hourTimeEnd, minuteTimeEnd)

                    description = input("Give a description of the activity")
                    listOfPersons = []
                    print("Choose which people (by id) will take part of the activity, stop when 0 is read")
                    elementRead = ""
                    while elementRead != "0":
                        elementRead = input()
                        if int(elementRead) != 0:
                            if self.__person_service.is_an_id_in_repo(int(elementRead)) == True:
                                if int(elementRead) not in listOfPersons:
                                    if  self.__activity_service.is_already_in_a_specific_time_frame(elementRead,date,timeStart,timeEnd,activityID) == True:
                                        listOfPersons.append(int(elementRead))
                                    else:
                                        print("The person with the given id is not available")
                                else:
                                    print("Id already in the current activity")
                            else:
                                print("Given id is not in the list of people")
                    try:
                        if(date.today()<date):
                                try:
                                    listOfActivities = self.__activity_service.get_all_activities()
                                    for i in range(0, len(listOfActivities)):
                                        if listOfActivities[i].activity_id == activityID:
                                            UndoManager.register_operation(self.__activity_service,
                                                                           UndoHandler.UPDATE_ACTIVITY, activityID, listOfActivities[i].date,listOfActivities[i].timeStart,\
                                                                           listOfActivities[i].timeEnd,listOfActivities[i].description,listOfActivities[i].person_id)
                                    self.__activity_service.update_activity_by_id(activityID,date,timeStart,timeEnd,description,listOfPersons)
                                    RedoManager.register_operation(self.__activity_service,RedoHandler.UPDATE_ACTIVITY,activityID,date,timeStart,timeEnd,description,listOfPersons)
                                    numberOfPossibleUndos += 1
                                except ServiceException as se:
                                    print(se)
                        else:
                            print("This date has already passed")
                            print("")

                    except RepositoryException as re:
                        print("")
                        print("ID given is NOT in the repository")
                        print("")
                except ValueError as ve:
                    print(ve)

            elif command.lower() == "Exit".lower():
                isRunning = False

            elif command == "9":
                self.print_second_menu()
                secondCommand = input()
                if secondCommand == "1":
                    givenName = input("Give a name")
                    listOfPeople = self.__person_service.search_people_by_name(givenName)
                    for index in range(0,len(listOfPeople)):
                        print(listOfPeople[index])
                elif secondCommand == "2":
                    givenPhoneNumber = input("Give a phone number")
                    listOfPeople = self.__person_service.search_people_by_phone_number(givenPhoneNumber)
                    for index in range(0, len(listOfPeople)):
                        print(listOfPeople[index])

                elif secondCommand == "3":
                    try:
                        year = int(input("Give a year"))
                        month = int(input("Give a month"))
                        day = int(input("Give a day"))
                        listOfActivities = self.__activity_service.search_activity_by_date(year,month,day)
                        for index in range(0, len(listOfActivities)):
                            print(listOfActivities[index])
                    except ValueError as ve:
                        print(ve)

                elif secondCommand == "4":
                    try:
                        hour = int(input("Give a hour"))
                        minute = int(input("Give a minute"))
                        listOfActivities = self.__activity_service.search_activity_by_time_start(hour,minute)
                        for index in range(0, len(listOfActivities)):
                            print(listOfActivities[index])
                    except ValueError as ve:
                        print(ve)

                elif secondCommand == "5":
                    try:
                        hour = int(input("Give a hour"))
                        minute = int(input("Give a minute"))
                        listOfActivities = self.__activity_service.search_activity_by_time_end(hour, minute)
                        for index in range(0, len(listOfActivities)):
                            print(listOfActivities[index])
                    except ValueError as ve:
                        print(ve)


                elif secondCommand == "6":
                    description = input("Give a description")
                    listOfActivities = self.__activity_service.search_activity_by_description(description)
                    for index in range(0, len(listOfActivities)):
                        print(listOfActivities[index])

                elif secondCommand == "7":
                    pass

                elif secondCommand.lower() == "Exit".lower():
                    isRunning = False

            elif command == "10":
                try:
                    year = int(input("Give a year"))
                    month = int(input("Give a month"))
                    day = int(input("Give a day"))
                    listOfActivities = self.__activity_service.activities_for_a_given_date(year,month,day)
                    for index in range(0, len(listOfActivities)):
                        print(listOfActivities[index])
                except ValueError as ve:
                    print(ve)

            elif command == "11":
                try:
                    givenID = int(input("Give an id"))
                    listOfActivities = self.__activity_service.activities_for_a_given_person(givenID)
                    for index in range(0, len(listOfActivities)):
                        print(listOfActivities[index])
                except ValueError as ve:
                    print(ve)

            elif command == "12":
                finalList,values = self.__activity_service.statistic_days_least_free_time()
                for i in range (0,len(finalList)):
                    print(finalList[i][-1], end = " ")
                    for j in range(0,len(finalList[i])-1):
                        print("(" + str(finalList[i][j][0]) + "," + str(finalList[i][j][1]) + ")", end = " ")
                    print("| Free time in the day : " + str(values[i]))
                    print("")
                print("")
            elif command == "Undo":
                try:
                    if numberOfPossibleUndos >= 0:
                        UndoManager.undo(numberOfPossibleUndos)
                        numberOfPossibleUndos = numberOfPossibleUndos - 1
                        numberOfPossibleRedos += 1
                    else:
                        print("There's nothing to undo")
                except IDinRepoAlreadyDueToUndoRedo as notWorking:
                    print("Due to multiple undo/redo and then adding, the id is already in repo")

            elif command == "Redo":
                try:
                    if numberOfPossibleRedos > 0:
                        RedoManager.redo(-numberOfPossibleRedos)
                        numberOfPossibleRedos = numberOfPossibleRedos - 1
                        numberOfPossibleUndos = numberOfPossibleUndos + 1
                    else:
                        print("There's nothing to redo")
                except IDinRepoAlreadyDueToUndoRedo as notWorking:
                    print("Due to multiple undo/redo and then adding, the id is already in repo")

            elif command == "generate":
                self.generate_starting_people()
                self.generate_starting_activities()

            elif command == "a10Sort":
                listOfActivities = self.__activity_service.sort_activities_by_date()
                for index in range(0, len(listOfActivities)):
                    print(listOfActivities[index])

            elif command == "a10Filter":
                listOfActivities = self.__activity_service.get_activities_year_higher_2022()
                for index in range(0, len(listOfActivities)):
                    print(listOfActivities[index])