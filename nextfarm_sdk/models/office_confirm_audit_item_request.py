from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeConfirmAuditItemRequest")



@_attrs_define
class OfficeConfirmAuditItemRequest:
    

    actual_condition: None | str | Unset = UNSET
    is_matched: bool | Unset = UNSET
    note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        actual_condition: None | str | Unset
        if isinstance(self.actual_condition, Unset):
            actual_condition = UNSET
        else:
            actual_condition = self.actual_condition

        is_matched = self.is_matched

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if actual_condition is not UNSET:
            field_dict["actualCondition"] = actual_condition
        if is_matched is not UNSET:
            field_dict["isMatched"] = is_matched
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_actual_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_condition = _parse_actual_condition(d.pop("actualCondition", UNSET))


        is_matched = d.pop("isMatched", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        office_confirm_audit_item_request = cls(
            actual_condition=actual_condition,
            is_matched=is_matched,
            note=note,
        )

        return office_confirm_audit_item_request

