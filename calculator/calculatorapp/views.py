from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import HomeForm


class HomePage(TemplateView):
    template_name = 'calculatorapp/index.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            if 'add' in request.POST:
                result = num1 + num2
            elif 'sub' in request.POST:
                result = num1 - num2
            elif 'mul' in request.POST:
                result = num1 * num2
            elif 'div' in request.POST:
                result = num1 / num2

            form = HomeForm()

        return render(request, self.template_name, context={'form': form, 'result': result})
