from typing import Literal

OfficeAddMemberRequestMemberType = Literal['Department', 'Group', 'User']

OFFICE_ADD_MEMBER_REQUEST_MEMBER_TYPE_VALUES: set[OfficeAddMemberRequestMemberType] = { 'Department', 'Group', 'User',  }

def check_office_add_member_request_member_type(value: str) -> OfficeAddMemberRequestMemberType:
    if value in OFFICE_ADD_MEMBER_REQUEST_MEMBER_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_ADD_MEMBER_REQUEST_MEMBER_TYPE_VALUES!r}")
