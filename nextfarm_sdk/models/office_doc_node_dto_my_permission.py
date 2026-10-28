from typing import Literal

OfficeDocNodeDtoMyPermission = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_DOC_NODE_DTO_MY_PERMISSION_VALUES: set[OfficeDocNodeDtoMyPermission] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_doc_node_dto_my_permission(value: str) -> OfficeDocNodeDtoMyPermission:
    if value in OFFICE_DOC_NODE_DTO_MY_PERMISSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_DTO_MY_PERMISSION_VALUES!r}")
