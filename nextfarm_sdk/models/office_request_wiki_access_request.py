from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_request_wiki_access_request_level import check_office_request_wiki_access_request_level
from ..models.office_request_wiki_access_request_level import OfficeRequestWikiAccessRequestLevel
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRequestWikiAccessRequest")



@_attrs_define
class OfficeRequestWikiAccessRequest:
    

    level: OfficeRequestWikiAccessRequestLevel | Unset = UNSET
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level


        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _level = d.pop("level", UNSET)
        level: OfficeRequestWikiAccessRequestLevel | Unset
        if isinstance(_level,  Unset):
            level = UNSET
        else:
            level = check_office_request_wiki_access_request_level(_level)




        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        office_request_wiki_access_request = cls(
            level=level,
            message=message,
        )

        return office_request_wiki_access_request

