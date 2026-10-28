from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeUpdateRecordRequest")



@_attrs_define
class OfficeUpdateRecordRequest:
    

    data: Any | Unset = UNSET
    expected_values: Any | Unset = UNSET
    replace: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data = self.data

        expected_values = self.expected_values

        replace = self.replace


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if expected_values is not UNSET:
            field_dict["expectedValues"] = expected_values
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        expected_values = d.pop("expectedValues", UNSET)

        replace = d.pop("replace", UNSET)

        office_update_record_request = cls(
            data=data,
            expected_values=expected_values,
            replace=replace,
        )

        return office_update_record_request

