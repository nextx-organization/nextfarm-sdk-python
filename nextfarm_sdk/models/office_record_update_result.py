from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_record_cell_conflict_dto import OfficeRecordCellConflictDto





T = TypeVar("T", bound="OfficeRecordUpdateResult")



@_attrs_define
class OfficeRecordUpdateResult:
    

    applied: bool | Unset = UNSET
    conflicts: list[OfficeRecordCellConflictDto] | None | Unset = UNSET
    message: None | str | Unset = UNSET
    message_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_cell_conflict_dto import OfficeRecordCellConflictDto # noqa: PLC0415
        applied = self.applied

        conflicts: list[dict[str, Any]] | None | Unset
        if isinstance(self.conflicts, Unset):
            conflicts = UNSET
        elif isinstance(self.conflicts, list):
            conflicts = []
            for conflicts_type_0_item_data in self.conflicts:
                conflicts_type_0_item = conflicts_type_0_item_data.to_dict()
                conflicts.append(conflicts_type_0_item)


        else:
            conflicts = self.conflicts

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        message_key: None | str | Unset
        if isinstance(self.message_key, Unset):
            message_key = UNSET
        else:
            message_key = self.message_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if applied is not UNSET:
            field_dict["applied"] = applied
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts
        if message is not UNSET:
            field_dict["message"] = message
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_cell_conflict_dto import OfficeRecordCellConflictDto # noqa: PLC0415
        d = dict(src_dict)
        applied = d.pop("applied", UNSET)

        def _parse_conflicts(data: object) -> list[OfficeRecordCellConflictDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conflicts_type_0 = []
                _conflicts_type_0 = data
                for conflicts_type_0_item_data in (_conflicts_type_0):
                    conflicts_type_0_item = OfficeRecordCellConflictDto.from_dict(conflicts_type_0_item_data)



                    conflicts_type_0.append(conflicts_type_0_item)

                return conflicts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRecordCellConflictDto] | None | Unset, data)

        conflicts = _parse_conflicts(d.pop("conflicts", UNSET))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        def _parse_message_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_key = _parse_message_key(d.pop("messageKey", UNSET))


        office_record_update_result = cls(
            applied=applied,
            conflicts=conflicts,
            message=message,
            message_key=message_key,
        )

        return office_record_update_result

