from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow unsafe methods if user is owner of object
    """
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # https://stackoverflow.com/questions/12906933/how-to-check-if-the-object-has-property-in-view-in-django
        # obj also self.model
        # wazne: musi istniec na modelu "owner"
        
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'author'):
            return obj.author == request.user
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # try:
        #     return obj.owner == request.user
        # except AttributeError:
        #     pass

