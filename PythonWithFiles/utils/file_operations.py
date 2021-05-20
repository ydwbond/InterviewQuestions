def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        raise
