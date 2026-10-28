from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_share_wiki_page_request_level import check_office_share_wiki_page_request_level
from ..models.office_share_wiki_page_request_level import OfficeShareWikiPageRequestLevel
from ..models.office_share_wiki_page_request_principal_type import check_office_share_wiki_page_request_principal_type
from ..models.office_share_wiki_page_request_principal_type import OfficeShareWikiPageRequestPrincipalType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeShareWikiPageRequest")



@_attrs_define
class OfficeShareWikiPageRequest:
    

    level: OfficeShareWikiPageRequestLevel | Unset = UNSET
    principal_id: None | str | Unset = UNSET
    principal_type: OfficeShareWikiPageRequestPrincipalType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level


        principal_id: None | str | Unset
        if isinstance(self.principal_id, Unset):
            principal_id = UNSET
        else:
            principal_id = self.principal_id

        principal_type: str | Unset = UNSET
        if not isinstance(self.principal_type, Unset):
            principal_type = self.principal_type



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if level is not UNSET:
            field_dict["level"] = level
        if principal_id is not UNSET:
            field_dict["principalId"] = principal_id
        if principal_type is not UNSET:
            field_dict["principalType"] = principal_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _level = d.pop("level", UNSET)
        level: OfficeShareWikiPageRequestLevel | Unset
        if isinstance(_level,  Unset):
            level = UNSET
        else:
            level = check_office_share_wiki_page_request_level(_level)




        def _parse_principal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principal_id = _parse_principal_id(d.pop("principalId", UNSET))


        _principal_type = d.pop("principalType", UNSET)
        principal_type: OfficeShareWikiPageRequestPrincipalType | Unset
        if isinstance(_principal_type,  Unset):
            principal_type = UNSET
        else:
            principal_type = check_office_share_wiki_page_request_principal_type(_principal_type)




        office_share_wiki_page_request = cls(
            level=level,
            principal_id=principal_id,
            principal_type=principal_type,
        )

        return office_share_wiki_page_request

