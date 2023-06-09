
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from .models import Client, DocumentRequest, Document
from django.shortcuts import render
from .forms import RequestDocumentForm, UploadDocumentForm

from .services import DocumentRequestService, UploadDocumentService

import pdb

def index(request):
    return render(request, 'client_management/index.html', dict())
def error(request):
    return HttpResponse("error")

def documents(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {'documents': client.documents.all}
    return render(request, 'client_management/documents.html', context)

def request_document(request, client_id):
    if request.method == 'POST':
        form = RequestDocumentForm(request.POST)
        if form.is_valid():
            document_type = form.cleaned_data['document_type']
            DocumentRequestService().create(client_id, document_type)
            return HttpResponseRedirect('/client_management/clients')
    else:
        form = RequestDocumentForm()

    return render(request, 'name.html', {'form': form})

def download_document(request, document_id):
    document = Document.objects.get(id=document_id)
    return FileResponse(open('./' + document.destination, 'rb'), as_attachment=True)

def upload_document(request, document_request_uuid):
    document_request_invalid = DocumentRequest.objects.filter(uuid=document_request_uuid, uploaded=False).count() == 0
    if document_request_invalid:
        return HttpResponseRedirect('/client_management/error')

    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)

        if form.is_valid():
            UploadDocumentService().upload(request.FILES['document'], document_request_uuid)
            return HttpResponse('your document has been successfully uploaded. Thank you')


    context = {"document_request_uuid": document_request_uuid}
    return render(request, 'client_management/upload_document.html', context)

def clients(request):
    latest_clients_list = Client.objects.all()

    order_by_email = request.GET.get('order_by_email')
    order_by_name = request.GET.get('order_by_name')

    if order_by_email != None:
        latest_clients_list = latest_clients_list.order_by(int(order_by_email == 'desc') * '-' + 'email_address')
    if order_by_name != None:
        latest_clients_list = latest_clients_list.order_by(int(order_by_name == 'desc') * '-' + 'first_name')

    context = {'latest_clients_list': latest_clients_list, 'order_by_email': order_by_email, 'order_by_name': order_by_name}
    return render(request, 'client_management/clients.html', context)

def client(request, client_id):
    client_object = Client.objects.get(id=client_id)
    context = {'client': client_object}
    return render(request, 'client_management/client.html', context)
