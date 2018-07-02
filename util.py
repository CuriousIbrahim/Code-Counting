

def get_file_extension(file):
    file = file.split('.')

    extension = '.' + file[len(file)-1]

    return extension
