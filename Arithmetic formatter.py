#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:12:34 2020

@author: sithlord-dev
"""
import operator
ops = { "+": operator.add, "-": operator.sub }
lst= list()

def arithmetic_arranger(eqs,arg=None) :
    if len(eqs) > 5 : 
        return print("Error: Too many problems.")
    else :
        i=0
        line_st = ''
        line_nd = ''
        line_rd = ''
        line_rth = ''
        for eq in eqs :
            terms = [eq.split()[0], eq.split()[-1]]
            oper = eq.split()[1]
            if arg is True :
                nmbs = [int(terms[0]),int(terms[-1])]
                l=len(sorted(terms,key=len,reverse=True)[0])+2
                total=str(ops[oper](nmbs[0],nmbs[1]))
                barre='-'*(l)
                term_st = (l-len(terms[0]))*' '+terms[0]
                term_nd = oper+(l-len(terms[-1])-1)*' '+terms[-1]
                term_rth = (l-len(total))*' '+total
                line_st = line_st+'    '+term_st
                line_nd = line_nd+'    '+term_nd
                line_rd = line_rd+'    '+barre
                line_rth = line_rth+'    '+term_rth
                i=i+1
            else : 
                l=len(sorted(terms,key=len,reverse=True)[0])+2
                barre='-'*(l)
                term_st = (l-len(terms[0]))*' '+terms[0]
                term_nd = oper+(l-len(terms[1])-1)*' '+terms[1]
                line_st = line_st+'    '+term_st
                #line_st = term_st+'    '+line_st
                line_nd = line_nd+'    '+term_nd
                #line_nd = term_nd+'    '+line_nd
                line_rd = line_rd+'    '+barre
                #line_rd = barre+'    '+line_rd
                i=i+1
        return print(line_st+'\n'+line_nd+'\n'+line_rd+'\n'+line_rth)
        
print('Welcome to this very simple arithmetic formatter.')
print('This program ony takes five equations at a time.') 
print('''Please, keep in mind to typer your equations with space between each 
      character and write \'done\' when you finish.''')

while True:
    inp = input('Enter an equation: ')
    if (inp == 'done') or (len(lst) == 5) : 
        break
    if len(inp.split()) == 3 :
        try :
            int(inp.split()[0])
            int(inp.split()[-1])
        except :
            print("Error: Numbers must only contain digits.")
            continue 
        if (len(inp.split()[0]) <= 4) and (len(inp.split()[-1]) <= 4):
            pass
        else :
            print("Error: Numbers cannot be more than four digits. Try again.")
            continue
        if (inp.split()[1]) in [k for k,v in ops.items()] :
            pass
        else :
            print("Error: Operator must be \'+\' or \'-\'.")
            continue
        lst.append(inp)
    else :
        print("Invalid input, try again")
        continue
arithmetic_arranger(lst)
arg_inp = input("Write 'Now' to show the result, or any other key to exit. ")
if arg_inp in {'Now','now'} :
    arithmetic_arranger(lst,True)
    
# =============================================================================
# import operator
# 
# def arithmetic_arranger(eqs,arg=None) :
#     if len(eqs) > 5 : 
#         return print("Error: Too many problems.")
#     else :
#         i=0
#         line_st = ''
#         line_nd = ''
#         line_rd = ''
#         line_rth = ''
#         ops = { "+": operator.add, "-": operator.sub }
#         for eq in eqs :
#             terms = [eq.split()[0], eq.split()[-1]]
#             oper = eq.split()[1]
#             if not (terms[0].isdigit() and terms[-1].isdigit()) :
#                 return print("Error: Numbers must only contain digits.")
#             elif (len(terms[0]) > 4) or (len(terms[-1]) > 4) :
#                 return print("Error: Numbers cannot be more than four digits.")
#             elif oper not in [k for k,v in ops.items()] :
#                 return print("Error: Operator must be \'+\' or \'-\'.")
#             elif arg is True :
#                 nmbs = [int(terms[0]),int(terms[-1])]
#                 l=len(sorted(terms,key=len,reverse=True)[0])+2
#                 total=str(ops[oper](nmbs[0],nmbs[1]))
#                 barre='-'*(l)
#                 term_st = (l-len(terms[0]))*' '+terms[0]
#                 term_nd = oper+(l-len(terms[-1])-1)*' '+terms[-1]
#                 term_rth = (l-len(total))*' '+total
#                 line_st = line_st+'    '+term_st
#                 line_nd = line_nd+'    '+term_nd
#                 line_rd = line_rd+'    '+barre
#                 line_rth = line_rth+'    '+term_rth
#                 i=i+1
#             else : 
#                 l=len(sorted(terms,key=len,reverse=True)[0])+2
#                 barre='-'*(l)
#                 term_st = (l-len(terms[0]))*' '+terms[0]
#                 term_nd = oper+(l-len(terms[1])-1)*' '+terms[1]
#                 line_st = line_st+'    '+term_st
#                 #line_st = term_st+'    '+line_st
#                 line_nd = line_nd+'    '+term_nd
#                 #line_nd = term_nd+'    '+line_nd
#                 line_rd = line_rd+'    '+barre
#                 #line_rd = barre+'    '+line_rd
#                 i=i+1
#         return print(line_st+'\n'+line_nd+'\n'+line_rd+'\n'+line_rth)
# 
# eqs = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
# arithmetic_arranger(eqs)
# =============================================================================


