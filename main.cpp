//
//  main.cpp
//  MatchingBracesStackSoln
//
//  Created by Gary Powell on 6/14/19.
//  Copyright © 2019 Guest User. All rights reserved.
//

#include <iostream>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <string>
#include <iomanip>
#include <exception>



typedef enum { PASS, FAIL } RESULT_t;
std::map<RESULT_t, std::string> enumText = {{PASS, "PASS"}, {FAIL, "FAIL"}};

std::set<char> const opening = { '(', '{', '[' };
std::map<char, char> const match_brace = { {')', '('}, {'}', '{'}, {']', '['}};

RESULT_t parse(std::string const &input)
{
    using std::stack;
    using std::runtime_error;
    stack<char> braces;
    
    for (auto c: input){
        auto found_opening = opening.find(c);
        if (found_opening != opening.cend())
            braces.push(c);
        else {
            auto found_closing = match_brace.find(c);
            if (found_closing != match_brace.cend()) {
                if (braces.empty()) return FAIL;
                auto p = braces.top();
                braces.pop();
                if (p != found_closing->second) {
                        return FAIL;
                    }
                }
            }
        }
    if (!braces.empty()) return FAIL;
    
    return PASS;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    using std::string;
    using std::cout;
    using std::endl;
    using std::pair;
    using std::make_pair;

    pair<string, RESULT_t> input[] = {
        make_pair("(abc)", PASS),
        make_pair("((", FAIL),
        make_pair("({[]})", PASS),
        make_pair("", PASS),
        make_pair(")", FAIL),
        make_pair("]", FAIL),
        make_pair("}", FAIL),
        make_pair("({)", FAIL),
        make_pair("(})", FAIL),
        make_pair("([)", FAIL),
        make_pair("(])", FAIL),
        make_pair("({)", FAIL),
        make_pair("[(]", FAIL),
        make_pair("[)]", FAIL),
        make_pair("[{]", FAIL),
        make_pair("[{]}", FAIL),
        make_pair("{(}", FAIL),
        make_pair("{[}", FAIL),
        make_pair("()(", FAIL),
        make_pair("][", FAIL),
        make_pair("}{", FAIL),
        make_pair("()", PASS),
        make_pair("[]", PASS),
        make_pair("{}", PASS),
        make_pair("()[]", PASS),
        make_pair("(){}", PASS),
        make_pair("[]{}", PASS),
        make_pair("()[]{}", PASS)
    };
    for (auto i : input){
        auto result = parse(i.first);
        if (result == i.second) {
            cout << "input = \"" << i.first << "\" correctly " << enumText[result] << "\n";
        }
        else {
            cout << "input " << enumText[result] <<  " \"" << i.first
                 << "\" should should have " << enumText[i.second] << ".\n";
        }
    }
    cout << "Done!\n";
    return 0;
}
