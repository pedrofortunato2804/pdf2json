from django.http import HttpResponse
from django.shortcuts import render

def pdf_reader(request):
    if request.method == "POST":
        pdf2view = request.FILES
        return HttpResponse(pdf2view)
    
    return render(request, "pdf2json/reader.html")