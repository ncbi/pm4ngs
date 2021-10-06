import json


def update_pipeline_zone(pipeline_filename, zone_list):
    with open(pipeline_filename) as fin:
        pipeline = json.load(fin)
        pipeline['resources']['zones'] = zone_list
    with open(pipeline_filename, 'w') as fout:
        json.dump(pipeline, fout, indent=4)
