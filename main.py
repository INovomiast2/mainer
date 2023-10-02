# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ivnovomi <ivnovomi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/28 05:59:45 by ivnovomi          #+#    #+#              #
#    Updated: 2023/10/02 07:32:32 by ivnovomi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
    Mainer v.1.0 - Developed by ivnovomi<intra.42.fr> - (c) 2023
    
    Summary:
        Make the libft correction 10 times faster, with mainer you'll
        just run the code in a terminal and this will create al the mains
        for your libft functions.
"""

import os
import sys
import time
import subprocess
import configparser
from colorama import Fore, Back, Style

help_message = """
    Mainer v.1.0 - Developed by ivnovomi<intra.42.fr> - (c) 2023
    
    Summary:
        Make the libft correction 10 times faster, optimize your time
        and make the correction faster and less boring.
        
    Usage:
        -- If Alias not Configured --
        python3 mainer.py/main.py
        python3 mainer.py/main.py [options]
        -- If Alias Configured --
        mainer
        mainer [options]
        
    Options:
        -h,  --help          Show this help message and exit
        -rt, --remove-tests  Remove all the test files created by mainer
        -n,  --norminette    Run norminette before mainer does his work
        -d,  --debug         Run mainer on Debug Mode (Just show DEV things)
        -  
"""

def mainer():
    # Check if mains folder is avaliable, if not create it
    if not os.path.exists('mains'):
        os.mkdir('mains')
    # Check if ccc or gcc is installed
    if not os.path.exists('/usr/bin/clang') and not os.path.exists('/usr/bin/gcc'):
        print('You need to install gcc or clang to use mainer')
        sys.exit(1)
    else:
        os.system('clear' or 'cls')
        print("Mainer v.1.0 - Developed by ivnovomi<intra.42.fr> - (c) 2023")
        print("============================================================")
        print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "Starting Mainer...")
        print("============================================================")
        time.sleep(2)
        print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "Checking libft...")
        if os.path.exists(f'{os.getcwd()}/libft'):
            print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "libft.h found")
        else:
            print(Fore.RED + "[ERROR]: " + Fore.RESET + "libft.h not found")
            sys.exit(1)
        print("============================================================")
        time.sleep(2)
        print(Fore.YELLOW + "[INFO]: " + Fore.RESET + "Checking files inside libft...")
        # List al the files with the ft_*.c pattern
        files = [f for f in os.listdir(f'{os.getcwd()}/libft') if f.startswith('ft_') and f.endswith('.c')]
        for f in files:
            time.sleep(0.5)
            print(Fore.WHITE + f + " found! " + Fore.GREEN + "✔" + Fore.RESET)
        print("============================================================")
        time.sleep(2)
        # Reading the main.c file inside the mains folder
        print(Fore.YELLOW + "[INFO]: " + Fore.RESET + "Reading test files...")
        # Just for faster development
        # Create mains inside the mains folder following the test_functionname.c pattern
        # So, first we need to split the name of the functions inside the libft folder
        # and just leave the function name, quit the ft_ and the .c and then add the test_
        # and the .c to the function name
        # Check if the files with the test_*.c pattern exists
        files = [f for f in os.listdir(f'{os.getcwd()}/libft') if f.startswith('ft_') and f.endswith('.c')]
        for f in files:
            if not os.path.isfile(f"{os.getcwd()}/mainer.py/mains/test_{f.split('_')[1].split('.')[0]}.c"):
                print(Fore.YELLOW + "[INFO]: " + Fore.RESET + f"Creating test_{f.split('_')[1].split('.')[0]}.c")
                # Split the name of the function to just functionname without the ft_ and the .c
                function_name = f.split('_')[1].split('.')[0]
                # Now we add the test_ and .c to the function name
                modified_name = f'test_{function_name}.c'
                # And we create the files with the modified name inside the mains folder
                os.system(f'touch {os.getcwd()}/mainer.py/mains/{modified_name}')
                with open(f'{os.getcwd()}/mainer.py/mains/{modified_name}', 'w') as file:
                    file.write(f'#include "libft.h"\n\nint\t\tmain(void)\n{{\n\treturn (0);\n}}')
                    file.close()
                if len(os.listdir(f'{os.getcwd()}/mainer.py/mains')) == len(files):
                    os.system('clear' or 'cls')
                    print("Mainer v.1.0 - Developed by ivnovomi<intra.42.fr> - (c) 2023")
                    print("============================================================")
                    print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "All test files created!")
                    print(Fore.LIGHTMAGENTA_EX + "[IMPORTANT]: " + Fore.RESET + "Create the mains inside every file and re-run mainer.py")
                    print("============================================================")
                    sys.exit(0)
                else:
                    pass
            else:
                break
        print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "All test files found!")
        print("============================================================")
        print(Fore.GREEN + "[STATUS]" + Fore.RESET + "Checking all test files...")
        time.sleep(2)
        print("============================================================")
        # Compile test files with functions inside libft.
        # First we need to check if the mains folder exists
        if os.path.exists(os.getcwd() + "/libft/"):
            # Get all the test files inside the mains folder
            test_files = [f for f in os.listdir(f'{os.getcwd()}/mainer.py/mains') if f.startswith('test_') and f.endswith('.c')]
            print(test_files)
            
        
            

if __name__ == '__main__':
    if len(sys.argv) > 1 and (sys.argv[1] == '-rt' or sys.argv[1] == '--remove-tests'):
        os.system('clear' or 'cls')
        print("Mainer Remove Tests v.1.0 - Developed by ivnovomi<intra.42.fr> - (c) 2023")
        print("=========================================================================")
        time.sleep(2)
        os.system(f'rm -rf {os.getcwd()}/mainer.py/mains/test_*.c')
        print(Fore.GREEN + "[STATUS]: " + Fore.RESET + "All test files removed!")
        time.sleep(2)
        os.system('clear' or 'cls')
        sys.exit(0)
    if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print(help_message)
        sys.exit(0)
    if len(sys.argv) > 1 and (sys.argv[1] == '-n' or sys.argv[1] != '--norminette'):
        subprocess.call(['norminette', '-R', 'CheckForbiddenSourceHeader', 'libft/'])
    else:
        mainer()