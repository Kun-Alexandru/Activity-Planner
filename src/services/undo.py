from dataclasses import dataclass
from src.services.personService import RepositoryException


class nothingToUndoException(Exception):
    pass

class IDinRepoAlreadyDueToUndoRedo(Exception):
    pass

@dataclass
class UndoOperation:
    target_object: object
    handler: object
    arguments: tuple

class UndoManager:
    __undo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *arguments):
        UndoManager.__undo_operations.append(UndoOperation(target_object,handler,arguments))

    @staticmethod
    def undo(index):
        try:
            if(len(UndoManager.__undo_operations)>0):
                undo_operation = UndoManager.__undo_operations[index]
                undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)
            else:
                raise nothingToUndoException("Nothing to Undo")
        except RepositoryException as re:
            raise IDinRepoAlreadyDueToUndoRedo("")

