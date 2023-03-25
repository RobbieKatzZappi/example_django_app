import uuid
from .models import Client, DocumentRequest, RelationshipManager
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
