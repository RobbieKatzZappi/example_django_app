import uuid
from .models import Client, DocumentRequest, RelationshipManager, Document
class DocumentRequestService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance
    def create(client_id, document_type):
        client = Client.objects.get(id=client_id)
        document_request = DocumentRequest(
            uuid = str(uuid.uuid4()),
            client = client,
            uploaded = False,
            relationship_manager = RelationshipManager.objects.first(),
            document_type = document_type
        ).save()

        return True

class UploadDocumentService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

    def upload(document, document_request_uuid):
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
        Document(name=document.name, destination=filepath, client=document_request.client).save()
        return True
