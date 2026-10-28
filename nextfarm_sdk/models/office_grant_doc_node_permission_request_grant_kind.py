from typing import Literal

OfficeGrantDocNodePermissionRequestGrantKind = Literal['DirectInvite', 'InheritedRule']

OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_GRANT_KIND_VALUES: set[OfficeGrantDocNodePermissionRequestGrantKind] = { 'DirectInvite', 'InheritedRule',  }

def check_office_grant_doc_node_permission_request_grant_kind(value: str) -> OfficeGrantDocNodePermissionRequestGrantKind:
    if value in OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_GRANT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_GRANT_KIND_VALUES!r}")
