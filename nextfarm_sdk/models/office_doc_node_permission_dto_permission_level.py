from typing import Literal

OfficeDocNodePermissionDtoPermissionLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_DOC_NODE_PERMISSION_DTO_PERMISSION_LEVEL_VALUES: set[OfficeDocNodePermissionDtoPermissionLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_doc_node_permission_dto_permission_level(value: str) -> OfficeDocNodePermissionDtoPermissionLevel:
    if value in OFFICE_DOC_NODE_PERMISSION_DTO_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_PERMISSION_DTO_PERMISSION_LEVEL_VALUES!r}")
