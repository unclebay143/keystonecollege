from django.shortcuts import render

# Create your views here.
def Science(request):
    context = {
    "hodscience":"Prof Ayodele Samuel Adebayo",
    "sciencebooks":['English', 'Mathematics', 'Introduction to Computing', 'Use of English','Geography']
    }
    return render(request, 'science.html',context)

def Art(request):
    context = {
    "hodart": "Prof. Aremu Adebayo",
    "artbooks":['Economics', 'Government', 'Commerce', 'Use of English','Literature in English']
    }
    return render(request, 'art.html', context)

def Commercial(request):
    context = {
    "hodcommerce":"Dr. Adewale Obaloluwa",
    "commercebooks":['Economics', 'Principle of Account', 'Commerce', 'Use of English','Literature in English']
    }
    return render(request, 'commercial.html',context)

def Contact(request):
    return render(request, 'contact.html')
