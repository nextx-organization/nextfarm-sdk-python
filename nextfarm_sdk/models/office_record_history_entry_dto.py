from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_record_history_change_dto import OfficeRecordHistoryChangeDto





T = TypeVar("T", bound="OfficeRecordHistoryEntryDto")



@_attrs_define
class OfficeRecordHistoryEntryDto:
    

    action: None | str | Unset = UNSET
    changes: list[OfficeRecordHistoryChangeDto] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_history_change_dto import OfficeRecordHistoryChangeDto # noqa: PLC0415
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        changes: list[dict[str, Any]] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)


        else:
            changes = self.changes

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if changes is not UNSET:
            field_dict["changes"] = changes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_history_change_dto import OfficeRecordHistoryChangeDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_changes(data: object) -> list[OfficeRecordHistoryChangeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in (_changes_type_0):
                    changes_type_0_item = OfficeRecordHistoryChangeDto.from_dict(changes_type_0_item_data)



                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRecordHistoryChangeDto] | None | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)



                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        office_record_history_entry_dto = cls(
            action=action,
            changes=changes,
            created_at=created_at,
            id=id,
            user_id=user_id,
        )

        return office_record_history_entry_dto

