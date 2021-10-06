import json


def update_pipeline(pipeline_filename, zone_list, machineType, local_sdd_size=375,
                    use_preemptible=True):
    with open(pipeline_filename) as fin:
        pipeline = json.load(fin)
        pipeline['resources']['zones'] = zone_list
        pipeline['resources']['virtualMachine']['machineType'] = machineType
        pipeline['resources']['virtualMachine']['preemptible'] = use_preemptible
        pipeline['resources']['virtualMachine']['disks'][0]['sizeGb'] = local_sdd_size
    # Writing pipeline back to file
    with open(pipeline_filename, 'w') as fout:
        json.dump(pipeline, fout, indent=4)
