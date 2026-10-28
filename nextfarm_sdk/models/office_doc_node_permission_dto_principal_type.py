from typing import Literal

OfficeDocNodePermissionDtoPrincipalType = Literal['Department', 'Group', 'Guest', 'User']

OFFICE_DOC_NODE_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES: set[OfficeDocNodePermissionDtoPrincipalType] = { 'Department', 'Group', 'Guest', 'User',  }

def check_office_doc_node_permission_dto_principal_type(value: str) -> OfficeDocNodePermissionDtoPrincipalType:
    if value in OFFICE_DOC_NODE_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES!r}")
