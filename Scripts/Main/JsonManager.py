import jsonpickle


def Serialize(object) -> str:
    return jsonpickle.encode(object)


def Deserialize(string: str) -> object:
    return jsonpickle.decode(string)
