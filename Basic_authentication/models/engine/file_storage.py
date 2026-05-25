#!/usr/bin/env python3
"""File-based storage engine for the API users."""

import json
import os


class FileStorage:
    """Serialize and deserialize model instances to a JSON file."""

    __file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "file.json")
    __objects = {}

    def all(self, cls=None):
        """Return all stored objects, optionally filtered by class."""

        if cls is None:
            return self.__objects
        result = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                result[key] = obj
        return result

    def new(self, obj):
        """Register a new object in storage."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Persist all stored objects to disk."""

        serializable = {
            key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serializable, file)

    def reload(self):
        """Load objects from disk if the JSON file exists."""

        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception:
            return

        from models.user import User

        classes = {"User": User}
        self.__objects = {}
        for key, value in data.items():
            class_name = value.get("__class__")
            model_class = classes.get(class_name)
            if model_class is not None:
                self.__objects[key] = model_class(**value)

    def search(self, cls, **kwargs):
        """Return the list of objects that match the provided filters."""

        results = []
        for obj in self.all(cls).values():
            if all(getattr(obj, key, None) == value
                   for key, value in kwargs.items()):
                results.append(obj)
        return results


storage = FileStorage()
storage.reload()
