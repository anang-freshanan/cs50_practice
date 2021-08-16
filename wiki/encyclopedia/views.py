import random


from django import forms
from django.shortcuts import render, redirect

from . import util

from markdown2 import Markdown

markdowner = Markdown()

class NewForm(forms.Form):
    title = forms.CharField(label="Entry title", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-8', 'rows' : 10}))
   
class EditForm(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    
    webpage = util.get_entry(title)
    if webpage == None:
        return render(request, "encyclopedia/error.html", {
            "title": title
                 
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(webpage),
            "title": title
        })


def search(request):
    query = request.GET.get("q", "")
    if query == None or query == "":
        return render(
            request,
            "encyclopedia/search.html",
            {"searched_entries": "", "query": query},
        )

    entries = util.list_entries()

    searched_entries = [
        valid_entry
        for valid_entry in entries
        if query.lower() in valid_entry.lower()
    ]
    if len(searched_entries) == 1:
        return redirect("entry", searched_entries[0])

    return render(
        request,
        "encyclopedia/search.html",
        {"searched_entries": searched_entries, "query": query},
    )


def new(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if(util.get_entry(title) is None):
                util.save_entry(title,content)
                return redirect("entry", title=title)
            else:
                return render(request, "encyclopedia/new.html", {
                "form": form,
                "existing": True,
                "entry": title
                })
        else:
            return render(request, "encyclopedia/new.html", {
            "form": form,
            "existing": False
            })
    else:
        return render(request,"encyclopedia/new.html", {
            "form": NewForm(),
            "existing": False
        })    
    
       

def edit(request, title):
     if request.method == 'GET':
        page = util.get_entry(title)
        
        context = {
            'form': NewForm(),
            'edit': EditForm(initial={'textarea': page}),
            'title': title
        }

        return render(request, "encyclopedia/edit.html", context)
     else:
        form = EditForm(request.POST) 
        if form.is_valid():
            textarea = form.cleaned_data["textarea"]
            util.save_entry(title,textarea)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)

            context = {
                'form': NewForm(),
                'page': page_converted,
                'title': title
            }

            return render(request, "encyclopedia/entry.html", context)
    

    
def random_page(request):
    return entry(request,random.choice( util.list_entries()))
    


   



