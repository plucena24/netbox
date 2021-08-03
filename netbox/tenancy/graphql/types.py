from tenancy import filtersets, models
from netbox.graphql.types import ObjectType, PrimaryObjectType

__all__ = (
    'TenantType',
    'TenantGroupType',
)


class TenantType(PrimaryObjectType):

    class Meta:
        model = models.Tenant
        fields = '__all__'
        filterset_class = filtersets.TenantFilterSet


class TenantGroupType(ObjectType):

    class Meta:
        model = models.TenantGroup
        fields = '__all__'
        filterset_class = filtersets.TenantGroupFilterSet
