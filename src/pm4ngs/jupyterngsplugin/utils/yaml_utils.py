import yaml


def write_to_yaml(src, file_name):
    with open(file_name, 'w') as file:
        yaml.dump(src, file)


def load_from_yaml(file_name):
    data = None
    with open(file_name) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data
