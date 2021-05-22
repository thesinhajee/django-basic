from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

"""def surname(request):
    return HttpResponse('Hello')"""
def about(request):
    return render(request,'about.html')
    
def count(request):
    abc=request.GET['textbox']
    wordlist=abc.split()
    #print(wordlist)
    dictword={}
    for word in wordlist:
        if word in dictword:
            dictword[word]+=1
        else:
            dictword[word]=1

    sorteddict=sorted(dictword.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'textbox':abc,'count':len(wordlist),'dictword':sorteddict})
