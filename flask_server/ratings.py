def read():
    with open('example_data.json') as f:
        data = eval(f.read())
    return data