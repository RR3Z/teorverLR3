import math
from enum import Enum
from scipy.stats import laplace
from scipy import integrate
from math import cos, pi
import numpy as np

class FormulaType(Enum):
    EQUALITY = 0
    LOWER = 1
    HIGHEREQUAL = 2
    INTERVAL = 3


def sochetNoRepeat(n : int, k : int):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def perestanovRepeat(n : int, m : list):
    res = math.factorial(n)
    for currentM in range(len(m)):
        res = res // math.factorial(int(m[currentM]))
    return res

def bernulli(p : float, n : int, m1 : int, m2 : int, type : FormulaType):
    # Сделай switch case с выбором всех возможных type для формулы Бернулли
    if type == FormulaType.EQUALITY:
        return sochetNoRepeat(n, m1) * (p ** m1) * ((1 - p) ** (n - m1))
    elif type == FormulaType.LOWER:
        return sum([sochetNoRepeat(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(0, m1)])
    elif type == FormulaType.HIGHEREQUAL:
        return sum([sochetNoRepeat(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(m1, n)])
    elif type == FormulaType.INTERVAL:
        return bernulli(p, n, m1, m2, FormulaType.HIGHEREQUAL) - bernulli(p, n, m2 + 1, 0, FormulaType.HIGHEREQUAL)
    
    
#Напиши программу, которя позволяет вычислить вероятности событий по полиномиальной формуле Бернулли
#Например, для Pn(m1,m2,m3) = n!/m1!m2!m3! ... mk! * p1^m1 * p2^m2 * p3^m3 * ... pk^mk, где m1+m2+...+mk=n
#Функция должна принимать на вход n, p1, p2, p3, ... pk, m1, m2, m3, ... mk
def bernulliPolynom(n : int, p : list, m : list):
    if len(p) != len(m):
        return -1
    fraction = perestanovRepeat(n, m)
    for currentP in range(len(p)):
        fraction = fraction * (p[currentP] ** m[currentP])
    return fraction


#напиши функцию которая возводит эксопненту в степень -x^2/2
func = lambda x: math.e ** (-x ** 2 / 2)

def laplace(x):
    return (1/math.sqrt(2*math.pi))*integrate.fixed_quad(func, 0, x, n = 1000)[0]

#Напиши функцию которая вычисляет вероятность по интегральной теореме Муара-Лапласа
#Функция должна принимать на вход n, m1 - левая граница интервала, m2 - правая граница интервала, p
def muavLaplasLib(n : int, m1 : int, m2 : int, p : float):
    #Напиши реализацию
    arg1 = (m2 - n * p) / math.sqrt(n * p * (1 - p))
    arg2 = (m1 - n * p) / math.sqrt(n * p * (1 - p))
    arg1 = round(arg1, 5)
    arg2 = round(arg2, 5)
    return laplace(arg1) - laplace(arg2)


def simpson_rule(f, a, b, n):
    h = (b - a) / (2 * n)
    x = [a + i * h for i in range(2 * n + 1)]
    y = [f(x[i]) for i in range(2 * n + 1)]
    integral = (b - a) / (6 * n) * sum([y[i-1] + 4 * y[i] + y[i+1] for i in range(1, 2*n, 2)])
    return integral

def laplace2(x):
    return (1/math.sqrt(2*math.pi))*simpson_rule(func, 0, x, 10)

def muavLaplaceSimpson(n : int, m1 : int, m2 : int, p : float):
    #Напиши реализацию
    arg1 = (m2 - n * p) / math.sqrt(n * p * (1 - p))
    arg2 = (m1 - n * p) / math.sqrt(n * p * (1 - p))
    arg1 = round(arg1, 5)
    arg2 = round(arg2, 5)
    return laplace2(arg1) - laplace2(arg2)





