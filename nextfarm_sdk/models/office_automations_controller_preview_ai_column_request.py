from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeAutomationsControllerPreviewAiColumnRequest")



@_attrs_define
class OfficeAutomationsControllerPreviewAiColumnRequest:
    

    field_id: UUID | Unset = UNSET
    record_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_id: str | Unset = UNSET
        if not isinstance(self.field_id, Unset):
            field_id = str(self.field_id)

        record_id: str | Unset = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = str(self.record_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field_id = d.pop("fieldId", UNSET)
        field_id: UUID | Unset
        if isinstance(_field_id,  Unset):
            field_id = UNSET
        else:
            field_id = UUID(_field_id)




        _record_id = d.pop("recordId", UNSET)
        record_id: UUID | Unset
        if isinstance(_record_id,  Unset):
            record_id = UNSET
        else:
            record_id = UUID(_record_id)




        office_automations_controller_preview_ai_column_request = cls(
            field_id=field_id,
            record_id=record_id,
        )

        return office_automations_controller_preview_ai_column_request

