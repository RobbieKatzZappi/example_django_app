from django.contrib import admin
from client_management.models import Client, RelationshipManager, Document, DocumentRequest

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

class RelationshipManagerAdmin(admin.ModelAdmin):
    pass
admin.site.register(RelationshipManager, RelationshipManagerAdmin)

class DocumentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Document, DocumentAdmin)

class DocumentRequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(DocumentRequest, DocumentRequestAdmin)
