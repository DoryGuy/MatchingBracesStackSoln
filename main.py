
#  main.py
#  MatchingBracesStackSoln
#
#  Created by Gary Powell on 1/9/25.
#  Copyright © 2025 Guest User. All rights reserved.
#

from enum import Enum

PASS = 1
FAIL = 0
enumText = ('FAIL', 'PASS')

Result_t = Enum ('Result',  [(enumText[FAIL], FAIL), (enumText[PASS], PASS) ])

# character set which starts the grouping
opening = { '(', '{', '[', '<' }
# hash map which maps opening character to the closing character.
match_brace = { ')': '(', 
                '}': '{',
                ']': '[', 
                '>': '<' }

def parse(input):
    braces = []
    
    for c in input:
        if c in opening:
            braces.append(c);
        else:
            if match_brace.get(c) is not None:
                found_closing = match_brace.get(c)
                if len(braces) == 0:
                    return FAIL;
                p = braces[-1];
                braces.pop();
                if (p != found_closing):
                    return FAIL;

    if len(braces) != 0:
        return FAIL;
    
    return PASS;

def main():
    input = (
        ("([])", PASS),
        ("(abc)", PASS),
        ("((", FAIL),
        (")(", FAIL),
        ("({[]})", PASS),
        ("", PASS),
        (")", FAIL),
        ("]", FAIL),
        ("}", FAIL),
        ("(", FAIL),
        ("[", FAIL),
        ("}", FAIL),
        ("<", FAIL),
        ("({)", FAIL),
        ("(})", FAIL),
        ("([)", FAIL),
        ("(])", FAIL),
        ("({)", FAIL),
        ("[(]", FAIL),
        ("[)]", FAIL),
        ("[{]", FAIL),
        ("[{]}", FAIL),
        ("({])", FAIL),
        ("([})", FAIL),
        ("((]}", FAIL),
        ("([)]", FAIL),
        ("({)}", FAIL),
        ("[{]}", FAIL),
        ("[(])", FAIL),
        ("{(})", FAIL),
        ("{[}]", FAIL),
        ("<(>)", FAIL),
        ("<[>]", FAIL),
        ("<{>}", FAIL),
        ("(([))]", FAIL),
        ("{(}", FAIL),
        ("{[}", FAIL),
        ("()(", FAIL),
        ("][", FAIL),
        ("}{", FAIL),
        ("()", PASS),
        ("[]", PASS),
        ("{}", PASS),
        ("<>", PASS),
        ("<()>", PASS),
        ("><", FAIL),
        ("()[]", PASS),
        ("(){}", PASS),
        ("[]{}", PASS),
        ("()[]{}", PASS),
        ("()[]{}<>", PASS)
    )

    for i in input:
        result = parse(i[0])
        if (result == i[1]):
            print("input = \"" + i[0] + "\" correctly " + enumText[result] + ".")
        else:
            print("input " + enumText[result] + " \"" + i[0] + "\" should should have " + enumText[i[1]] + ".")

    return 0

main()
print("Done")
