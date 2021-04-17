def is_required(func):
    def wrapper(msg, required=True):
        input_ = func(msg)
        if required:
            while not input_:
                input_ = input(msg)
        return input_

    return wrapper


@is_required
def input_(msg):
    return input(msg)
