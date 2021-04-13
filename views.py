from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    markdown = Markdown()
    entryPage= util.get_entry(entry)
    entryPage_converted = markdowner.convert(entryPage)
    if entryPage is None:
        return render(request, "encyclopedia/notFound.html", {
                "entryName" :entry
    })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "entry":markdowner.convert(entryPage)
                "entryName" :entry
    })




        

