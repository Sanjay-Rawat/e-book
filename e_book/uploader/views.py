from django.shortcuts import render
from uploader.models import Books
from e_book.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
import os
import string
import random
from itertools import groupby

def home(request):  
     abc=getBooks()   
     return render(request,'index.html',{'tabs':abc})

def upload(request):   
     if(request.method=='POST'):
          name = request.POST.get('name')
          author = request.POST.get('author')
          about = request.POST.get('about')
          category = request.POST.get('category')
          isForMembers = request.POST.get('isForMembers')
          fileUrl = file_uploader(request.FILES['pdf'])
          posterUrl = file_uploader(request.FILES['poster'])
          data=Books(name=name,author=author,about=about,category=category,fileUrl=fileUrl,posterUrl=posterUrl,isForMembers=True if isForMembers=='on' else False)
          data.save()          
     return render(request,'upload.html')



def file_uploader(file):
    filename=getRandomStr()+file.name  
    path=os.path.join(BASE_DIR, "static_files/"+filename)
    fs = FileSystemStorage()
    fs.save(path, file)
    return '/assets/'+filename

def getRandomStr(): 
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return str(res)



def getBooks():
    try:
        books= Books.objects.all().order_by('category')
    except:
        books=[]
    if(len(books)==0):
        return []
    result=[]
    temp=[]
    current=books[0].category 
    for book in books:
        if(book.category==current):
            temp.append(book)
        else:
            result.append({"tabName":temp[0].category.title() ,"books":chunkIt(temp,3)})
            current=book.category 
            temp=[]
            temp.append(book)
    
    if(len(temp)>0):
        result.append({"tabName":temp[0].category.title() ,"books":chunkIt(temp,3)})
    print(result)
    return result


def chunkIt(my_list, n):
    return [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 

