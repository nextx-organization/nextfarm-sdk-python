from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_office_department_dto import OfficeOfficeDepartmentDto





T = TypeVar("T", bound="OfficeOfficeDepartmentListDto")



@_attrs_define
class OfficeOfficeDepartmentListDto:
    

    departments: list[OfficeOfficeDepartmentDto] | None | Unset = UNSET
    total_member_count: int | Unset = UNSET
    unassigned_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_office_department_dto import OfficeOfficeDepartmentDto # noqa: PLC0415
        departments: list[dict[str, Any]] | None | Unset
        if isinstance(self.departments, Unset):
            departments = UNSET
        elif isinstance(self.departments, list):
            departments = []
            for departments_type_0_item_data in self.departments:
                departments_type_0_item = departments_type_0_item_data.to_dict()
                departments.append(departments_type_0_item)


        else:
            departments = self.departments

        total_member_count = self.total_member_count

        unassigned_count = self.unassigned_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if departments is not UNSET:
            field_dict["departments"] = departments
        if total_member_count is not UNSET:
            field_dict["totalMemberCount"] = total_member_count
        if unassigned_count is not UNSET:
            field_dict["unassignedCount"] = unassigned_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_office_department_dto import OfficeOfficeDepartmentDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_departments(data: object) -> list[OfficeOfficeDepartmentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                departments_type_0 = []
                _departments_type_0 = data
                for departments_type_0_item_data in (_departments_type_0):
                    departments_type_0_item = OfficeOfficeDepartmentDto.from_dict(departments_type_0_item_data)



                    departments_type_0.append(departments_type_0_item)

                return departments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOfficeDepartmentDto] | None | Unset, data)

        departments = _parse_departments(d.pop("departments", UNSET))


        total_member_count = d.pop("totalMemberCount", UNSET)

        unassigned_count = d.pop("unassignedCount", UNSET)

        office_office_department_list_dto = cls(
            departments=departments,
            total_member_count=total_member_count,
            unassigned_count=unassigned_count,
        )

        return office_office_department_list_dto

