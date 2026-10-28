from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeListTaskDependenciesBatchRequest")



@_attrs_define
class OfficeListTaskDependenciesBatchRequest:
    

    task_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        task_ids: list[str] | None | Unset
        if isinstance(self.task_ids, Unset):
            task_ids = UNSET
        elif isinstance(self.task_ids, list):
            task_ids = []
            for task_ids_type_0_item_data in self.task_ids:
                task_ids_type_0_item = str(task_ids_type_0_item_data)
                task_ids.append(task_ids_type_0_item)


        else:
            task_ids = self.task_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if task_ids is not UNSET:
            field_dict["taskIds"] = task_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_task_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                task_ids_type_0 = []
                _task_ids_type_0 = data
                for task_ids_type_0_item_data in (_task_ids_type_0):
                    task_ids_type_0_item = UUID(task_ids_type_0_item_data)



                    task_ids_type_0.append(task_ids_type_0_item)

                return task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        task_ids = _parse_task_ids(d.pop("taskIds", UNSET))


        office_list_task_dependencies_batch_request = cls(
            task_ids=task_ids,
        )

        return office_list_task_dependencies_batch_request

