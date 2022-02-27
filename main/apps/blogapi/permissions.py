# setup custom permissions if project level permissions are not to be used.

from rest_framework import permissions


class BasePermission(object):
    '''a base parent class to inherit all permission classes'''

    def has_permission(self, request, view):
        '''Return True for permissions granted, else False'''
        return True

    def has_object_permission(self, request, view, obj):
        '''return True for permissions granted, else False'''
        return True
