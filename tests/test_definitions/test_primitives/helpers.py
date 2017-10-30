
def get_valid_primitive_data(primitive):
    data = None
    if {float, str, int}.intersection(set(primitive.__bases__)):
        try:
            data = primitive.example
        except AttributeError:
            try:
                data = next(iter(primitive.values))
            except AttributeError:
                if float in primitive.__bases__:
                    data = '14.0'
                elif int in primitive.__bases__:
                    data = '12345567'
                else:
                    data = 'TEST_DATA'
    else:
        data = 1
    return data
