from typing import Literal

OfficeGrantFolderPermissionRequestPermissionLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES: set[OfficeGrantFolderPermissionRequestPermissionLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_grant_folder_permission_request_permission_level(value: str) -> OfficeGrantFolderPermissionRequestPermissionLevel:
    if value in OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PERMISSION_LEVEL_VALUES!r}")
