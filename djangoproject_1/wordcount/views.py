from django.shortcuts import render
import operator
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
     full_text = request.GET['fulltext']
 
     word_list = full_text.lower().split()
     
     word_dictionary = {}
 
     for word in word_list:
         if word in word_dictionary:
             # Increase
             word_dictionary[word] += 1
         else:
             # add to the dictionary
             word_dictionary[word] = 1

     sorted_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
     print(sorted_dictionary)

     return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list),'sorted_dictionary':sorted_dictionary})