from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()

def pdf_reader(request):
    if request.method == "POST":

        file_pdf = request.FILES.get("sent_pdf_name")
        name_pdf = file_pdf.name
        final_name = fs.save(name_pdf, file_pdf)
        fs_url = fs.url(final_name)
        return render(request, "pdf2json/reader.html", context={"pdf_url": fs_url})
    
    return render(request, "pdf2json/reader.html")