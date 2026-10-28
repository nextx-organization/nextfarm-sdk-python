from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMoveTaskListToGroupRequest")



@_attrs_define
class OfficeMoveTaskListToGroupRequest:
    

    group_id: None | Unset | UUID = UNSET
    ordered_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        ordered_ids: list[str] | None | Unset
        if isinstance(self.ordered_ids, Unset):
            ordered_ids = UNSET
        elif isinstance(self.ordered_ids, list):
            ordered_ids = []
            for ordered_ids_type_0_item_data in self.ordered_ids:
                ordered_ids_type_0_item = str(ordered_ids_type_0_item_data)
                ordered_ids.append(ordered_ids_type_0_item)


        else:
            ordered_ids = self.ordered_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if ordered_ids is not UNSET:
            field_dict["orderedIds"] = ordered_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        def _parse_ordered_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ordered_ids_type_0 = []
                _ordered_ids_type_0 = data
                for ordered_ids_type_0_item_data in (_ordered_ids_type_0):
                    ordered_ids_type_0_item = UUID(ordered_ids_type_0_item_data)



                    ordered_ids_type_0.append(ordered_ids_type_0_item)

                return ordered_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ordered_ids = _parse_ordered_ids(d.pop("orderedIds", UNSET))


        office_move_task_list_to_group_request = cls(
            group_id=group_id,
            ordered_ids=ordered_ids,
        )

        return office_move_task_list_to_group_request

