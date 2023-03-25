
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Client, DocumentRequest
from django.shortcuts import render
from .forms import RequestDocumentForm
from .services import DocumentRequestService

def index(request):
    return HttpResponse("client management index")

def request_document(request, client_id):
    if request.method == 'POST':
        form = RequestDocumentForm(request.POST)
        if form.is_valid():
            document_type = form.cleaned_data['document_type']
            DocumentRequestService.create(client_id, document_type)
            return HttpResponseRedirect('/client_management/clients')
    else:
        form = RequestDocumentForm()

    return render(request, 'name.html', {'form': form})

def clients(request):
    latest_clients_list = Client.objects.all()
    context = {'latest_clients_list': latest_clients_list}
    return render(request, 'client_management/clients.html', context)

def client(request, client_id):
    client_object = Client.objects.get(id=client_id)
    context = {'client': client_object}
    return render(request, 'client_management/client.html', context)
