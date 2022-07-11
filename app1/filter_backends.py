from os import name
from rest_framework.filters import BaseFilterBackend
from rest_framework.compat import coreschema
import coreapi

class NameFilterBackend(BaseFilterBackend):

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name="name",
                location="query",
                required=False,
                schema=coreschema.String(
                    description="Filter by name")
            )
        ]

    def filter_queryset(self, request, queryset, *args, **kwargs):
        name = request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)
        return queryset