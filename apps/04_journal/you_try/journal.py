import os


def load(name):
    # todo: populate from file if it exists.
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("....... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals/', name + '.jrl'))
    return filename


def add_entry(text, data):
    data.append(text)