#!/usr/bin/env python3
import os
import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def compare_result(ans, result):
    ans = ans.strip().split('\n')
    result = result.strip().split('\n')

    min_len = min(len(ans), len(result))
    for line in range(min_len):
        print("ans: %s\nres: %s" % (ans[line], result[line]))
        if ans[line] != result[line]:
            print(bcolors.FAIL + "\n!! Mismatch !!\n" + bcolors.ENDC)
            return False
        else:
            print("")

    if len(ans) > len(result):
        print(bcolors.FAIL + "!! Result is shorter than the answer !!" + bcolors.ENDC)
        print(bcolors.UNDERLINE + '\n'.join(ans[min_len:])+'\n' + bcolors.ENDC)
        return False
    elif len(ans) < len(result):
        print(bcolors.FAIL + "!! Result is longer than the answer !!" + bcolors.ENDC)
        print(bcolors.UNDERLINE + '\n'.join(result[min_len:])+'\n' + bcolors.ENDC)
        return False
    else:
        print(bcolors.OKGREEN + "OK" + bcolors.ENDC + '\n')
        return True

num_test = 0
pass_n = 0
pass_v = 0

for filename in sorted(os.listdir('test')):
    if filename.endswith('.in'):
        num_test += 1

        # copy input data
        os.chdir('test')
        in_file = open(filename)
        test_file = open('../test.uml', 'w')
        test_file.write(in_file.read())
        in_file.close()
        test_file.close()

        # read call-by-name answer
        ansn_file = open(filename[:-3]+'.n')
        ans_n = ansn_file.read()
        ansn_file.close()

        # read call-by-value answer
        ansv_file = open(filename[:-3]+'.v')
        ans_v = ansv_file.read()
        ansv_file.close()

        # get result
        os.chdir('..')
        proc = subprocess.Popen(['ocaml', 'test.ml'], stdout=subprocess.PIPE)
        result = str(proc.communicate()[0], 'ascii')
        result_n, result_v = result.split('---END---\n')[:2]

        # compare result
        print(bcolors.HEADER + ("<<%s>>" % filename) + bcolors.ENDC)
        print(bcolors.OKBLUE + "[Call-by-name]" + bcolors.ENDC)
        pass_n += compare_result(ans_n, result_n)
        print(bcolors.OKBLUE + "[Call-by-value]" + bcolors.ENDC)
        pass_v += compare_result(ans_v, result_v)

print("Call-by-name: %d / %d" % (pass_n, num_test))
print("Call-by-value: %d / %d" % (pass_v, num_test))
