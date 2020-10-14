from django.shortcuts import render, redirect
from .forms import ExpenseModelForm, ProfileModelForm
from .models import Profile, Expense


def home(request):
    if request.method == 'POST':
        csrf, budget, first_name, last_name = request.POST.values()
        Profile.objects.create(first_name=first_name,
                               last_name=last_name,
                               budget=budget)

    user = Profile.objects.last()
    if not user:
        form = ProfileModelForm()
        return render(request, 'home-no-profile.html', {'form': form})

    context = {'expenses': Expense.objects.all(),
               'user': user,
               'budget_left': get_budget()}

    return render(request, 'home-with-profile.html', context)


def get_object(task_pk):
    try:
        return Expense.objects.get(pk=task_pk)
    except (Expense.DoesNotExist, ValueError):
        return None


def get_budget():
    user = Profile.objects.last()
    expenses = Expense.objects.all()
    return user.budget - sum([expense.price for expense in expenses])


def create_expense(request):
    if request.method == 'POST':
        csrf, title, description, image_url, price = request.POST.values()
        Expense.objects.create(title=title,
                               description=description,
                               image_url=image_url,
                               price=price)
        return redirect('home')

    context = {'form': ExpenseModelForm()}
    return render(request, 'expense/expense-create.html', context)


def edit_expense(request, pk):
    expense = get_object(pk)

    if request.method == 'POST':
        expense = ExpenseModelForm(request.POST, instance=expense)
        if expense.is_valid():
            expense.save()
            return redirect('home')
    context = {'form': ExpenseModelForm(instance=expense)}
    return render(request, 'expense/expense-edit.html', context)


def delete_expense(request, pk):
    expense = get_object(pk)
    form = ExpenseModelForm(instance=expense)

    if request.method == 'POST':
        expense.delete()
        return redirect('home')

    for field in form.fields:
        form.fields[field].widget.attrs.update({'disabled': ""})

    context = {'form': form}
    return render(request, 'expense/expense-delete.html', context)


def profile(request):
    user = Profile.objects.last()
    context = {'user': user, 'budget_left': get_budget()}
    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    user = Profile.objects.last()

    if request.method == 'POST':
        user = ProfileModelForm(request.POST, instance=user)
        if user.is_valid():
            user.save()
            return redirect('home')
    context = {'form': ProfileModelForm(instance=user)}
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        user = Profile.objects.last()
        user.delete()
        objects = Expense.objects.all()
        objects.delete()
        return redirect('home')
    return render(request, 'profile/profile-delete.html')
