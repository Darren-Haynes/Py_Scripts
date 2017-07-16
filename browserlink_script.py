"""
    Basic script that adds a socket to the bottom of a html file (or css, or
    js file). This socket allows for (almost) real time of editing of html,
    js or css files in browsers.
"""

from sys import argv


def main():

    script = "<script src='http://127.0.0.1:9001/js/socket.js'></script>"

    with open(argv[1], 'a') as f:
        f.write('\n' + script + '\n')


if __name__ == "__main__":
    main()
