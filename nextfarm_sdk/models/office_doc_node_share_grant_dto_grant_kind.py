from typing import Literal

OfficeDocNodeShareGrantDtoGrantKind = Literal['DirectInvite', 'InheritedRule']

OFFICE_DOC_NODE_SHARE_GRANT_DTO_GRANT_KIND_VALUES: set[OfficeDocNodeShareGrantDtoGrantKind] = { 'DirectInvite', 'InheritedRule',  }

def check_office_doc_node_share_grant_dto_grant_kind(value: str) -> OfficeDocNodeShareGrantDtoGrantKind:
    if value in OFFICE_DOC_NODE_SHARE_GRANT_DTO_GRANT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_SHARE_GRANT_DTO_GRANT_KIND_VALUES!r}")
