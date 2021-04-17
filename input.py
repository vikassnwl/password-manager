def required(label):
    input_ = input(label)
    while not input_:
        input_ = input(label)
    return input_
