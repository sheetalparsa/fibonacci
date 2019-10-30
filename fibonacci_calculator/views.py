from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse


def multiply(a, b):
    # Creating an auxiliary matrix
    # to store elements of the
    # multiplication matrix
    mul = [[0 for x in range(2)]
            for y in range(2)]
    for i in range(2):
        for j in range(2):
            mul[i][j] = 0
            for k in range(2):
                mul[i][j] += a[i][k] * b[k][j]

                # storing the multiplication
    # result in a[][]
    for i in range(2):
        for j in range(2):
            a[i][j] = mul[i][j]  # Updating our matrix
    return a


def power(F, n):
    if n == 0 or n == 1:
        return

    M = [[1, 1], [1, 0]]

    power(F, int(n / 2))
    F = multiply(F, F)

    if n % 2 != 0:
        F = multiply(F, M)



def findNthTerm(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    power(F, n)

    return F[0][1]


def index(request):
    template = loader.get_template('fibonacci_calculator/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def calc_fib(request):

    n = int(request.GET.get('N'))
    data = {
        'result': str(findNthTerm(n))
    }

    return JsonResponse(data)

