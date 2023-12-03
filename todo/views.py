from django.shortcuts import render

#create wiew here:
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')



