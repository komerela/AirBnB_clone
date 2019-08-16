#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import models


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        """
        new_dic = {}
        if cls is None:
            return self.__objects

        for key, value in self.objects.item():
            if value.__class__ == cls:
                new_dic[key] = value
        return new_dic

    def new(self, obj):
        """add the object to the current session by setting obj with obj class
        """
        key = str(obj.__class__.name__) + "." + str(obj.id)
        value_dic = obj
        self.__objects[key] = value_dic

    def save(self):
        """serializes the object_attr to JSON file
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as fd:
            json.dump(my_dict, fd)

    def reload(self):
        """deserialize the json file path to objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
            delete obj from __objects from File storage schema
        """
        dict = FileStorage.__objects
        if obj is not None and obj in dict.values():
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del dict[key]
            self.save()
        else:
            return

    def close(self):
        """
        Deserialize Json file to obj
        """
        self.reload()
