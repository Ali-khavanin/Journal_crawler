import pickle


def save_obj(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def get_key(dict_obj: dict, val):
    for key, value in dict_obj.items():
        if val == value:
            return key
