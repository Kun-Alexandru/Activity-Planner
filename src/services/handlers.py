from enum import Enum
from src.domain.person import *
from src.domain.activity import *

def add_person_handler(personService, person_id, activityService):
    personService.remove_person_by_id(person_id)
    activityService.remove_person_id_from_list_of_activities(person_id)

def delete_person_handler(personService, person_id, name, phoneNumber,listOfActivityToAddPersonBack,activityService):
    personService.add_person(Person(person_id,name,phoneNumber))
    activityService.add_person_to_activities(person_id, listOfActivityToAddPersonBack)

def update_person_handler(personService, person_id, name, phoneNumber):
    personService.update_person_by_id(person_id,name,phoneNumber)

def add_activity_handler(activityService, activity_id):
    activityService.remove_activity_by_id(activity_id)

def delete_activity_handler(activityService, activity_id,date,timeStart,timeEnd,givenDescription,listOfPersons):
    activityService.add_activity(Activity(activity_id,date,timeStart,timeEnd,givenDescription,listOfPersons))


def update_activity_handler(activityService, activity_id,date,timeStart,timeEnd,givenDescription,listOfPersons):
    activityService.update_activity_by_id(activity_id,date,timeStart,timeEnd,givenDescription,listOfPersons)

def add_person_id_to_activity_handler(activityService, givenID, listOfActivityToAddPersonBack):
    activityService.add_person_to_activities(givenID,listOfActivityToAddPersonBack)

class UndoHandler(Enum):
    ADD_PERSON = add_person_handler
    DELETE_PERSON = delete_person_handler
    UPDATE_PERSON = update_person_handler
    ADD_PERSON_TO_ACTIVITIES = add_person_id_to_activity_handler

    ADD_ACTIVITY = add_activity_handler
    DELETE_ACTIVITY = delete_activity_handler
    UPDATE_ACTIVITY = update_activity_handler

class RedoHandler(Enum):
    ADD_PERSON = delete_person_handler
    DELETE_PERSON = add_person_handler
    UPDATE_PERSON = update_person_handler

    ADD_ACTIVITY = delete_activity_handler
    DELETE_ACTIVITY = add_activity_handler
    UPDATE_ACTIVITY = update_activity_handler

