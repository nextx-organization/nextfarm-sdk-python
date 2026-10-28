from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRecordSort")



@_attrs_define
class OfficeRecordSort:
    

    descending: bool | Unset = UNSET
    field_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        descending = self.descending

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if descending is not UNSET:
            field_dict["descending"] = descending
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        descending = d.pop("descending", UNSET)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("fieldId", UNSET))


        office_record_sort = cls(
            descending=descending,
            field_id=field_id,
        )

        return office_record_sort

