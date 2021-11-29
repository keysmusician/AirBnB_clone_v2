#!/usr/bin/python3
"""File storage engine class definition."""
import json


class FileStorage:
    """Manage disk storage of HBnB models in JSON format."""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of models currently in storage."""
        if cls is None:
            return FileStorage.__objects
        new_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                new_dict[key] = value
        # Using dict comprehension
        # {key: value for key, value in self.objects.items()
        #  if isinstance(value, cls)}
        return new_dict

    def close(self):
        self.reload()

    def delete(self, obj=None):
        """Delete `obj` from `__objects`."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()

    def new(self, obj):
        """Add a new object to storage dictionary."""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def reload(self):
        """Load storage dictionary from a file."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def save(self):
        """Write storage dictionary to a file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
