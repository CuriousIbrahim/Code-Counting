import sys


def parse(argv):

    argv = argv[1:]

    result = {
        'dir': None,
        'ignore': [],
        'only': []
    }

    buffer = []

    for v in argv:

        if '-d' == v:
            temp = ''.join(buffer)
            result['dir'] = temp
            buffer.clear()

        elif '-i' == v:
            result['ignore'] += buffer
            buffer.clear()

        elif '-o' == v:
            result['only'] += buffer
            buffer.clear()

        else:
            buffer.append(v)

    return result



