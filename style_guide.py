import os


def find_word(t, word):
    return t.replace(word, "\033[1;31m" + word + "\033[0m")


bad_words = ['please', 'currently', 'refer to', 'utilize']
content_path = os.getcwd() + "/content"
for dirpath, dirnames, filename in os.walk(content_path):
    for file in filename:
        if file.endswith(".md"):
            # create full path
            md_path = os.path.join(dirpath, file)
            with open(md_path) as f:
                lines = [line.rstrip('\n') for line in f]
                for number, line in enumerate(lines):
                    for bad_word in bad_words:
                        if bad_word in line.lower():
                            print(md_path, 'in line number:', number, '\n', find_word(line, bad_word))
