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
  from ..models.office_create_task_line_dto import OfficeCreateTaskLineDto





T = TypeVar("T", bound="OfficeCreateTasksBatchRequest")



@_attrs_define
class OfficeCreateTasksBatchRequest:
    

    default_assignee_id: None | Unset | UUID = UNSET
    default_task_group_id: None | Unset | UUID = UNSET
    default_task_list_id: None | Unset | UUID = UNSET
    lines: list[OfficeCreateTaskLineDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_create_task_line_dto import OfficeCreateTaskLineDto # noqa: PLC0415
        default_assignee_id: None | str | Unset
        if isinstance(self.default_assignee_id, Unset):
            default_assignee_id = UNSET
        elif isinstance(self.default_assignee_id, UUID):
            default_assignee_id = str(self.default_assignee_id)
        else:
            default_assignee_id = self.default_assignee_id

        default_task_group_id: None | str | Unset
        if isinstance(self.default_task_group_id, Unset):
            default_task_group_id = UNSET
        elif isinstance(self.default_task_group_id, UUID):
            default_task_group_id = str(self.default_task_group_id)
        else:
            default_task_group_id = self.default_task_group_id

        default_task_list_id: None | str | Unset
        if isinstance(self.default_task_list_id, Unset):
            default_task_list_id = UNSET
        elif isinstance(self.default_task_list_id, UUID):
            default_task_list_id = str(self.default_task_list_id)
        else:
            default_task_list_id = self.default_task_list_id

        lines: list[dict[str, Any]] | None | Unset
        if isinstance(self.lines, Unset):
            lines = UNSET
        elif isinstance(self.lines, list):
            lines = []
            for lines_type_0_item_data in self.lines:
                lines_type_0_item = lines_type_0_item_data.to_dict()
                lines.append(lines_type_0_item)


        else:
            lines = self.lines


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if default_assignee_id is not UNSET:
            field_dict["defaultAssigneeId"] = default_assignee_id
        if default_task_group_id is not UNSET:
            field_dict["defaultTaskGroupId"] = default_task_group_id
        if default_task_list_id is not UNSET:
            field_dict["defaultTaskListId"] = default_task_list_id
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_create_task_line_dto import OfficeCreateTaskLineDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_default_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_assignee_id_type_0 = UUID(data)



                return default_assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_assignee_id = _parse_default_assignee_id(d.pop("defaultAssigneeId", UNSET))


        def _parse_default_task_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_task_group_id_type_0 = UUID(data)



                return default_task_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_task_group_id = _parse_default_task_group_id(d.pop("defaultTaskGroupId", UNSET))


        def _parse_default_task_list_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_task_list_id_type_0 = UUID(data)



                return default_task_list_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_task_list_id = _parse_default_task_list_id(d.pop("defaultTaskListId", UNSET))


        def _parse_lines(data: object) -> list[OfficeCreateTaskLineDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lines_type_0 = []
                _lines_type_0 = data
                for lines_type_0_item_data in (_lines_type_0):
                    lines_type_0_item = OfficeCreateTaskLineDto.from_dict(lines_type_0_item_data)



                    lines_type_0.append(lines_type_0_item)

                return lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCreateTaskLineDto] | None | Unset, data)

        lines = _parse_lines(d.pop("lines", UNSET))


        office_create_tasks_batch_request = cls(
            default_assignee_id=default_assignee_id,
            default_task_group_id=default_task_group_id,
            default_task_list_id=default_task_list_id,
            lines=lines,
        )

        return office_create_tasks_batch_request

