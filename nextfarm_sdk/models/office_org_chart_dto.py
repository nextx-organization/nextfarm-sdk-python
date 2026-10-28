from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_org_member_dto import OfficeOrgMemberDto
  from ..models.office_org_unit_node_dto import OfficeOrgUnitNodeDto





T = TypeVar("T", bound="OfficeOrgChartDto")



@_attrs_define
class OfficeOrgChartDto:
    

    unassigned_members: list[OfficeOrgMemberDto] | None | Unset = UNSET
    units: list[OfficeOrgUnitNodeDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_org_member_dto import OfficeOrgMemberDto # noqa: PLC0415
        from ..models.office_org_unit_node_dto import OfficeOrgUnitNodeDto # noqa: PLC0415
        unassigned_members: list[dict[str, Any]] | None | Unset
        if isinstance(self.unassigned_members, Unset):
            unassigned_members = UNSET
        elif isinstance(self.unassigned_members, list):
            unassigned_members = []
            for unassigned_members_type_0_item_data in self.unassigned_members:
                unassigned_members_type_0_item = unassigned_members_type_0_item_data.to_dict()
                unassigned_members.append(unassigned_members_type_0_item)


        else:
            unassigned_members = self.unassigned_members

        units: list[dict[str, Any]] | None | Unset
        if isinstance(self.units, Unset):
            units = UNSET
        elif isinstance(self.units, list):
            units = []
            for units_type_0_item_data in self.units:
                units_type_0_item = units_type_0_item_data.to_dict()
                units.append(units_type_0_item)


        else:
            units = self.units


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if unassigned_members is not UNSET:
            field_dict["unassignedMembers"] = unassigned_members
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_org_member_dto import OfficeOrgMemberDto # noqa: PLC0415
        from ..models.office_org_unit_node_dto import OfficeOrgUnitNodeDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_unassigned_members(data: object) -> list[OfficeOrgMemberDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unassigned_members_type_0 = []
                _unassigned_members_type_0 = data
                for unassigned_members_type_0_item_data in (_unassigned_members_type_0):
                    unassigned_members_type_0_item = OfficeOrgMemberDto.from_dict(unassigned_members_type_0_item_data)



                    unassigned_members_type_0.append(unassigned_members_type_0_item)

                return unassigned_members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOrgMemberDto] | None | Unset, data)

        unassigned_members = _parse_unassigned_members(d.pop("unassignedMembers", UNSET))


        def _parse_units(data: object) -> list[OfficeOrgUnitNodeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                units_type_0 = []
                _units_type_0 = data
                for units_type_0_item_data in (_units_type_0):
                    units_type_0_item = OfficeOrgUnitNodeDto.from_dict(units_type_0_item_data)



                    units_type_0.append(units_type_0_item)

                return units_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOrgUnitNodeDto] | None | Unset, data)

        units = _parse_units(d.pop("units", UNSET))


        office_org_chart_dto = cls(
            unassigned_members=unassigned_members,
            units=units,
        )

        return office_org_chart_dto

