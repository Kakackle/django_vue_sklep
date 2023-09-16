from rest_framework import permissions
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Only allow unsafe methods if user is owner of object
#     """
#     edit_methods = ("PUT", "PATCH")

#     def has_permission(self, request, view):
#         # if request.user.is_authenticated:
#         #     return True
#         edit_methods = ("PUT", "PATCH")

#         if request.method not in edit_methods:
#             return True
#         # return super().has_permission(request, view)

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True       
#         print('please')
#         # https://stackoverflow.com/questions/12906933/how-to-check-if-the-object-has-property-in-view-in-django
#         # obj also self.model
#         # wazne: musi istniec na modelu "owner"
        
#         # if hasattr(obj, 'owner'):
#         #     # print('owner')
#         #     return obj.owner == request.user
#         # if hasattr(obj, 'author'):
#         #     return obj.author == request.user
#         # if hasattr(obj, 'user'):
#         #     return obj.user == request.user
        
#         # if obj.owner == request.user:
#         #     return True
    
#         try:
#             return obj.owner == request.user
#         except AttributeError:
#             return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    