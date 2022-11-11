from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from autos.forms import MakeForm
from autos.models import Make,Auto


class MainView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()
        cxt = {'make_count' :mc, 'auto_list':al}
        return render(request, 'autos/auto_list.html',cxt)



class MakeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


class MakeCreate(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk = pk)
        form = MakeForm(instance=make)
        cxt = {'form':form}
        return render(request, self.template, cxt)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk = pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid:
            cxt = {'form':form}
            return render(request, self.template, cxt)

        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk = pk)
        form = MakeForm(instance=make)
        cxt = {'form':form}
        return render(request, self.template, cxt)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk = pk)
        make.delete()
        return redirect(self.success_url)

class AutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

