from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotIrrOutputConfigRequest")



@_attrs_define
class IotIrrOutputConfigRequest:
    

    fert_idx: int | None | Unset = UNSET
    fert_mcv_id: int | None | Unset = UNSET
    fert_out: int | None | Unset = UNSET
    pump: int | None | Unset = UNSET
    pump_idx: int | None | Unset = UNSET
    pump_out: int | None | Unset = UNSET
    pump_role: None | str | Unset = UNSET
    zone_idx: int | None | Unset = UNSET
    zone_out: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        fert_idx: int | None | Unset
        if isinstance(self.fert_idx, Unset):
            fert_idx = UNSET
        else:
            fert_idx = self.fert_idx

        fert_mcv_id: int | None | Unset
        if isinstance(self.fert_mcv_id, Unset):
            fert_mcv_id = UNSET
        else:
            fert_mcv_id = self.fert_mcv_id

        fert_out: int | None | Unset
        if isinstance(self.fert_out, Unset):
            fert_out = UNSET
        else:
            fert_out = self.fert_out

        pump: int | None | Unset
        if isinstance(self.pump, Unset):
            pump = UNSET
        else:
            pump = self.pump

        pump_idx: int | None | Unset
        if isinstance(self.pump_idx, Unset):
            pump_idx = UNSET
        else:
            pump_idx = self.pump_idx

        pump_out: int | None | Unset
        if isinstance(self.pump_out, Unset):
            pump_out = UNSET
        else:
            pump_out = self.pump_out

        pump_role: None | str | Unset
        if isinstance(self.pump_role, Unset):
            pump_role = UNSET
        else:
            pump_role = self.pump_role

        zone_idx: int | None | Unset
        if isinstance(self.zone_idx, Unset):
            zone_idx = UNSET
        else:
            zone_idx = self.zone_idx

        zone_out: int | None | Unset
        if isinstance(self.zone_out, Unset):
            zone_out = UNSET
        else:
            zone_out = self.zone_out


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if fert_idx is not UNSET:
            field_dict["fert_idx"] = fert_idx
        if fert_mcv_id is not UNSET:
            field_dict["fert_mcv_id"] = fert_mcv_id
        if fert_out is not UNSET:
            field_dict["fert_out"] = fert_out
        if pump is not UNSET:
            field_dict["pump"] = pump
        if pump_idx is not UNSET:
            field_dict["pump_idx"] = pump_idx
        if pump_out is not UNSET:
            field_dict["pump_out"] = pump_out
        if pump_role is not UNSET:
            field_dict["pump_role"] = pump_role
        if zone_idx is not UNSET:
            field_dict["zone_idx"] = zone_idx
        if zone_out is not UNSET:
            field_dict["zone_out"] = zone_out

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_fert_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_idx = _parse_fert_idx(d.pop("fert_idx", UNSET))


        def _parse_fert_mcv_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_mcv_id = _parse_fert_mcv_id(d.pop("fert_mcv_id", UNSET))


        def _parse_fert_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_out = _parse_fert_out(d.pop("fert_out", UNSET))


        def _parse_pump(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pump = _parse_pump(d.pop("pump", UNSET))


        def _parse_pump_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pump_idx = _parse_pump_idx(d.pop("pump_idx", UNSET))


        def _parse_pump_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pump_out = _parse_pump_out(d.pop("pump_out", UNSET))


        def _parse_pump_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pump_role = _parse_pump_role(d.pop("pump_role", UNSET))


        def _parse_zone_idx(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        zone_idx = _parse_zone_idx(d.pop("zone_idx", UNSET))


        def _parse_zone_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        zone_out = _parse_zone_out(d.pop("zone_out", UNSET))


        iot_irr_output_config_request = cls(
            fert_idx=fert_idx,
            fert_mcv_id=fert_mcv_id,
            fert_out=fert_out,
            pump=pump,
            pump_idx=pump_idx,
            pump_out=pump_out,
            pump_role=pump_role,
            zone_idx=zone_idx,
            zone_out=zone_out,
        )

        return iot_irr_output_config_request

