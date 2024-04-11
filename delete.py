import sys


def delete_stop(input_file, stop_file):
    def read():
        word = []
        with open(stop_file, 'r') as f2:
            for token in f2:
                word.append(token.strip())
        return word

    word_to_delete = read()
    output = []
    with open(input_file, 'r+', encoding='utf-8') as f:
        for line in f:
            tokens = str(line).strip().split(' ')
            sen = ' '.join(token for token in tokens if token not in word_to_delete)
            if len(sen.strip().split(' ')) > 5:
                output.append(sen.strip() + '\n')
    output_file = input_file.split('.')[0] + '_remove.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in output:
            f.write(line)
    print('delete success')


if __name__ == "__main__":
    input_file = sys.argv[1]
    stop_file = sys.argv[2]
    delete_stop(input_file, stop_file)
