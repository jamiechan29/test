#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:03:10 2021

@author: Chanmei
"""

polynomial = input('Input the polynomials:')
polynomial = polynomial.replace("(", ")")
tokens = polynomial.split(")")
multipliers = [x for x in tokens if x]
multipliers = []
for x in tokens:
    if x:
        multipliers.append(x)

coefficients = []
for mul in multipliers:
    mul = mul.replace("-", "+-")
    mul = mul.split("+")
    
def decomp(co):
    if not co:
#         print("Constant")
        return {'': 1}
    vrb = {}
    for index in range(len(co)):
        if co[index].isnumeric():
            end = index + 1
            for i in range(index+1, len(co)):
                if co[i].isalpha():
                    end = end + 1
                else:
                    break
            if co[index-1:end]:
                vrb[co[index]] = int(co[index-1:end])
#                 print("{0}: {1}".format(power[index], power[index+1:end]))
            else:
                vrb[co[index]] = 1
#                 print("{0}: {1}".format(power[index], 1))
    return vrb

    
def decomposition(power):
    if not power:
#         print("Constant")
        return {'': 1}
    variable = {}
    for index in range(len(power)):
        if power[index].isalpha():
            end = index + 1
            for i in range(index+1, len(power)):
                if power[i].isnumeric():
                    end = end + 1
                else:
                    break
            if power[index+1:end]:
                variable[power[index]] = int(power[index+1:end])
#                 print("{0}: {1}".format(power[index], power[index+1:end]))
            else:
                variable[power[index]] = 1
#                 print("{0}: {1}".format(power[index], 1))
    return variable

def combine(var1, var2):
    if "" in var1:
        return var2
    elif "" in var2:
        return var1
    else:
        for key in var1:
            if key in var2:
                var2[key] += var1[key]
            else:
                var2[key] = var1[key]
        var2 = dict(sorted(var2.items()))
        return var2

def multiply(coef1, coef2, power, result):
    if "" in power:
#         print(coef1*coef2)
        result[""] = coef1*coef2
        return result
    string = ""
    for key in power:
        if power[key] == 1:
            string += key
        else:
            string += (key + str(power[key]))
        
    if string in result:
        result[string] += coef1 * coef2
    else:
        result[string] = coef1 * coef2
    return result

def printPoly(result):
    variables = []
    for key in result:
        if result[key] == 1 or result[key] == -1:
            variables.append(key)
        else:
            variables.append(str(result[key])+"*"+key)
    ans = "+".join(variables)
    ans = ans.replace("+-", "-")
    print('Output Result:',ans)

result = {'': 1}
for coef in coefficients:
    temp = {}
    for res in result:
#         print("{0} : {1}".format(res, result[res]))
        var1 = decomposition(res.replace("^", ""))
#         print(var1)
        for key in coef:
#             print(key.replace("^", ""))
            var2 = decomposition(key.replace("^", ""))
#             print(var2)
            power = combine(var1, var2)
            temp = multiply(result[res], coef[key], power, temp)
#             print("{0} : {1}".format(key, coef[key]))
    result = temp.copy()
printPoly(result)        