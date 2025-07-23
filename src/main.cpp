#include "../includes/computorv1.hpp"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Split a string by a given delimiter
vector<string> split(string s, const string &delimiter)
{
    size_t pos_start = 0, pos_end;
    size_t delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos)
    {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr(pos_start));
    return res;
}

int main(int ac, char **av)
{
    if (ac != 2)
    {
        cerr << "Error: wrong number of arguments." << endl;
        return 1;
    }

    string equation = av[1];
    vector<string> sides = split(equation, "=");
    int index = 0;
    for (size_t i = 0; i <= equation.length(); i++)
    {
        if (equation[i] == '=')
            index++;
    }
    if (index != 1)
    {
        cerr << "error equation" << endl;
        return 1;
    }
    for (size_t i = 0; i < equation.length(); i++)
    {
        if (equation[i] == '^')
        {
            if (!(isnumber(equation[i + 1]) && equation[i - 1] == 'X'))
            {
                cerr << "error euq";
                return 1;
            }
        }
    }

    return 0;
}
