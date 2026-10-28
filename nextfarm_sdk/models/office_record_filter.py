from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_filter_condition import OfficeFilterCondition





T = TypeVar("T", bound="OfficeRecordFilter")



@_attrs_define
class OfficeRecordFilter:
    

    conditions: list[OfficeFilterCondition] | None | Unset = UNSET
    conjunction: None | str | Unset = UNSET
    groups: list[OfficeRecordFilter] | None | Unset = UNSET
    has_criteria: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_filter_condition import OfficeFilterCondition # noqa: PLC0415
        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)


        else:
            conditions = self.conditions

        conjunction: None | str | Unset
        if isinstance(self.conjunction, Unset):
            conjunction = UNSET
        else:
            conjunction = self.conjunction

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

        has_criteria = self.has_criteria


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if conjunction is not UNSET:
            field_dict["conjunction"] = conjunction
        if groups is not UNSET:
            field_dict["groups"] = groups
        if has_criteria is not UNSET:
            field_dict["hasCriteria"] = has_criteria

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_filter_condition import OfficeFilterCondition # noqa: PLC0415
        d = dict(src_dict)
        def _parse_conditions(data: object) -> list[OfficeFilterCondition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in (_conditions_type_0):
                    conditions_type_0_item = OfficeFilterCondition.from_dict(conditions_type_0_item_data)



                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeFilterCondition] | None | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))


        def _parse_conjunction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conjunction = _parse_conjunction(d.pop("conjunction", UNSET))


        def _parse_groups(data: object) -> list[OfficeRecordFilter] | None | Unset:
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
                    groups_type_0_item = OfficeRecordFilter.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRecordFilter] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        has_criteria = d.pop("hasCriteria", UNSET)

        office_record_filter = cls(
            conditions=conditions,
            conjunction=conjunction,
            groups=groups,
            has_criteria=has_criteria,
        )

        return office_record_filter

