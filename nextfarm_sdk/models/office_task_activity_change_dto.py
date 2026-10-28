from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeTaskActivityChangeDto")



@_attrs_define
class OfficeTaskActivityChangeDto:
    

    field: None | str | Unset = UNSET
    new_value: None | str | Unset = UNSET
    old_value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        new_value: None | str | Unset
        if isinstance(self.new_value, Unset):
            new_value = UNSET
        else:
            new_value = self.new_value

        old_value: None | str | Unset
        if isinstance(self.old_value, Unset):
            old_value = UNSET
        else:
            old_value = self.old_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field is not UNSET:
            field_dict["field"] = field
        if new_value is not UNSET:
            field_dict["newValue"] = new_value
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        def _parse_new_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_value = _parse_new_value(d.pop("newValue", UNSET))


        def _parse_old_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_value = _parse_old_value(d.pop("oldValue", UNSET))


        office_task_activity_change_dto = cls(
            field=field,
            new_value=new_value,
            old_value=old_value,
        )

        return office_task_activity_change_dto

