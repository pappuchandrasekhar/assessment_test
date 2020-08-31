from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Questions

# Create your views here.
def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user_check = authenticate(username=user_name, password=password)
        if user_check is not None:
            return redirect("/exam")
        else:
            print("user details are not correct")
    return render(request, 'examtest/login.html')



def exam(request):
    question_data = Questions.objects.all()
    if request.method == 'POST':
        #print(request.POST.getlist('question_ids[]'))
        question_ids = request.POST.getlist('question_ids[]')
        answer1 = request.POST.get('answer1[]')
        answer2 = request.POST.get('answer2[]')
        answer3 = request.POST.get('answer3[]')
        answer4 = request.POST.get('answer4[]')
        answer5 = request.POST.get('answer5[]')
        store_list = [question_ids, [answer1, answer2, answer3, answer4, answer5]]
        Questions.objects.bulk_create(store_list)

        #print(store_list)

        # print(request.POST.getlist('answer1[]'))
        # print(request.POST.getlist('answer2[]'))
        # print(request.POST.getlist('answer3[]'))
        # print(request.POST.getlist('answer4[]'))
        # print(request.POST.getlist('answer5[]'))


    return render(request, 'examtest/exam.html',{'question_data': question_data})
