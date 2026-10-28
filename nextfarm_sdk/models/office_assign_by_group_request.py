from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_group_assignment import OfficeGroupAssignment





T = TypeVar("T", bound="OfficeAssignByGroupRequest")



@_attrs_define
class OfficeAssignByGroupRequest:
    

    assignments: list[OfficeGroupAssignment] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_group_assignment import OfficeGroupAssignment # noqa: PLC0415
        assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item = assignments_type_0_item_data.to_dict()
                assignments.append(assignments_type_0_item)


        else:
            assignments = self.assignments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignments is not UNSET:
            field_dict["assignments"] = assignments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_group_assignment import OfficeGroupAssignment # noqa: PLC0415
        d = dict(src_dict)
        def _parse_assignments(data: object) -> list[OfficeGroupAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignments_type_0 = []
                _assignments_type_0 = data
                for assignments_type_0_item_data in (_assignments_type_0):
                    assignments_type_0_item = OfficeGroupAssignment.from_dict(assignments_type_0_item_data)



                    assignments_type_0.append(assignments_type_0_item)

                return assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeGroupAssignment] | None | Unset, data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))


        office_assign_by_group_request = cls(
            assignments=assignments,
        )

        return office_assign_by_group_request

