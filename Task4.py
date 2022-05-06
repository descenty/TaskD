import glob
import os
import sys
from time import time
import shutil
import subprocess
import re


def copy_task_files():
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    source_path = os.path.join(app_path, 'Tasks AB')
    target_path = os.path.join(app_path, 'Ознакомительная папка')
    target_a_path = os.path.join(target_path, 'тема A')
    target_b_path = os.path.join(target_path, 'тема B')

    os.makedirs(target_path, exist_ok=True)
    os.makedirs(target_a_path, exist_ok=True)
    os.makedirs(target_a_path, exist_ok=True)

    filenames = glob.glob(os.path.join(source_path, '*.py'))
    for filename in filenames:
        if os.path.isfile(filename):
            if filename.split('/')[-1].count('A') > 0:
                shutil.copy2(filename, target_a_path)
            else:
                shutil.copy2(filename, target_b_path)


regex_function = r'def (.+\))'
regex_params = r'assert.+= (.+)'


def manage_scripts():
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    target_path = os.path.join(app_path, 'Ознакомительная папка')
    for sub_path in [os.path.join(target_path, x) for x in os.listdir(target_path)]:
        filenames = glob.glob(os.path.join(sub_path, '*.py'))
        for filename in filenames:
            if os.path.isfile(filename):
                with open(filename, 'r') as f:
                    file_data = f.read()
                    functions = re.findall(regex_function, file_data)
                    if len(functions) != 1 or functions[0].count('wiki') != 0:
                        continue
                    function_name = functions[0]
                    parameters = re.findall(regex_params, file_data)
                    filename = re.search(r'Ознак.+', filename).group()
                    folder = filename.split('/')[1]
                    print(f'folder \'{folder}\'')
                    print(f'>>> script {filename.split("/")[-1]}')
                    print(f'>>> >>> function \'{function_name}\'')
                    print(f'>>> >>> output \'{" ".join(parameters)} ', end='')
                    time1 = time()
                    popen = subprocess.Popen(['python3', filename],
                                             stdout=subprocess.PIPE, shell=False)
                    time2 = time()
                    print(str(popen.communicate()[0]).replace("b'", '').replace(r'\n', ''), end='')
                    print(r'')
                    delta_time = round((time2 - time1) * 1000, 3)
                    print(f'>>> >>> time \'{delta_time} sec\'', end='\n\n')


def main():
    # copy_task_files()
    manage_scripts()


main()
