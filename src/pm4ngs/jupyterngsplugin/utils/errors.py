import os


def check_errors_from_logs(path, log_suffix):
    """
    Check all files with name finishing on the `log_suffix` variable.
    If file doesn't ends with the line:  'Final process status is success'
    the file is reported with error
    :param path: Path to log files
    :param log_suffix: Siffix of logs files to process
    """
    logs = [f for ds, dr, files in os.walk(path) for f in files if f.endswith(log_suffix)]
    if len(logs) == 0:
        print('No logs in folder: ' + path + 'with suffix: ' + log_suffix)
    else:
        failed = False
        for log in logs:
            log_file = os.path.join(path, log)
            with open(log_file, 'r') as fin:
                for line in fin:
                    pass
                if 'Final process status is success' not in line.strip():
                    print('Process no completed or failed.\n'
                          'Please, do not proceed to next cells\n'
                          'Check log file: ' + log_file)
                    failed = True
        if not failed:
            print('Process completed.\nProceed to next cells')
        else:
            print('There are errors in: ' + str(failed) + '/' + str(len(logs)))


def check_cwl_command_log(log_file):
    """
    Check all files with name finishing on the `log_suffix` variable.
    If file doesn't ends with the line:  'Final process status is success'
    the file is reported with error
    :param fastqc.log: log file
    """
    with open(log_file, 'r') as fin:
        failed = False
        for line in fin:
            if 'completed permanentFail' in line:
                print('Process failed.\n'
                      'Please, do not proceed to next cells\n'
                      'Check log file: ' + log_file)
                failed = True
                break
        if not failed:
            if 'Final process status is success' in line.strip():
                print('Process completed.\nProceed to next cells')
            else:
                print('Process no completed.\n'
                      'Please, do not proceed to next cells\n'
                      'Check log file: ' + log_file)
