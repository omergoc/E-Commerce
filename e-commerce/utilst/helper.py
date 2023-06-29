from bson import ObjectId


def object_id_handler(o):
    if isinstance(o, ObjectId):
        return str(o)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(o).__name__)
