from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRecordHistoryChangeDto")



@_attrs_define
class OfficeRecordHistoryChangeDto:
    

    field_id: None | str | Unset = UNSET
    field_name: None | str | Unset = UNSET
    field_type: int | None | Unset = UNSET
    new_value: Any | Unset = UNSET
    old_value: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        field_type: int | None | Unset
        if isinstance(self.field_type, Unset):
            field_type = UNSET
        else:
            field_type = self.field_type

        new_value = self.new_value

        old_value = self.old_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if new_value is not UNSET:
            field_dict["newValue"] = new_value
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_field_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        field_type = _parse_field_type(d.pop("fieldType", UNSET))


        new_value = d.pop("newValue", UNSET)

        old_value = d.pop("oldValue", UNSET)

        office_record_history_change_dto = cls(
            field_id=field_id,
            field_name=field_name,
            field_type=field_type,
            new_value=new_value,
            old_value=old_value,
        )

        return office_record_history_change_dto

