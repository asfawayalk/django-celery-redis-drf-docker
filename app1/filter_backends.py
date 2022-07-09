from os import name
from rest_framework.filters import BaseFilterBackend

class NameFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, *args, **kwargs):
        name = request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)
        return queryset