import uuid
from .models import Client, DocumentRequest, RelationshipManager, Document
from django.core.mail import EmailMessage

class EmailService(object):
    def send_client_email(self, client, document_request):
        title = "Document Request"
        recipients = [client.email_address, client.relationship_manager.email_address]

        link = "localhost:8080/client_management/upload_document/" + document_request.uuid
        body = "You have a new document request. Please upload your requested document at: " + link + \
            "\nThe document requested is of type: " + document_request.document_type + "\nPlease note, " + \
            "for security reasons you can only upload once."

        self.send_mail(recipients, body, title)

    def send_relationship_manager_email(self, relationship_manager, document):
        client = document.client
        title = "Document submitted"
        recipients = [relationship_manager.email_address]
        link = "localhost:8080/client_management/download_document/" + str(document.id)
        body = "Your client, " + client.first_name + " " + client.surname + " has uploaded the document you requested." + \
            "Download link: " + link
        self.send_mail(recipients, body, title)

    def send_mail(self, recipients, body, title):
        email = EmailMessage(
                    title,
                    body,
                    'from@example.com',
                    list(recipients),
                    ['bcc@example.com'],
                    reply_to=['another@example.com'],
                    headers={'Message-ID': 'foo'},
                )

        email.send()

class DocumentRequestService(object):
    def create(self, client_id, document_type):
        client = Client.objects.get(id=client_id)
        document_request = DocumentRequest(
            uuid = str(uuid.uuid4()),
            client = client,
            uploaded = False,
            relationship_manager = RelationshipManager.objects.first(),
            document_type = document_type
        )
        document_request.save()

        EmailService().send_client_email(client, document_request)

class UploadDocumentService(object):
    def upload(self, document, document_request_uuid):
        document_request = DocumentRequest.objects.get(uuid=document_request_uuid)

        accepted_file_types = {
            'image/png': '.png',
            'text/csv': '.csv',
            'application/pdf': '.pdf'
        }

        extension = accepted_file_types.get(document.content_type)
        if extension == None:
            raise Exception("Sorry that file type is not allowed")

        filepath = 'files/' + str(document_request.id) + extension
        with open(filepath, 'wb+') as destination:
            for chunk in document.chunks():
                destination.write(chunk)
        document_request.uploaded = True
        document_request.save()
        document = Document(name=document.name, destination=filepath, client=document_request.client)
        document.save()

        EmailService().send_relationship_manager_email(document_request.relationship_manager, document)
