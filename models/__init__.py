#!/usr/bin/python3
"""
Determines which storage engine will be used (database or file storage).
The storage engine can be selected from the environment variable
`HBNB_TYPE_STORAGE`.

The file storage engine works by converting instances to/from JSON strings and
reading/writing them to/from a file.
For details, see "./engine/file_Storage.py".

Alternatively, if database storage engine is selected, it connects to a
database server and submits queries to manage instances.
For details, see "./engine/db_storage.py".

"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
