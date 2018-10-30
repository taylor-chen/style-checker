import os
import argparse

BAD_WORDS = ['please', 'currently', 'refer to', 'utilize']


def run():
    args = parse_cli()
    content_path = os.path.abspath(args.inputDirectory)
    for dirpath, _, filename in os.walk(content_path):
        for file in filename:
            if file.endswith(".{}".format(args.extension)):
                # create full path
                md_path = os.path.join(dirpath, file)
                with open(md_path) as f:
                    lines = [line.rstrip('\n') for line in f]
                    for number, line in enumerate(lines):
                        for bad_word in BAD_WORDS:
                            if bad_word in line.lower():
                                print(md_path, 'in line number:', number, '\n', find_word(line, bad_word))


def parse_cli():
    parser = argparse.ArgumentParser(description='Style guide linter.')
    parser.add_argument('inputDirectory', help='Path to the input directory to lint.')
    parser.add_argument('-e', '--extension', nargs='?', default='md',
                        help='Change the extension of file to search for, the default is `md`')
    return parser.parse_args()


def find_word(t, word):
    return t.replace(word, "\033[1;31m" + word + "\033[0m")


if __name__ == "__main__":
    run()
