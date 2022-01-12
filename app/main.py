def create_dict(*args):
    diction = {}
    value = 0
    for argument in args:
        if isinstance(argument, int) or isinstance(argument, float)\
                or isinstance(argument, str) or isinstance(argument, bool)\
                or argument is None or callable(argument):
            diction[argument] = value
            value += 1
        elif isinstance(argument, tuple):
            statment = 0
            for arg in argument:
                if isinstance(arg, list) or isinstance(arg, set)\
                        or isinstance(arg, dict):
                    statment += 1
                else:
                    pass
            if statment == 0:
                diction[argument] = value
                value += 1
            else:
                print(f"Cannot add {argument} to the dict!")
                value += 1
        else:
            value += 1
            print(f"Cannot add {argument} to the dict!")

    return diction
