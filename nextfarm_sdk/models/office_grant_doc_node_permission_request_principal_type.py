from typing import Literal

OfficeGrantDocNodePermissionRequestPrincipalType = Literal['Department', 'Group', 'Guest', 'User']

OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES: set[OfficeGrantDocNodePermissionRequestPrincipalType] = { 'Department', 'Group', 'Guest', 'User',  }

def check_office_grant_doc_node_permission_request_principal_type(value: str) -> OfficeGrantDocNodePermissionRequestPrincipalType:
    if value in OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES!r}")
