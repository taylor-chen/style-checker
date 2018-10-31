import os
import argparse
import yaml


def run():
    args = parse_cli()
    content_path = os.path.abspath(args.inputDirectory)
    words = get_words_from_yaml(args.words)
    for dirpath, _, filename in os.walk(content_path):
        for file in filename:
            if file.endswith(".{}".format(args.extension)):
                # create full path
                md_path = os.path.join(dirpath, file)
                process_file(md_path, words)


def process_file(path, words):
    with open(path) as f:
        lines = [line.rstrip('\n') for line in f]
        for number, line in enumerate(lines):
            for bad_word in words:
                if bad_word in line.lower():
                    print(path, 'in line number:', number, '\n', find_word(line, bad_word))


def find_word(t, word):
    return t.replace(word, "\033[1;31m" + word + "\033[0m")


def get_words_from_yaml(file):
    with open(file, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def parse_cli():
    parser = argparse.ArgumentParser(description='Style guide linter.')
    parser.add_argument('inputDirectory', help='Path to the input directory to lint.')
    parser.add_argument('-w', '--words', default='words.yml',
                        help='YAML file with list of words to lint for, default is `words.yml` in the same directory.')
    parser.add_argument('-e', '--extension', nargs='?', default='md',
                        help='Change the extension of file to search for, the default is `md`')
    return parser.parse_args()


if __name__ == "__main__":
    run()
