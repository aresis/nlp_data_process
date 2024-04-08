import tqdm

import main


def data_clean(filelist):
    result = [item.split('.')[0] + '_clean.txt' for item in filelist]

    for i in range(len(filelist)):
        r = open(result[i], 'w', encoding='utf-8')
        with open(filelist[i], 'r', encoding='utf-8') as f:
            data = f.readlines()

        for text in tqdm.tqdm(data):
            cleaned_doc = main.process(text.strip())
            if len(cleaned_doc.strip().split(' ')) > 5:
                r.write(cleaned_doc.strip() + '\n')
        r.close()


if __name__ == "__main__":
    filelist = ['COVID.csv']
    data_clean(filelist)
