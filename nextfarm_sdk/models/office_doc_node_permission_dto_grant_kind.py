from typing import Literal

OfficeDocNodePermissionDtoGrantKind = Literal['DirectInvite', 'InheritedRule']

OFFICE_DOC_NODE_PERMISSION_DTO_GRANT_KIND_VALUES: set[OfficeDocNodePermissionDtoGrantKind] = { 'DirectInvite', 'InheritedRule',  }

def check_office_doc_node_permission_dto_grant_kind(value: str) -> OfficeDocNodePermissionDtoGrantKind:
    if value in OFFICE_DOC_NODE_PERMISSION_DTO_GRANT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_PERMISSION_DTO_GRANT_KIND_VALUES!r}")
