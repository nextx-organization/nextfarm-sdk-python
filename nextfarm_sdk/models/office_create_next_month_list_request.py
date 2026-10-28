from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCreateNextMonthListRequest")



@_attrs_define
class OfficeCreateNextMonthListRequest:
    

    carry_over: bool | Unset = UNSET
    copy_groups: bool | Unset = UNSET
    duty_names: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        carry_over = self.carry_over

        copy_groups = self.copy_groups

        duty_names: list[str] | None | Unset
        if isinstance(self.duty_names, Unset):
            duty_names = UNSET
        elif isinstance(self.duty_names, list):
            duty_names = self.duty_names


        else:
            duty_names = self.duty_names


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if carry_over is not UNSET:
            field_dict["carryOver"] = carry_over
        if copy_groups is not UNSET:
            field_dict["copyGroups"] = copy_groups
        if duty_names is not UNSET:
            field_dict["dutyNames"] = duty_names

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carry_over = d.pop("carryOver", UNSET)

        copy_groups = d.pop("copyGroups", UNSET)

        def _parse_duty_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                duty_names_type_0 = cast(list[str], data)

                return duty_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        duty_names = _parse_duty_names(d.pop("dutyNames", UNSET))


        office_create_next_month_list_request = cls(
            carry_over=carry_over,
            copy_groups=copy_groups,
            duty_names=duty_names,
        )

        return office_create_next_month_list_request

