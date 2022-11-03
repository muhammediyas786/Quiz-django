
from django.shortcuts import render
from django.shortcuts import redirect
from Quiz.models import *

# Create your views here.


def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{'categories':categories})





def questions_method(request,category,number=1):
    
    categ = Category.objects.get(name=category)
    if python_questions.objects.filter(category=categ,id=number):
        questions = python_questions.objects.filter(category=categ,id=number)
    elif django_questions.objects.filter(category=categ,id=number):
        questions = django_questions.objects.filter(category=categ,id=number)
    elif mathematical_questions.objects.filter(category=categ,id=number):
        questions = mathematical_questions.objects.filter(category=categ,id=number)
    elif spots_questions.objects.filter(category=categ,id=number):
        questions = spots_questions.objects.filter(category=categ,id=number)
    elif entertainment_questions.objects.filter(category=categ,id=number):
        questions = entertainment_questions.objects.filter(category=categ,id=number)
    elif technology_questions.objects.filter(category=categ,id=number):
        questions = technology_questions.objects.filter(category=categ,id=number)
    elif nature_questions.objects.filter(category=categ,id=number):
        questions = nature_questions.objects.filter(category=categ,id=number)
    elif history_questions.objects.filter(category=categ,id=number):
        questions = history_questions.objects.filter(category=categ,id=number)
    else:
        questions = movies_questions.objects.filter(category=categ,id=number)
    if request.method == 'POST':
        input = request.POST.get('input')
        if input:
            for i in questions:
                if input == i.answer:
                    print(input)
                    return render(request, 'questions.html',{'question':questions,'number':number,'answer':input})
                else:
                    print(input)
                    print(i.answer)
                    return render(request, 'questions.html',{'question':questions,'number':number,'input':input,'answer':i.answer})

        else:
            number = int(request.POST['number'])
            print('Number: ',type(number))
            number = number+1
            return redirect('questions',category,number)
    return render(request, 'questions.html',{'question':questions,'number':number})