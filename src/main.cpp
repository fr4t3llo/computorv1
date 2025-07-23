#include "../includes/computorv1.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Split a string by a given delimiter
vector<string> split(string s, const string& delimiter) {
    size_t pos_start = 0, pos_end;
    size_t delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr(pos_start));
    return res;
}

int main(int ac, char **av)
{
    if (ac != 2) {
        cerr << "Error: wrong number of arguments. Usage: ./computor \"equation\"" << endl;
        return 1;
    }

    string equation = av[1];
    vector<string> sides = split(equation, "=");

    if (sides.size() != 2) {
        cerr << "Error: equation must contain exactly one '=' sign." << endl;
        return 1;
    }
    

    cout << "Left side: " << sides[0] << endl;
    cout << "Right side: " << sides[1] << endl;

    return 0;
}
