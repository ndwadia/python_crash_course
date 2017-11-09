# pylint: disable=invalid-name
"""
Word Count
"""

def count_words(file_name):
    """Count the approximate number of words in a file"""
    try:
        with open(file_name, encoding='UTF-8', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError as e:
        print(e)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words.")

filenames = ['../dataproc/ebooks/pg4300-0.txt', '../dataproc/ebooks/pg20417.txt',
             '../dataproc/ebooks/pg5000-8.txt']
for filename in filenames:
    count_words(filename)
