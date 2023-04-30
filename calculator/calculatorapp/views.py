from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import HomeForm


class HomePage(TemplateView):
    template_name = 'calculatorapp/index.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            if 'add' in request.POST:
                result = number1 + number2
            elif 'sub' in request.POST:
                result = number1 - number2
            elif 'mul' in request.POST:
                result = number1 * number2
            elif 'div' in request.POST:
                result = number1 / number2

        return render(request, self.template_name, context={'form': form, 'result': result})
