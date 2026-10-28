from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_merge_field_dto import OfficeMergeFieldDto





T = TypeVar("T", bound="OfficeAutomationMergeFieldGroupDto")



@_attrs_define
class OfficeAutomationMergeFieldGroupDto:
    

    fields: list[OfficeMergeFieldDto] | None | Unset = UNSET
    label: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET
    step_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_merge_field_dto import OfficeMergeFieldDto # noqa: PLC0415
        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)


        else:
            fields = self.fields

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        step_id: None | str | Unset
        if isinstance(self.step_id, Unset):
            step_id = UNSET
        elif isinstance(self.step_id, UUID):
            step_id = str(self.step_id)
        else:
            step_id = self.step_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if label is not UNSET:
            field_dict["label"] = label
        if scope is not UNSET:
            field_dict["scope"] = scope
        if step_id is not UNSET:
            field_dict["stepId"] = step_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_merge_field_dto import OfficeMergeFieldDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_fields(data: object) -> list[OfficeMergeFieldDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in (_fields_type_0):
                    fields_type_0_item = OfficeMergeFieldDto.from_dict(fields_type_0_item_data)



                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeMergeFieldDto] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        def _parse_step_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                step_id_type_0 = UUID(data)



                return step_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        step_id = _parse_step_id(d.pop("stepId", UNSET))


        office_automation_merge_field_group_dto = cls(
            fields=fields,
            label=label,
            scope=scope,
            step_id=step_id,
        )

        return office_automation_merge_field_group_dto

