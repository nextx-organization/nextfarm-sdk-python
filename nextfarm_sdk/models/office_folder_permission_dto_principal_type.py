from typing import Literal

OfficeFolderPermissionDtoPrincipalType = Literal['Group', 'User']

OFFICE_FOLDER_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES: set[OfficeFolderPermissionDtoPrincipalType] = { 'Group', 'User',  }

def check_office_folder_permission_dto_principal_type(value: str) -> OfficeFolderPermissionDtoPrincipalType:
    if value in OFFICE_FOLDER_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_FOLDER_PERMISSION_DTO_PRINCIPAL_TYPE_VALUES!r}")
