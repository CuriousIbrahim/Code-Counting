import sys


def parse(argv):

    argv = argv[1:]

    result = {
        'dir': None,
        'ignore': [],
        'only': []
    }

    buffer = []

    for i, v in enumerate(argv):

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

        if i == len(argv) - 1:
            temp = ''.join(buffer)
            result['dir'] = temp

    return result



