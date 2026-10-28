from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAiCellResult")



@_attrs_define
class OfficeAiCellResult:
    

    changed: bool | Unset = UNSET
    field_id: None | str | Unset = UNSET
    field_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    skipped: bool | Unset = UNSET
    value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        field_name: None | str | Unset
        if isinstance(self.field_name, Unset):
            field_name = UNSET
        else:
            field_name = self.field_name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        skipped = self.skipped

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if changed is not UNSET:
            field_dict["changed"] = changed
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("fieldId", UNSET))


        def _parse_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_name = _parse_field_name(d.pop("fieldName", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        skipped = d.pop("skipped", UNSET)

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        office_ai_cell_result = cls(
            changed=changed,
            field_id=field_id,
            field_name=field_name,
            reason=reason,
            skipped=skipped,
            value=value,
        )

        return office_ai_cell_result

