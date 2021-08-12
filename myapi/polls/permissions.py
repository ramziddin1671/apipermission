from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqat korish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        # ozgartirishlar faqat avtorning o'zigagina mumkun
        return obj.author ==request.user
