from django.shortcuts import render

def contact(request):
	return render(request, 'contacts/contacts.html')

# Create your views here.
