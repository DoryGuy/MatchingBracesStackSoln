
#  main.py
#  MatchingBracesStackSoln
#
#  Created by Gary Powell on 1/9/25.
#  Copyright © 2025 Guest User. All rights reserved.
#

# pylint: disable=line-too-long,missing-module-docstring

from enum import Enum

class ResultType(Enum):
    '''
    Class to have a type for results which is type safe and
    easy to print. ie builtin 'name'
    '''
    PASS = 1
    FAIL = 0

# character set which starts the grouping
opening = { '(', '{', '[', '<' }
# hash map which maps opening character to the closing character.
match_brace = { ')': '(',
                '}': '{',
                ']': '[', 
                '>': '<' }

def parse(string: str) -> ResultType:
    '''
    check the input for correctly matching braces
    '''
    braces = []

    for c in string:
        if c in opening:
            braces.append(c)
        else:
            if match_brace.get(c) is not None:
                found_closing = match_brace.get(c)
                if len(braces) == 0:
                    return ResultType.FAIL
                p: str = braces[-1]
                braces.pop()
                if p != found_closing:
                    return ResultType.FAIL

    if len(braces) != 0:
        return ResultType.FAIL

    return ResultType.PASS

def main() -> int:
    '''
    controlling fn.
    '''
    test_strings = (
        ("([])", ResultType.PASS),
        ("(abc)", ResultType.PASS),
        ("((", ResultType.FAIL),
        (")(", ResultType.FAIL),
        ("({[]})", ResultType.PASS),
        ("", ResultType.PASS),
        (")", ResultType.FAIL),
        ("]", ResultType.FAIL),
        ("}", ResultType.FAIL),
        ("(", ResultType.FAIL),
        ("[", ResultType.FAIL),
        ("}", ResultType.FAIL),
        ("<", ResultType.FAIL),
        ("({)", ResultType.FAIL),
        ("(})", ResultType.FAIL),
        ("([)", ResultType.FAIL),
        ("(])", ResultType.FAIL),
        ("({)", ResultType.FAIL),
        ("[(]", ResultType.FAIL),
        ("[)]", ResultType.FAIL),
        ("[{]", ResultType.FAIL),
        ("[{]}", ResultType.FAIL),
        ("({])", ResultType.FAIL),
        ("([})", ResultType.FAIL),
        ("((]}", ResultType.FAIL),
        ("([)]", ResultType.FAIL),
        ("({)}", ResultType.FAIL),
        ("[{]}", ResultType.FAIL),
        ("[(])", ResultType.FAIL),
        ("{(})", ResultType.FAIL),
        ("{[}]", ResultType.FAIL),
        ("<(>)", ResultType.FAIL),
        ("<[>]", ResultType.FAIL),
        ("<{>}", ResultType.FAIL),
        ("(([))]", ResultType.FAIL),
        ("{(}", ResultType.FAIL),
        ("{[}", ResultType.FAIL),
        ("()(", ResultType.FAIL),
        ("][", ResultType.FAIL),
        ("}{", ResultType.FAIL),
        ("()", ResultType.PASS),
        ("[]", ResultType.PASS),
        ("{}", ResultType.PASS),
        ("<>", ResultType.PASS),
        ("<()>", ResultType.PASS),
        ("><", ResultType.FAIL),
        ("()[]", ResultType.PASS),
        ("(){}", ResultType.PASS),
        ("[]{}", ResultType.PASS),
        ("()[]{}", ResultType.PASS),
        ("()[]{}<>", ResultType.PASS)
    )

    for i in test_strings:
        result = parse(i[0])
        if result == i[1]:
            print("input = \"" + i[0] + "\" correctly " + result.name + ".")
        else:
            print("input " + result.name + " \"" + i[0] + "\" should should have " + i[1].name + ".")

    print("Done")
    return 0

# This code runs only when the module is executed directly
if __name__ == '__main__':
    main()
