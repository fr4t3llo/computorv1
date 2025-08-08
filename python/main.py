#!/usr/bin/env python3
import sys
import re
import math

def parse_equation(equation):
    """Parse equation and return coefficients dict"""
    coeffs = {0: 0, 1: 0, 2: 0}
    
    try:
        # Split by = and process both sides
        left, right = equation.split('=')
        
        def extract_terms(side, sign):
            # Remove spaces and make uppercase
            side = side.replace(' ', '').upper()
            # Add + at beginning if needed
            if not side.startswith(('+', '-')):
                side = '+' + side
            # Split into terms by + and - while keeping the operators
            terms = []
            current_term = ''
            for i, char in enumerate(side):
                if char in '+-' and i > 0:
                    if current_term:
                        terms.append(current_term)
                    current_term = char
                else:
                    current_term += char
            if current_term:
                terms.append(current_term)
            
            for term in terms:
                if not term.strip():
                    continue
                
                # Parse each term (like "+5*X^0", "-9.3*X^2")
                # Extract sign
                term_sign = 1
                if term.startswith('-'):
                    term_sign = -1
                    term = term[1:]
                elif term.startswith('+'):
                    term = term[1:]
                
                # Find coefficient and power
                if '*X^' in term:
                    coeff_str, power_str = term.split('*X^')
                    coeff = float(coeff_str) if coeff_str else 1
                    power = int(power_str)
                elif '*X' in term:
                    coeff_str = term.split('*X')[0]
                    coeff = float(coeff_str) if coeff_str else 1
                    power = 1
                elif 'X^' in term:
                    power = int(term.split('X^')[1])
                    coeff = 1
                elif 'X' in term:
                    coeff = 1
                    power = 1
                else:
                    # Pure number
                    coeff = float(term)
                    power = 0
                
                coeffs[power] += sign * term_sign * coeff
        
        # Process both sides
        extract_terms(left, 1)
        extract_terms(right, -1)
        
        return coeffs
        
    except Exception as e:
        raise Exception(f"Failed to parse equation: {equation}")


def get_reduced_form(coeffs):
    """Generate reduced form string"""
    terms = []
    
    # Always show in order: X^0, X^1, X^2, etc.
    max_power = max(k for k, v in coeffs.items() if abs(v) > 1e-10) if any(abs(v) > 1e-10 for v in coeffs.values()) else 0
    
    for power in range(max_power + 1):
        coeff = coeffs.get(power, 0)
        if abs(coeff) < 1e-10:
            continue
        
        # Format each term as "coeff * X^power"
        if power == 0:
            term = f"{coeff} * X^0"
        elif power == 1:
            term = f"{coeff} * X^1"
        else:
            term = f"{coeff} * X^{power}"
        
        terms.append(term)
    
    if not terms:
        return "0 * X^0 = 0"
    
    # Join terms with proper signs
    result = terms[0]
    for i in range(1, len(terms)):
        term = terms[i]
        if term.startswith('-'):
            result += f" - {term[1:]}"
        else:
            result += f" + {term}"
    
    return f"{result} = 0"

def get_degree(coeffs):
    """Get polynomial degree"""
    for power in sorted(coeffs.keys(), reverse=True):
        if abs(coeffs[power]) > 1e-10:
            return power
    return 0

def solve_polynomial(coeffs):
    """Solve the polynomial equation"""
    degree = get_degree(coeffs)
    print(f"Polynomial degree: {degree}")
    
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return
    
    if degree == 0:
        a0 = coeffs[0]
        if abs(a0) < 1e-10:
            print("Any real number is a solution.")
        else:
            print("No solution.")
    
    elif degree == 1:
        a0, a1 = coeffs[0], coeffs[1]
        if abs(a1) < 1e-10:
            if abs(a0) < 1e-10:
                print("Any real number is a solution.")
            else:
                print("No solution.")
        else:
            solution = -a0 / a1
            print("The solution is:")
            print(f"{solution:.6g}")
    
    elif degree == 2:
        a0, a1, a2 = coeffs[0], coeffs[1], coeffs[2]
        discriminant = a1**2 - 4*a2*a0
        
        if discriminant > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            sqrt_d = math.sqrt(discriminant)
            sol1 = (-a1 + sqrt_d) / (2*a2)
            sol2 = (-a1 - sqrt_d) / (2*a2)
            print(f"{sol1:.6g}")
            print(f"{sol2:.6g}")
        
        elif abs(discriminant) < 1e-10:
            print("Discriminant is zero, the solution is:")
            solution = -a1 / (2*a2)
            print(f"{solution:.6g}")
        
        else:
            print("Discriminant is strictly negative, the two complex solutions are:")
            real = -a1 / (2*a2)
            imag = math.sqrt(-discriminant) / (2*a2)
            print(f"{real:.6g} + {imag:.6g}i")
            print(f"{real:.6g} - {imag:.6g}i")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} \"equation\"")
        print(f"Example: {sys.argv[0]} \"5 + 4 * X + X^2 = X^2\"")
        sys.exit(1)
    
    try:
        equation = sys.argv[1]
        coeffs = parse_equation(equation)
        
        print(f"Reduced form: {get_reduced_form(coeffs)}")
        solve_polynomial(coeffs)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()