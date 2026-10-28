from typing import Literal

OfficeFolderPermissionDtoPermissionLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_FOLDER_PERMISSION_DTO_PERMISSION_LEVEL_VALUES: set[OfficeFolderPermissionDtoPermissionLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_folder_permission_dto_permission_level(value: str) -> OfficeFolderPermissionDtoPermissionLevel:
    if value in OFFICE_FOLDER_PERMISSION_DTO_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_FOLDER_PERMISSION_DTO_PERMISSION_LEVEL_VALUES!r}")
