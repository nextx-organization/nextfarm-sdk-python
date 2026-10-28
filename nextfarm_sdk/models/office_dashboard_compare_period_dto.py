from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDashboardComparePeriodDto")



@_attrs_define
class OfficeDashboardComparePeriodDto:
    

    from_: None | str | Unset = UNSET
    previous_from: None | str | Unset = UNSET
    previous_to: None | str | Unset = UNSET
    to: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        previous_from: None | str | Unset
        if isinstance(self.previous_from, Unset):
            previous_from = UNSET
        else:
            previous_from = self.previous_from

        previous_to: None | str | Unset
        if isinstance(self.previous_to, Unset):
            previous_to = UNSET
        else:
            previous_to = self.previous_to

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if previous_from is not UNSET:
            field_dict["previousFrom"] = previous_from
        if previous_to is not UNSET:
            field_dict["previousTo"] = previous_to
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_previous_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_from = _parse_previous_from(d.pop("previousFrom", UNSET))


        def _parse_previous_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_to = _parse_previous_to(d.pop("previousTo", UNSET))


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        office_dashboard_compare_period_dto = cls(
            from_=from_,
            previous_from=previous_from,
            previous_to=previous_to,
            to=to,
        )

        return office_dashboard_compare_period_dto

