from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from cats.models import Cat,Breed
from cats.forms import BreedForm


class MainView(LoginRequiredMixin, View):
    # login_url = reverse_lazy('login')
    def get(self, request):
        mc = Breed.objects.all().count()
        al = Cat.objects.all()
        cxt = {'breed_count' :mc, 'cat_list':al}
        return render(request, 'cats/cat_list.html',cxt)


class BreedView(LoginRequiredMixin, View):
    # login_url = reverse_lazy('login')
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'breed_list': ml}
        return render(request, 'cats/breed_list.html', ctx)


class BreedCreate(LoginRequiredMixin, View):
    # login_url = reverse_lazy('login')
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        Breed = form.save()
        return redirect(self.success_url)


class BreedUpdate(LoginRequiredMixin, View):
    # login_url = reverse_lazy('login')
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    def get(self, request, pk):
        Breed = get_object_or_404(self.model, pk = pk)
        form = BreedForm(instance=Breed)
        cxt = {'form':form}
        return render(request, self.template, cxt)

    def post(self, request, pk):
        Breed = get_object_or_404(self.model, pk = pk)
        form = BreedForm(request.POST, instance=Breed)
        if not form.is_valid:
            cxt = {'form':form}
            return render(request, self.template, cxt)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    # login_url = reverse_lazy('login')
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk):
        Breed = get_object_or_404(self.model, pk = pk)
        form = BreedForm(instance=Breed)
        cxt = {'form':form}
        return render(request, self.template, cxt)

    def post(self, request, pk):
        Breed = get_object_or_404(self.model, pk = pk)
        Breed.delete()
        return redirect(self.success_url)

class CatCreate(LoginRequiredMixin, CreateView):
    # login_url = reverse_lazy('login')
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    # login_url = reverse_lazy('login')
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    login_url = 'registration/login.html'
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

