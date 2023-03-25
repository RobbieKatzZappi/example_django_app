from django.db import models

class RelationshipManager(models.Model):
    first_name = models.CharField(max_length=200, default=None)
    surname = models.CharField(max_length=200, default=None)
    email_address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Client(models.Model):
    first_name = models.CharField(max_length=200, default=None)
    surname = models.CharField(max_length=200, default=None)
    email_address = models.CharField(max_length=200)
    relationship_manager = models.ForeignKey(RelationshipManager, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def document_count(self):
        return self.documents.count()
    def requested_document_count(self):
        return self.requested_documents.filter(uploaded=False).count()

class DocumentRequest(models.Model):
    uuid = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='requested_documents')
    relationship_manager = models.ForeignKey(RelationshipManager, models.SET_NULL, null=True)
    document_type = models.CharField(max_length=200)
    additional_notes = models.CharField(max_length=500)
    uploaded = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
