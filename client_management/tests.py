from django.test import TestCase
from client_management.models import Client, DocumentRequest, Document

class ClientTestCase(TestCase):
    def setUp(self):
        client = Client.objects.create(first_name='foo', surname='bar')
        DocumentRequest.objects.create(client=client, uploaded=False)
        DocumentRequest.objects.create(client=client, uploaded=True)
        Document.objects.create(client=client)
        Document.objects.create(client=client)

    def test_client_document_count(self):
        client = Client.objects.get(first_name = 'foo')
        self.assertEqual(client.document_count(), 2)
    def test_client_requested_document_count(self):
        client = Client.objects.get(first_name = 'foo')
        self.assertEqual(client.requested_document_count(), 1)
