from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from tablib import Dataset
from django.views.generic import View,TemplateView,ListView,DetailView
from .models  import *
from django.db.models import Q
from pymongo import MongoClient
from pprint import pprint


client = MongoClient()
db = client.movies_dataset
# Create your views here.
def index(request):
    movi = db.movi_metadata
    bills = movi.find({'adult': 'False'})[:10]
    context = {
    'movies': bills ,

    }
    return render(request, 'movi/index.html',context)

def listing(request):
    movi = db.movi_metadata
    if request.method == 'POST':
        key = request.POST.get('movie_name', None)
        list = movi.find({'original_title': {'$regex' : key}})[:5]
        #print(list)
        context = {'key' : list, }
        return render(request, 'movi/lists.html', context)

    else:
        return render(request, 'index.html')


def genre(request):
    movi = db.movi_metadata
    movies = Metadata.objects.all()[:12]
    if request.method == 'POST':
        keys = request.POST.get('movie_genre', None)
        # db.probCancer.aggregate([ { $unwind : "$cases" }, { $match : {"cases.level":-1}} ]);
        #listed = object(movi.aggregate([ { '$unwind'  : "$genres"} , { '$match' : {"genres.name":keys }}])[:10])
        #listed = movi.find( { 'title' : keys } )
        list = movi.find({'genres': {'$regex' : keys    }})[:12]
        context = {'keys' : list,'movies' : movies }
        return render(request, 'movi/genre.html', context)

    else:
        return render(request, 'index.html')



def vote(request):
    movi = db.movi_metadata
    if request.method == 'POST':
        vote1 = request.POST.get('vote_average', None)
        genres = request.POST.get('vote_genre', None)
        vote2 = float(vote1)

        #list = movi.find({'vote_average' : {'$gt' : 9}})
        list = movi.find({ '$and': [{ 'vote_average' : { '$gt' : vote2 } } , { 'revenue' : {'$gt' : 300000000 } } , { 'genres' : {'$regex' : genres} }]  })
        # for doc in list:
        #     pprint (doc)
        context = {'votes' : list, }
        return render(request, 'movi/lists2.html', context)

    else:
        return render(request, 'index.html')

def credit(request):
        movi = db.movi_metadata
        if request.method == 'POST':
            cred = request.POST.get('movie_credit', None)


            # for doc in hmm:
            #      pprint (doc)

            pipeline = [{'$lookup':
                    {'from' : 'movi_credits',
                     'localField' : 'id',
                     'foreignField' : 'id',
                     'as' : 'credits'}},
                     {'$match' :
                        {'title' : {'$regex' : cred } }
                     },
                     { '$limit' : 1},
                     {'$unwind' : '$credits'},
                     {'$unwind' : '$credits.crew'},
                     {'$project' :
                        {'credits.crew': 1 }
                     }
                 ]
            list = movi.aggregate(pipeline)
            # for doc in (movi.aggregate(pipeline)):
            #      pprint (doc)

            context = {'credits' : list, }
            return render(request, 'movi/index.html', context)
        else:
            return render(request, 'index.html')
