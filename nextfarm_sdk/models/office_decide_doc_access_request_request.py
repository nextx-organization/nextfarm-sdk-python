from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_decide_doc_access_request_request_granted_level import check_office_decide_doc_access_request_request_granted_level
from ..models.office_decide_doc_access_request_request_granted_level import OfficeDecideDocAccessRequestRequestGrantedLevel
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDecideDocAccessRequestRequest")



@_attrs_define
class OfficeDecideDocAccessRequestRequest:
    

    granted_level: OfficeDecideDocAccessRequestRequestGrantedLevel | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        granted_level: str | Unset = UNSET
        if not isinstance(self.granted_level, Unset):
            granted_level = self.granted_level



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if granted_level is not UNSET:
            field_dict["grantedLevel"] = granted_level

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _granted_level = d.pop("grantedLevel", UNSET)
        granted_level: OfficeDecideDocAccessRequestRequestGrantedLevel | Unset
        if isinstance(_granted_level,  Unset):
            granted_level = UNSET
        else:
            granted_level = check_office_decide_doc_access_request_request_granted_level(_granted_level)




        office_decide_doc_access_request_request = cls(
            granted_level=granted_level,
        )

        return office_decide_doc_access_request_request

