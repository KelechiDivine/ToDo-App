from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/notes',
            'method': 'GET',
            'body':None,
            'description': 'Return an array of notes'
        },
        
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Return a single notes object'
        },
        
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new notes with data sent in the post request'
        },
    
        {
            'Endpoint': '/notes/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in the note'
        },
    
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing notes'
        },
    ]
    
    return JsonResponse(routes, safe= False)
