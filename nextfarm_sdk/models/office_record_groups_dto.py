from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_record_group_dto import OfficeRecordGroupDto





T = TypeVar("T", bound="OfficeRecordGroupsDto")



@_attrs_define
class OfficeRecordGroupsDto:
    

    field_hidden: bool | Unset = UNSET
    groups: list[OfficeRecordGroupDto] | None | Unset = UNSET
    too_many: bool | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_group_dto import OfficeRecordGroupDto # noqa: PLC0415
        field_hidden = self.field_hidden

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)


        else:
            groups = self.groups

        too_many = self.too_many

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_hidden is not UNSET:
            field_dict["fieldHidden"] = field_hidden
        if groups is not UNSET:
            field_dict["groups"] = groups
        if too_many is not UNSET:
            field_dict["tooMany"] = too_many
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_group_dto import OfficeRecordGroupDto # noqa: PLC0415
        d = dict(src_dict)
        field_hidden = d.pop("fieldHidden", UNSET)

        def _parse_groups(data: object) -> list[OfficeRecordGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in (_groups_type_0):
                    groups_type_0_item = OfficeRecordGroupDto.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRecordGroupDto] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        too_many = d.pop("tooMany", UNSET)

        total = d.pop("total", UNSET)

        office_record_groups_dto = cls(
            field_hidden=field_hidden,
            groups=groups,
            too_many=too_many,
            total=total,
        )

        return office_record_groups_dto

