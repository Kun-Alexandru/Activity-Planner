from src.ui.ui import *
from src.settings.settings import *

person_repository,activity_repository = Settings().get_repositories()
activity_service = ActivityService(activity_repository)
person_service = PersonService(person_repository)

ui = UI(person_service, activity_service)

ui.start()