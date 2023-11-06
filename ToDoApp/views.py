from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ToDo, Category
from .forms import AddCategoryForm


# Create your views here.


class CreateTodoView(CreateView):
    model = ToDo
    fields = '__all__'
    template_name = 'ToDoApp/form.html'
    context_object_name = 'tasks'
    success_url = 'todo/<int:pk>'
    value = 'Create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = 'Создание задачь'
        context['value'] = 'Создание задачи'
        return context


class UpdateTodoView(UpdateView):
    model = ToDo
    fields = '__all__'
    success_url = '/todo/{id}'
    template_name = 'ToDoApp/form.html'
    context_object_name = 'form'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_todo'] = 'Обновить задачу'
        context['update_text'] = True
        context['action'] = 'обновить'
        context['model'] = str(self.model)
        context['value'] = 'Обновление задачи'
        return context


class ToDoView(TemplateView):
    template_name = 'ToDoApp/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = ToDo.objects.all()
        return context


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = 'ToDoApp/todo_detail.html'
    context_object_name = 'tasks'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.get_object()
        categories = tasks.category
        context['categories'] = categories
        context['tasks'] = tasks
        # paginator = Paginator(posts, 2)
        # page_number: int = self.request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        # context['page_obj'] = page_obj
        # messages.success(self.request, 'Все посты этого автора найдены')
        # messages.warning(self.request, 'Возникла проблема')
        # messages.error(self.request, 'Ошибка')
        return context


class DeleteTodoView(DeleteView):
    model = ToDo
    template_name = 'ToDoApp/form.html'
    success_url = 'todo/<int:pk>'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vale'] = 'Удаление Задачи'
        return context


class CreateCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'ToDoApp/form.html'
    success_url = '/authors/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vale'] = 'Создание категории'
        return context

    def form_valid(self, form):
        return HttpResponse('form valid!'
                            'Категория зарегистрирована')

    def form_invalid(self, form):
        return HttpResponse('form invalid'
                            'Категория зарегистрирована')


class CategoryView(TemplateView):
    template_name = 'ToDoApp/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'ToDoApp/form.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Обновить категорию'
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'ToDoApp/category_detail.html'
    context_object_name = ''
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        tasks = category.categories.all()
        context['tasks'] = tasks
        return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['value'] = ''


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'ToDoApp/form.html'
    success_url = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Удаление категории'
        return context
