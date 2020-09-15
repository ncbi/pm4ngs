

def load_content_dict(file, delimiter, strip_line=True,
                      replace_old=None, replace_new=None, comment=None,
                      startswith=None):
    """
    This function load file content in a dictionary spliting the line in two (key-value)
    :param file: File to parse
    :param delimiter: Delimiter to split line
    :param strip_line: Strip line before splitting
    :param replace_old: Replace substring  replace_old with replace_new before splitting
    :param replace_new: Replace substring  replace_old with replace_new before splitting
    :param comment: Comment str to exclude line
    :param startswith: Parse line if start with startswith
    :return: Dict with file content
    """
    result = {}
    with open(file) as fin:
        for line in fin:
            if (not comment or (comment and not line.startswith(comment))) or \
                    (startswith and line.startswith(startswith)):
                if strip_line:
                    line = line.strip()
                if replace_old:
                    line = line.replace(replace_old, replace_new)
                fields = line.split(delimiter)
                if len(fields) == 2:
                    result[fields[0].strip()] = fields[1].strip()
    return result


def load_content_dict_line(file, delimiter, startswith, sec_delimiter, strip_line=True,
                           replace_old=None, replace_new=None):
    """
    This function load file content in a dictionary spliting the line in two (key-value)
    :param file: File to parse
    :param delimiter: Delimiter to split line
    :param strip_line: Strip line before splitting
    :param replace_old: Replace substring  replace_old with replace_new before splitting
    :param replace_new: Replace substring  replace_old with replace_new before splitting
    :param startswith: Parse line if start with startswith
    :return: Dict with file content
    """
    result = {}
    with open(file) as fin:
        for line in fin:
            if line.startswith(startswith):
                if strip_line:
                    line = line.strip()
                if replace_old:
                    line = line.replace(replace_old, replace_new)
                fields = line.split(delimiter)
                if len(fields) == 2:
                    result[fields[0].strip()] = fields[1].strip().split(sec_delimiter)[0]
    return result
