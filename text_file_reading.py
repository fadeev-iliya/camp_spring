def read_with_split(filename, split_simbol):
    file = open(filename, 'r')
    data = file.read()
    data_split = data.split(split_simbol)
    file.close()
    return data_split