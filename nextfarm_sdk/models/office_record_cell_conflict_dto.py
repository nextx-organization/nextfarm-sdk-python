from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeRecordCellConflictDto")



@_attrs_define
class OfficeRecordCellConflictDto:
    

    current_value: None | str | Unset = UNSET
    field_id: None | str | Unset = UNSET
    field_name: None | str | Unset = UNSET
    submitted_value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        current_value: None | str | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

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

        submitted_value: None | str | Unset
        if isinstance(self.submitted_value, Unset):
            submitted_value = UNSET
        else:
            submitted_value = self.submitted_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if submitted_value is not UNSET:
            field_dict["submittedValue"] = submitted_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_current_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_value = _parse_current_value(d.pop("currentValue", UNSET))


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


        def _parse_submitted_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitted_value = _parse_submitted_value(d.pop("submittedValue", UNSET))


        office_record_cell_conflict_dto = cls(
            current_value=current_value,
            field_id=field_id,
            field_name=field_name,
            submitted_value=submitted_value,
        )

        return office_record_cell_conflict_dto

