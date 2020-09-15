import os


def count_lines(filename, comment):
    """
    Count lines in a file excluding the comment
    :param filename: Path to the file to count
    :param comment: Comment char or string at the beginning of the line to exclude
    :return:
    """
    count = 0
    if os.path.exists(filename) and os.path.getsize(filename) != 0:
        with open(filename, 'r') as fin:
            for line in fin:
                if not line.startswith(comment):
                    count += 1
    return count
