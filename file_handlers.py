def file_writer(file_name, text):
    f = open(f"{file_name}", "a")
    result = f.write(text)
    f.close()
    return result

def file_reader(file_name):
    f = open(f'{file_name}', 'r')
    result = f.read()
    return result
