from django.db import models

class RelationshipManager(models.Model):
    email_address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Client(models.Model):
    email_address = models.CharField(max_length=200)
    relationship_manager = models.ForeignKey(RelationshipManager, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DocumentRequest(models.Model):
    uuid = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    relationship_manager = models.ForeignKey(RelationshipManager, models.SET_NULL, null=True)
    document_type = models.CharField(max_length=200)
    additional_notes = models.CharField(max_length=500)
    uploaded = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
