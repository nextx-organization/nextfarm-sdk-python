from typing import Literal

OfficeGrantDocNodePermissionRequestPermissionLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES: set[OfficeGrantDocNodePermissionRequestPermissionLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_grant_doc_node_permission_request_permission_level(value: str) -> OfficeGrantDocNodePermissionRequestPermissionLevel:
    if value in OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_GRANT_DOC_NODE_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES!r}")
