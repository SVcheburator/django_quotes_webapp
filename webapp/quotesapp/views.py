from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .forms import TagForm, AuthorsForm, QuotesForm
from .models import Tag, Authors, Quotes


def quotes_list(request):
    quotes = Quotes.objects.all()

    for quote in quotes:
        try:
            quote.author.all()[0]
        except IndexError:
            quote_id = quote.id
            Quotes.objects.get(pk=quote_id).delete()
            quotes = Quotes.objects.all()

    return render(request, 'quotesapp/quotes_list.html', {"quotes": quotes})


def authors_list(request):
    authors = Authors.objects.all()
    return render(request, 'quotesapp/authors_list.html', {"authors": authors})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:quotes_list')
        else:
            return render(request, 'quotesapp/tag.html', {'form': form})

    return render(request, 'quotesapp/tag.html', {'form': TagForm()})


@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Authors.objects.all()

    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            choice_author = Authors.objects.filter(fullname__in=request.POST.getlist('authors'))
            for author in choice_author.iterator():
                new_quote.author.add(author)

            return redirect(to='quotesapp:quotes_list')
        else:
            return render(request, 'quotesapp/quote.html', {"tags": tags, 'authors': authors, 'form': form})

    return render(request, 'quotesapp/quote.html', {"tags": tags, 'authors': authors, 'form': QuotesForm()})


@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:authors_list')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})

    return render(request, 'quotesapp/author.html', {'form': AuthorsForm()})


def detail_q(request, quote_id):
    quote = get_object_or_404(Quotes, pk=quote_id)
    return render(request, 'quotesapp/detail_q.html', {"quote": quote})


def detail_a(request, quote_id=0, author_id=0):
    if quote_id != 0:
        quote = get_object_or_404(Quotes, pk=quote_id)
        author_id = quote.author.all()[0].id
    
    author = get_object_or_404(Authors, pk=author_id)

    author.born_date = author.born_date.date()

    return render(request, 'quotesapp/detail_a.html', {"author": author})


@login_required
def delete_quote(request, quote_id):
    Quotes.objects.get(pk=quote_id).delete()
    return redirect(to='quotesapp:quotes_list')


@login_required
def delete_author(request, author_id):
    Authors.objects.get(pk=author_id).delete()
    return redirect(to='quotesapp:authors_list')