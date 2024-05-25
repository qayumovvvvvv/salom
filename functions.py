from file_handlers import file_reader

def file_count(file_name):
    result = file_reader(file_name=file_name)
    return len(result.split())

def biggest_word(file_name):
    result = file_reader(file_name=file_name)
    bigWord= ''
    for word in result.split():
        if len(word)> len(bigWord):
            bigWord = word
    return f" biggest word is {bigWord}. lenght is {len(bigWord)}"

def increase_num(data):
    number= 0
    for num in data:
        if num > number :
            number = num
        elif num< number:
            return f"error: {num} \n{num} is not increasing after {number} in list"

def gmail(data:str):
    result = list()
    for word in data.split():
        if '@' in word and '.' in word and len(word) > 15:
            result.append(word)
    return result

