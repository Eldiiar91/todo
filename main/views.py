from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("This is my first page")

def x=int(input("Введите число: "))
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz", end=' ')
elif x % 3 == 0:
    print("Fizz", end=' ')
elif x % 5 == 0:
    print("Buzz", end=' ')
else:
    print(x, end=' ')

def test3(request):
    return HttpResponse("This is page test3")