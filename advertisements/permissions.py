from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        print(f'Ответ сервера user: {request.user}')
        print(f'Ответ сервера obj: {obj.creator}')
        return request.user == obj.creator
       