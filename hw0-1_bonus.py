#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:10:47 2021

@author: Chanmei
"""

polynomial = input('Input the polynomials:') #Input Polynomial Text
#Split Multiplication of Polynomials by Parentheses
#Replace left parenthesis by right parenthesis and split
polynomial = polynomial.replace("(", ")")
tokens = polynomial.split(")")
#Delete the empty string in the list
multipliers = [x for x in tokens if x]
#Split Each Polynomial by '+' and '-'
coefficients = []
for mul in multipliers:
    # Replace '-' with '+-' and split
    mul = mul.replace("-", "+-")
    mul = mul.split("+")
    # Using dictionary to store the information of polynomial
    # i.e. 3A+10B^2+3 will store as {'A': 3, 'B^2': 10, '': 3}
    coef = {}
    for exponent in mul:
        # Bonus:
        # If first character is numeric, then find the next position of alphabet.
        if exponent[0].isnumeric():
            end = 1
            for i in range(1, len(exponent)):
                if exponent[i].isnumeric():
                    end = end + 1
                else:
                    break
            coef[exponent[end:]] = int(exponent[:end])
        # Else, the coefficient will be 1 or -1
        else:
            if exponent[0] == "-":
                coef[exponent.replace("-", "")] = -1
            else:
                coef[exponent] = 1
    coefficients.append(coef)
# Decompose the variable term in each variable and its power
# varTerm is string such as "AB2C3"
# return value is dict such as {'A': 1, 'B': 2, 'C', 3}
def Decomposition(varTerm):
    # varTerm is empty indicate it is constant
    if not varTerm:
        return {'': 0}
    # Using dictionary to store the information of variable term
    # i.e. A^2B^10C will store as {'A': 2, 'B': 10, 'C': 1}
    variable = {}
    # If first character is alphabet, then find the next position of alphabet.
    for index in range(len(varTerm)):
        if varTerm[index].isalpha():
            end = index + 1
            for i in range(index+1, len(varTerm)):
                if varTerm[i].isnumeric():
                    end = end + 1
                else:
                    break
            # If varTerm[index+1:end] is not empty, store the power; otherwise, store 1
            if varTerm[index+1:end]:
                variable[varTerm[index]] = int(varTerm[index+1:end])
            else:
                variable[varTerm[index]] = 1
    return variable
# Encapsulate two variable terms in one variable term
# var1, var2 and the return value are dict. 
# i.e. {'A': 2, 'B': 3}
def Encapsulation(var1, var2):
    # If one of variable term is constant, return the other one.
    if "" in var1:
        return var2
    elif "" in var2:
        return var1
    # Else, add the power for the same variable; new the item for different variable
    else:
        for key in var1:
            if key in var2:
                var2[key] += var1[key]
            else:
                var2[key] = var1[key]
        # Sort the key in alphabetical order
        var2 = dict(sorted(var2.items()))
        return var2
# Multiply two terms and store the temporarily answer
# coef1 and coef2 are int.
# varTerm is dict such as {'A': 1, 'B': 2, 'C': 3}.
# result is dict that store the answer like {'AB^2': 2, 'A^2B': 4}.
def Multiply(coef1, coef2, varTerm, result):
    # Power is empty indicates it is constant
    if "" in varTerm:
        result[""] = coef1*coef2
        return result
    # Otherwise, concatenate the variable term in requested form
    term = ""
    for key in varTerm:
        if varTerm[key] == 1:
            term += key
        else:
            term += (key + str(varTerm[key]))
    # If the variable term can be found in result, then add the value.
    # Else, new the item for variable term.
    if term in result:
        result[term] += coef1 * coef2
    else:
        result[term] = coef1 * coef2
    return result
# Print the polynomial after the multiplication.
# result is dict that store the answer like {'AB^2': 2, 'A^2B': 4}.
def PrintPoly(result):
    # Using list to store each term of polynomial
    # i.e. ['2*AB^2', '4A^2B^3']
    variables = []
    for key in result:
        if result[key] == 0:
            continue
        elif result[key] == 1:
            variables.append(key)
        elif result[key] == -1:
            variables.append("-"+key)
        else:
            variables.append(str(result[key])+key)
    # Concantenate list with "+" and replace "+-" with "-"
    ans = "+".join(variables)
    ans = ans.replace("+-", "-")
    if ans:
        print("Output Result: {}".format(ans))
    else:
        print("Output Result: 0")
# Suppose the current result is 1.
result = {'': 1}
for coef in coefficients:
    # Use temporarily dict to store the current polynomial.
    temp = {}
    # Decompose the multiplicand polynomial in each variable term.
    for res in result:
        var1 = Decomposition(res.replace("^", ""))
        # Decompose the multiplier polynomial in each variable term.
        for key in coef:
            var2 = Decomposition(key.replace("^", ""))
            varTerm = Encapsulation(var1, var2)
            temp = Multiply(result[res], coef[key], varTerm, temp)
    # Update the current multiplication of polynomial
    result = temp.copy()
PrintPoly(result)