from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotRunOnceRequest")



@_attrs_define
class IotRunOnceRequest:
    

    minutes: int | Unset = UNSET
    name: None | str | Unset = UNSET
    via: None | str | Unset = UNSET
    zone_idx: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        minutes = self.minutes

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        via: None | str | Unset
        if isinstance(self.via, Unset):
            via = UNSET
        else:
            via = self.via

        zone_idx: list[int] | None | Unset
        if isinstance(self.zone_idx, Unset):
            zone_idx = UNSET
        elif isinstance(self.zone_idx, list):
            zone_idx = self.zone_idx


        else:
            zone_idx = self.zone_idx


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if name is not UNSET:
            field_dict["name"] = name
        if via is not UNSET:
            field_dict["via"] = via
        if zone_idx is not UNSET:
            field_dict["zone_idx"] = zone_idx

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minutes = d.pop("minutes", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_via(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        via = _parse_via(d.pop("via", UNSET))


        def _parse_zone_idx(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                zone_idx_type_0 = cast(list[int], data)

                return zone_idx_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        zone_idx = _parse_zone_idx(d.pop("zone_idx", UNSET))


        iot_run_once_request = cls(
            minutes=minutes,
            name=name,
            via=via,
            zone_idx=zone_idx,
        )

        return iot_run_once_request

