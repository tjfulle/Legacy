#!/usr/bin/env python
import os
import re
import sys
import math
import numpy as np
import xml.dom.minidom as xdom
try:
    import argparse
except ImportError:
    argparse = None

# safe values to be used in eval
GDICT = {"__builtins__": None}
DEBUG = False
MAGIC = -1234
WARNINGS = 0
RAND = np.random.RandomState()
SAFE = {"np": np,
        "sqrt": np.sqrt, "max": np.amax, "min": np.amin,
        "stdev": np.std, "std": np.std,
        "abs": np.abs, "ave": np.average, "average": np.average,
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "asin": np.arcsin, "acos": np.arccos,
        "atan2": np.arctan, "atan2": np.arctan2,
        "log": np.log, "exp": np.exp,
        "floor": np.floor, "ceil": np.ceil,
        "pi": math.pi, "G": 9.80665, "inf": np.inf, "nan": np.nan,
        "random": RAND.random_sample, "randreal": RAND.random_sample(),}


def logerr(message=None, errors=[0], inquire=False):
    if inquire:
        return errors[0]
    sys.stderr.write("*** error: {0}\n".format(message))
    errors[0] += 1


def parse_args_no_argparse(argv):
    """Dummy version of argparse"""
    usage = """pprepro.py: Python PreProcessor
usage: pprepro.py <file>"""
    if not argv or "-h" in argv:
        raise SystemExit(usage)
    class Namespace: pass
    args = Namespace()
    args.source = argv[0]
    args.o = None
    args.subs = {}
    args.c = "#"
    args.A = False
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argparse:
        args = parse_args_no_argparse(argv)
    else:
        parser = argparse.ArgumentParser(description="Python PreProcessor")
        parser.add_argument("-o", help="Output filename [default: stdout]")
        parser.add_argument("-c", default="#",
            help="Comment character [default: stdout]")
        parser.add_argument("-A", default=False, action="store_true",
            help="Abaqus preprocessing [default: stdout]")
        parser.add_argument("subs", nargs="*",
            help="Variables to substitute in the form var=val.  Accumulated.")
        parser.add_argument("source", help="PPR source file")
        args = parser.parse_args(argv)
        prepro = {}
        for sub in args.subs:
            try:
                k, v, = sub.split("=")
            except ValueError:
                logerr("expected subs as key=val pairs, got {0}".format(sub))
                continue
            prepro[k] = eval(v, GDICT, SAFE)
        if logerr(inquire=True):
            raise SystemExit("pprepro: stopping due to previous errors")
        args.subs = prepro

        if args.A:
            args.c = "**"

    filepath = os.path.realpath(args.source)
    if not os.path.isfile(filepath):
        raise SystemExit("{0}: no such file".format(filepath))
    lines = find_and_make_subs(open(filepath, "r").read(), prepro=args.subs,
                               cchar=args.c)
    stream = sys.stdout if not args.o else open(args.o, "w")
    for line in lines.split("\n"):
        stream.write(line + "\n")
    return


def update_safe(update_to_safe):
    """Update the SAFE dictionary for using in eval statments

    """
    global SAFE
    SAFE.update(update_to_safe)


def set_random_seed(seed):
    global RAND
    RAND = np.random.RandomState(seed)
    update_safe({"random": RAND.random_sample, "randreal": RAND.random_sample()})


def find_vars_to_sub(lines, argp):
    """Find vars to be preprocessed

    Parameters
    ----------
    lines : str
        user input

    argp : dict
       key, val pairs given on command line.

    Returns
    -------
    vars_to_sub : dict
        dictionary of found variables

    """
    vars_to_sub = {}
    hold = []
    regex = r"(?i)\{\s*[\w]+[\w\d]*\s*=.*?\}"
    variables = re.findall(regex, lines)
    for variable in variables:
        vsplit = re.sub(r"[\{\}]", "", variable).split("=")
        key = vsplit[0].strip()
        hold.append(key)
        if key in argp:
            var_to_sub = eval(argp[key], GDICT, SAFE)
        else:
            expr = vsplit[1].strip()
            var_to_sub = eval(expr, GDICT, SAFE)
        if key.lower() == "random_seed":
            set_random_seed(var_to_sub)
        update_safe({key: var_to_sub})
        vars_to_sub[key] = repr(var_to_sub)

    # replace the commented value.  ie. { foo = 1.2 } -> 1.2
    for (i, variable) in enumerate(variables):
        lines = re.sub(re.escape(variable), vars_to_sub[hold[i]], lines)

    return lines, vars_to_sub


def find_subs_to_make(lines):
    """Find all substitutions that need to be made

    """
    regex = re.compile(r"{(?P<var>.*)}")
    subs_to_make = [k for m in regex.findall(lines) for k in m.split()]
    return subs_to_make


def find_python_code(lines, cchar="#"):
    """Find python code

    """
    newlines = []
    regex = r"(?ms)\s*?\{PYTHON.*?ENDPYTHON\}"
    code_frags = re.findall(regex, lines)
    for code_frag in code_frags:
        # look for the python code
        cmnt = "{0}  PYTHON: EVAL'D".format(cchar)
        lines = lines.replace(code_frag, cmnt)
        code_frag = [l for l in code_frag.split("\n") if l.split()]
        py_exe = []
        for (i, line) in enumerate(code_frag[1:-1]):
            try:
                line = line.split(cchar, 1)[1:][0]
            except IndexError:
                continue
            # determine number of leading spaces on first line
            if i == 0:
                # find first white space character
                n = len(line) - len(line.lstrip())
            py_exe.append(line[n:])
        py_exe = "\n".join(py_exe)
        py_exe = compile(py_exe, "<string>", "exec")
        exec py_exe  in GDICT, SAFE
    return lines


def find_and_make_subs(lines, prepro=None, disp=0, argp=None, cchar="#"):
    """Preprocess the input file

    Parameters
    ----------
    lines : str
        user input

    Returns
    -------
    lines : str
        preprocessed user input

    """
    if prepro is not None:
        update_safe(prepro)
    if argp is None:
        argp = {}
    lines = find_python_code(lines, cchar=cchar)
    lines, vars_to_sub = find_vars_to_sub(lines, argp)
    if not vars_to_sub and prepro is None and disp != MAGIC:
        if disp:
            return lines, 0, 0
        else:
            return lines
    return make_var_subs(lines, vars_to_sub, disp=disp)


def make_var_subs(lines, vars_to_sub, disp=0):
    global WARNING
    magic = disp == MAGIC
    if magic:
        disp = 0

    # the regular expression that defines the preprocessing
    pregex = r"(?i){{.*\b{0:s}\b.*}}"

    if vars_to_sub and DEBUG:
        # Print out preprocessed values for debugging
        sys.stdout.write("Preprocessor values:\n")
        name_len = max([len(x) for x in vars_to_sub])
        for pat, repl in vars_to_sub.items():
            sys.stdout.write("    {0:<{1}s} {2}\n".format(
                pat + ":", name_len + 2, repl))

        for pat, repl in vars_to_sub.items():
            # Check that each preprocessor variable is used somewhere else in
            # the file. Issue a warning if not. It is done here outside of the
            # replacement loop to be sure that we can check all variables.
            # Because variables in the preprocessor block were put in the safe
            # it is possible for, say, var_2 to be replaced when replacing
            # var_1 if the user specified something like
            #          param = {var_1 * var_2}
            # So, since we want to check that all preprocessed variables are
            # used, we do it here. Checking is important for permutate and
            # optimization jobs to make sure that all permutated and optimized
            # variables are used properly in the file before the job actually
            # begins.
            if pat not in SAFE and not re.search(pregex.format(pat), lines):
                sys.stderr.write("*** prepro: {0}: not found in "
                                 "input\n".format(pat))
                WARNINGS += 1
                continue

    # Replace '{ var }' with '{ (var_value) }'
    regex = r"{{.*\b{0}\b.*}}"
    nsubs = 0
    for pat, repl in vars_to_sub.items():
        repl = "({0})".format(re.sub(r"[\{\}]", " ", repl).strip())
        matches = re.findall(regex.format(pat), lines)
        for match in matches:
            mrepl, n = re.subn(r"\b{0}\b".format(pat), repl, match)
            lines = re.sub(re.escape(match), mrepl, lines)
            nsubs += n
            continue
        continue

    # Evaluate substitutions
    errors = []
    regex = r"(?i){.*?}"
    matches = re.findall(regex, lines)
    for pat in matches:
        repl = re.sub(r"[\{\}]", "", pat)
        try:
            repl = str(eval(repl, GDICT, SAFE))
        except NameError as e:
            errors.append(e.message)
            if not disp: sys.stderr.write(e.message)
            continue
        lines = re.sub(re.escape(pat), repl, lines)

    if disp:
        return lines, nsubs, errors

    if errors:
        raise SystemExit("pprepro: stopping due to previous errors")
    return lines


def find_and_fill_includes(lines):
    """Look for 'include' commands in lines and insert then contents in place

    Parameters
    ----------
    lines : str
        User input

    Returns
    -------
    lines : str
        User input, modified in place, with inserts inserted

    """
    #print dir(includes[0])
    #print includes
    #sys.exit('check include')
    regex = r"(?i)<(include|insert)\s(?P<include>.*)/>"
    _lines = []
    for line in lines.split("\n"):
        if not line.split():
            _lines.append(line.strip())
            continue
        include = re.search(regex, line)
        if include is None:
            _lines.append(line)
            continue

        href = re.search(r"""href=["'](?P<href>.*?)["']""",
                         include.group("include"))

        tag = re.search(r"""tag=["'](?P<tag>.*?)["']""",
                        include.group("include"))
        if tag and href:
            raise SystemExit("Include: expected only one of: href, tag")

        if not href and not tag:
            raise SystemExit("Include: expected one of: href, tag")

        if href:
            name = href.group("href").strip()
            fpath = os.path.realpath(os.path.expanduser(name))
            try:
                fill = open(fpath, "r").read()
            except IOError:
                raise SystemExit("{0}: include not found".format(repr(name)))
        else:
            name = tag.group("tag").strip()
            doc = xdom.parseString(lines)
            el = doc.getElementsByTagName(name)
            if not el:
                raise SystemExit("{0}: tag not found".format(repr(name)))
            fill = "\n".join(e.toxml() for e in el[0].childNodes)

        _lines.extend(find_and_fill_includes(fill).split("\n"))
        continue
    return "\n".join(_lines)


if __name__ == "__main__":
    main()
