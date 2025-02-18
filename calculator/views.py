from django.shortcuts import render
from .forms import CalculatorForm

def calculate(request):
    result = None

    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            operation = form.cleaned_data["operation"]

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        else:
            print(form.errors)
    else:
        form = CalculatorForm()  

    return render(request, "calculator/calculate.html", {"form": form, "result": result})
