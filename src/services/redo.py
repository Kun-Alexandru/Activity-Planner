from dataclasses import dataclass
from src.services.personService import *

class nothingToRedoException(Exception):
    pass

class IDinRepoAlreadyDueToUndoRedo(Exception):
    pass

@dataclass
class RedoOperation:
    target_object: object
    handler: object
    arguments: tuple

class RedoManager:
    __redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *arguments):
        RedoManager.__redo_operations.append(RedoOperation(target_object, handler, arguments))

    @staticmethod
    def redo(index):
        try:
            redo_operation = RedoManager.__redo_operations[index]
            redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)
        except RepositoryException as re:
            raise IDinRepoAlreadyDueToUndoRedo("")