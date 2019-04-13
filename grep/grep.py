import argparse
import operator
from collections import defaultdict
from re import escape, match, sub
from colorama import init, Fore

# Colorama init, necessary only on Windows
init()

# Create command line interface
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", nargs='+', required=True, help="input file(s)")
ap.add_argument("-c", "--count", action='store_true', help="match count")
ap.add_argument("-i", "--name", action='store_true', help="display filename")
ap.add_argument("-p", "--pattern", type=str, help="pattern to match")
ap.add_argument("-r", "--regex", type=str, help="regular expression to match")
ap.add_argument("-n", "--inverse", action='store_true', help="inverse match")
ap.add_argument("-l", "--lines", type=int, help="display lines")
ap.add_argument("-C", "--context", type=int, help="print context")
args = vars(ap.parse_args())

# Error if both pattern and regex are selected
if args['pattern'] is not None and args['regex'] is not None:
    ap.error("options -p and -r are mutually exclusive")
elif args['pattern']:
    # Matching pattern
    regexp = f"((.*){escape(args['pattern'])}(.*))"
    sb = f"({escape(args['pattern'])})"
elif args['regex']:
    # Matching regex
    regexp = f"(.*){args['regex']}(.*)"
    sb = f"({args['regex']})"


# Color coded matches in terminal
def color_coded(string):
    return sub(sb, Fore.RED + r'\1' + Fore.RESET, string)


# Return file lines without end of line characters
def clean_lines(it):
    return map(operator.methodcaller('rstrip', '\r\n'), it)


# Console print to keep track of output lines
def print_out(string, print_count=[0]):
    print_count[0] += 1

    if args['lines'] and not print_count[0] % args['lines']:
        # Print a fixed number of output lines at a time
        print(string, end='')
        input()
    else:
        # Standard call to print
        print(string)


# Count of matching lines
count = 0
# Context to be printed
context = defaultdict(list)
context['leading'] = []
context['trailing'] = []
# Matching line index for context
match_idx = -1

# Display instructions
if args['lines']:
    print("> Press ENTER to display more content")

# Parse file
for file in args['file']:

    # Print the filename
    if args['name']:
        print(f"==> {file} <==")

    # Iterate on the files
    with open(file, "r") as f:
        for idx, line in enumerate(clean_lines(f)):

            # Logical XOR to detect both matching and inverse lines
            if bool(match(regexp, line)) != bool(args['inverse']):
                # Print leading context
                if args['context']:
                    for l in context['leading']:
                        print_out(l)
                    match_idx = idx
                    context['leading'] = []
                # Print color-coded string
                print_out(color_coded(line))
                count += 1

            elif args['context']:
                if match_idx != -1 and (idx - match_idx) <= args['context']:
                    # Save trailing context
                    context['trailing'].append(color_coded(line))
                    if len(context['trailing']) > args['context']:
                        context['trailing'].pop(0)

                # Save leading context and lines between matches
                context['leading'].append(color_coded(line))
                if len(context['leading']) > args['context']:
                    context['leading'].pop(0)

                # Print trailing context
                if idx == match_idx + args['context']:
                    for l in context['trailing']:
                        print_out(l)
                    context['trailing'] = []
                    print_out('> --')

# Print number of matching lines
if args['count']:
    print(f"> Matching lines: {count}")
'''
REFERENCES:
0) Argparse documentation: https://docs.python.org/3/library/argparse.html
1) Regex Highlighting: https://stackoverflow.com/a/7155015/9513156

'''