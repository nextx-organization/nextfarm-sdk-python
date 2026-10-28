from typing import Literal

OfficeFolderDtoMyPermission = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_FOLDER_DTO_MY_PERMISSION_VALUES: set[OfficeFolderDtoMyPermission] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_folder_dto_my_permission(value: str) -> OfficeFolderDtoMyPermission:
    if value in OFFICE_FOLDER_DTO_MY_PERMISSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_FOLDER_DTO_MY_PERMISSION_VALUES!r}")
