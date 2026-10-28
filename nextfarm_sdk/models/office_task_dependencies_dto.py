from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_dependency_dto import OfficeTaskDependencyDto





T = TypeVar("T", bound="OfficeTaskDependenciesDto")



@_attrs_define
class OfficeTaskDependenciesDto:
    

    blockers: list[OfficeTaskDependencyDto] | None | Unset = UNSET
    blocking: list[OfficeTaskDependencyDto] | None | Unset = UNSET
    is_blocked: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_dependency_dto import OfficeTaskDependencyDto # noqa: PLC0415
        blockers: list[dict[str, Any]] | None | Unset
        if isinstance(self.blockers, Unset):
            blockers = UNSET
        elif isinstance(self.blockers, list):
            blockers = []
            for blockers_type_0_item_data in self.blockers:
                blockers_type_0_item = blockers_type_0_item_data.to_dict()
                blockers.append(blockers_type_0_item)


        else:
            blockers = self.blockers

        blocking: list[dict[str, Any]] | None | Unset
        if isinstance(self.blocking, Unset):
            blocking = UNSET
        elif isinstance(self.blocking, list):
            blocking = []
            for blocking_type_0_item_data in self.blocking:
                blocking_type_0_item = blocking_type_0_item_data.to_dict()
                blocking.append(blocking_type_0_item)


        else:
            blocking = self.blocking

        is_blocked = self.is_blocked


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if blockers is not UNSET:
            field_dict["blockers"] = blockers
        if blocking is not UNSET:
            field_dict["blocking"] = blocking
        if is_blocked is not UNSET:
            field_dict["isBlocked"] = is_blocked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_dependency_dto import OfficeTaskDependencyDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_blockers(data: object) -> list[OfficeTaskDependencyDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blockers_type_0 = []
                _blockers_type_0 = data
                for blockers_type_0_item_data in (_blockers_type_0):
                    blockers_type_0_item = OfficeTaskDependencyDto.from_dict(blockers_type_0_item_data)



                    blockers_type_0.append(blockers_type_0_item)

                return blockers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskDependencyDto] | None | Unset, data)

        blockers = _parse_blockers(d.pop("blockers", UNSET))


        def _parse_blocking(data: object) -> list[OfficeTaskDependencyDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocking_type_0 = []
                _blocking_type_0 = data
                for blocking_type_0_item_data in (_blocking_type_0):
                    blocking_type_0_item = OfficeTaskDependencyDto.from_dict(blocking_type_0_item_data)



                    blocking_type_0.append(blocking_type_0_item)

                return blocking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskDependencyDto] | None | Unset, data)

        blocking = _parse_blocking(d.pop("blocking", UNSET))


        is_blocked = d.pop("isBlocked", UNSET)

        office_task_dependencies_dto = cls(
            blockers=blockers,
            blocking=blocking,
            is_blocked=is_blocked,
        )

        return office_task_dependencies_dto

