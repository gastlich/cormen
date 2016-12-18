def print_inout(wrapped):
    def ret(*args):
        print('Input: {}{}'.format(wrapped.__name__, args))
        output = wrapped(*args)
        print('Output: {}\n'.format(output))
        return output

    return ret
