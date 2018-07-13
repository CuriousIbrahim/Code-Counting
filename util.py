

def get_file_extension(file):
    file = file.split('.')

    extension = '.' + file[len(file)-1]

    return extension


def count_lines_of_code(file):
    count = 0

    with open(file, encoding='ISO-8859-1') as f:
        for line in f:
            print(line)
            count += 1

    return count