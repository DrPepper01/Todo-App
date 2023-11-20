from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ToDo, Category
from .forms import AddCategoryForm, AddTodoForm
from django.contrib import messages


# Create your views here.


class CreateTodoView(CreateView):
    model = ToDo
    form_class = AddTodoForm
    template_name = 'ToDoApp/new_form.html'
    success_url = 'todo/{id}'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = 'Создание задачь'
        context['value'] = 'Создать задачу'
        return context

    def form_valid(self, form):
        '''
        :is_valid() - проверяет коректность формы
        :redirect - внутри этой команды мы сначала переходим по первому значению
        затем туда вставляется наш PK и в это время мы применяем form.save()
        '''
        if form.is_valid():
            firma = form.save()
            return redirect('todo_detail', firma.pk)

    def form_invalid(self, form):
        return HttpResponse('Что то пошло не так, Задача не была создана =(')


class UpdateTodoView(UpdateView):
    model = ToDo
    form_class = AddTodoForm
    success_url = '/todo/{id}'
    template_name = 'ToDoApp/form.html'
    context_object_name = 'form'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_todo'] = 'Обновить задачу'
        context['update_text'] = True
        context['action'] = 'обновить'
        context['model'] = str(self.model)
        context['value'] = 'Обновление задачи'
        context['btn_value'] = 'Обновить'
        return context

    # def check_valid(self,request):
    #     if form.is_valid

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse('Что то пошло не так, Задача не обновлена =(')


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
    success_url = reverse_lazy("todo_list")
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo = self.get_object()
        context['tasks'] = todo
        context['value'] = 'Удаление Задачи'
        context['btn_value'] = 'Удалить'
        messages.warning(self.request, f'Вы хотите удалить задачу {todo}? ')
        return context

    def form_invalid(self, form):
        return HttpResponse('Что то пошло не так, Задача не удалена =(')


class CreateCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'ToDoApp/form.html'
    success_url = '/authors/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Создание категории'
        context['btn_value'] = 'Создать'
        return context

    def form_valid(self, form):
        """
        :is_valid() - проверяет коректность формы
        :redirect - внутри этой команды мы сначала переходим по первому значению
        затем туда вставляется наш PK и в это время мы применяем form.save()
        """
        if form.is_valid():
            firma = form.save()
            return redirect('category_detail', firma.pk)

    def form_invalid(self, form):
        return HttpResponse('Что то пошло не так, Категория не была создана =(')


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
    success_url = '/categories/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Обновить категорию'
        context['btn_value'] = 'Обновить'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponse('Что то пошло не так, Категория не обновилась =(')


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


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'ToDoApp/form.html'
    success_url = reverse_lazy('category_list')
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['category'] = category
        context['value'] = 'Удаление Категории'
        context['btn_value'] = 'Удалить'
        messages.warning(self.request, f'Вы хотите удалить категорию {category}? ')
        return context