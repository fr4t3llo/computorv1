#include "../includes/computorv1.hpp"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " \"equation\"" << std::endl;
        std::cerr << "Example: " << argv[0] << " \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"" << std::endl;
        return 1;
    }
    
    try {
        PolynomialSolver solver;
        std::string equation = argv[1];
        
        solver.parseEquation(equation);
        
        std::cout << "Reduced form: " << solver.getReducedForm() << std::endl;
        solver.solve();
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}



// // Split a string by a given delimiter
// vector<string> split(string s, const string &delimiter)
// {
//     size_t pos_start = 0, pos_end;
//     size_t delim_len = delimiter.length();
//     string token;
//     vector<string> res;

//     while ((pos_end = s.find(delimiter, pos_start)) != string::npos)
//     {
//         token = s.substr(pos_start, pos_end - pos_start);
//         pos_start = pos_end + delim_len;
//         res.push_back(token);
//     }

//     res.push_back(s.substr(pos_start));
//     return res;
// }

// int main(int ac, char **av)
// {
//     if (ac != 2)
//     {
//         cerr << "Error: wrong number of arguments." << endl;
//         return 1;
//     }

//     string equation = av[1];
//     vector<string> sides = split(equation, "=");
//     int index = 0;
//     for (size_t i = 0; i <= equation.length(); i++)
//     {
//         if (equation[i] == '=')
//             index++;
//     }
//     if (index != 1)
//     {
//         cerr << "error equation" << endl;
//         return 1;
//     }
//     for (size_t i = 0; i < equation.length(); i++)
//     {
//         if (equation[i] == '^')
//         {
//             if (!(isnumber(equation[i + 1]) && equation[i - 1] == 'X'))
//             {
//                 cerr << "error euq";
//                 return 1;
//             }
//         }
//     }

//     return 0;
// }
