#!/usr/bin/python
#This code remove empty file from a given dir
#Passed as argument in command line interface

import sys
import os

def remove(dir_path):

    failed, count, succeed = (0,0,0)
    for file_name in os.listdir(dir_path):
        if os.path.isfile(file_name) and os.stat(file_name).st_size == 0:
            try:
                os.remove(file_name)
                succeed +=1 
            except:
                failed +=1

    report = { 
        'succeed': succeed,
        'failed': failed,
        'total':succeed + failed
    }

    return report

def print_report(report):
    output= f"| Succeed: {report['succeed']} " \
            f"| Failed: {report['failed']}" \
            f"| Total: {report['total']} "\
            "|"
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '+'
    lines = [banner,border, output, border, banner]
    print("\n".join(lines))
    print()

def main(argv=None):

    if not len(argv) - 1:
        raise ValueError(f'None argument was passed')
    if not os.path.isdir(argv[1]):
        raise FileNotFoundError(f'Invalid value of {argv[1]} ')
    
    dir_name = argv[1]
    print_report(remove(dir_name))

if __name__ == '__main__':
    main(sys.argv)