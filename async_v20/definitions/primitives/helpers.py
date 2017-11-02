def domain_check(value, example=None, possible_values=None):

    if example:
        try:
            assert len(example) == len(value)
        except (AssertionError, TypeError):
            msg = f'{value} does not match length of example {example}'
            raise ValueError(msg)

    if possible_values:
        try:
            assert value in possible_values
        except AssertionError:
            possible_values = ', '.join(possible_values)
            msg = f'{value} must be in {possible_values}. Possible values are {possible_values}'
            raise ValueError(msg)

    return True