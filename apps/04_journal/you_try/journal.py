"""
This is the module to manage the journal data.

load()
save()
add_entry()
"""
import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method save the journal to a .jrl file.

    :param name: This base name of the journal to save
    :param journal_data: The journal data to save in the file
    :return:
    """
    filename = get_full_pathname(name)
    print("....... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    This method gets the full pathname of the file to load or save

    :param name: This base name of the file
    :return: the full pathname of the file name
    """
    filename = os.path.abspath(os.path.join('.', 'journals/', name + '.jrl'))
    return filename


def add_entry(text, data):
    """
    This method add an entry to the journal datal.

    :param text: The text of the new entry
    :param data: The journal data to add the new entry
    :return: nothing
    """
    data.append(text)
