from typing import Literal

OfficeGrantFolderPermissionRequestPrincipalType = Literal['Group', 'User']

OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES: set[OfficeGrantFolderPermissionRequestPrincipalType] = { 'Group', 'User',  }

def check_office_grant_folder_permission_request_principal_type(value: str) -> OfficeGrantFolderPermissionRequestPrincipalType:
    if value in OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_GRANT_FOLDER_PERMISSION_REQUEST_PRINCIPAL_TYPE_VALUES!r}")
