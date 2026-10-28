from typing import Literal

OfficeDocNodeShareDtoMyPermission = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_DOC_NODE_SHARE_DTO_MY_PERMISSION_VALUES: set[OfficeDocNodeShareDtoMyPermission] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_doc_node_share_dto_my_permission(value: str) -> OfficeDocNodeShareDtoMyPermission:
    if value in OFFICE_DOC_NODE_SHARE_DTO_MY_PERMISSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_SHARE_DTO_MY_PERMISSION_VALUES!r}")
