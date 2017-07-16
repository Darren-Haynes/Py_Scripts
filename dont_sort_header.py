import sys


def no_header_sort(user_file):
    """Alphabetically sort a list without sorting the first line
       Essentially keeping the header line intact"""

    with open(user_file, 'r+') as file_to_sort:
        data = file_to_sort.readlines()
        data.sort(key=lambda s: s.lower())
        print(data)
        file_to_sort.seek(0)
        file_to_sort.write(''.join(data))


if __name__ == '__main__':
    no_header_sort(sys.argv[1])
