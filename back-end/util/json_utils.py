import weakref
from datetime import date
from json import JSONEncoder


class AppJsonEncoder(JSONEncoder):
    # You may need to adapt this class to deal with different type of objects
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)

        except TypeError:
            pass
        else:
            return list(iterable)
        # default json encoding using the __dict__
        return obj.__dict__
