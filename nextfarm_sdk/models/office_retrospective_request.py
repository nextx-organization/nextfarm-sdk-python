from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRetrospectiveRequest")



@_attrs_define
class OfficeRetrospectiveRequest:
    

    retrospective: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        retrospective: None | str | Unset
        if isinstance(self.retrospective, Unset):
            retrospective = UNSET
        else:
            retrospective = self.retrospective


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if retrospective is not UNSET:
            field_dict["retrospective"] = retrospective

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_retrospective(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retrospective = _parse_retrospective(d.pop("retrospective", UNSET))


        office_retrospective_request = cls(
            retrospective=retrospective,
        )

        return office_retrospective_request

