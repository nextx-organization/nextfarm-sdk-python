from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotMcvCfgBaoKhai")



@_attrs_define
class IotMcvCfgBaoKhai:
    

    count: int | None | Unset = UNSET
    count_max: int | None | Unset = UNSET
    ec_cap: float | None | Unset = UNSET
    ec_on: bool | None | Unset = UNSET
    ec_target: float | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    fert: list[int] | None | Unset = UNSET
    k_ul: list[int] | None | Unset = UNSET
    liters: float | None | Unset = UNSET
    pump_fb: int | None | Unset = UNSET
    ratio: list[int] | None | Unset = UNSET
    types: list[int] | None | Unset = UNSET
    v: int | None | Unset = UNSET
    wait_min: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        count_max: int | None | Unset
        if isinstance(self.count_max, Unset):
            count_max = UNSET
        else:
            count_max = self.count_max

        ec_cap: float | None | Unset
        if isinstance(self.ec_cap, Unset):
            ec_cap = UNSET
        else:
            ec_cap = self.ec_cap

        ec_on: bool | None | Unset
        if isinstance(self.ec_on, Unset):
            ec_on = UNSET
        else:
            ec_on = self.ec_on

        ec_target: float | None | Unset
        if isinstance(self.ec_target, Unset):
            ec_target = UNSET
        else:
            ec_target = self.ec_target

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        fert: list[int] | None | Unset
        if isinstance(self.fert, Unset):
            fert = UNSET
        elif isinstance(self.fert, list):
            fert = self.fert


        else:
            fert = self.fert

        k_ul: list[int] | None | Unset
        if isinstance(self.k_ul, Unset):
            k_ul = UNSET
        elif isinstance(self.k_ul, list):
            k_ul = self.k_ul


        else:
            k_ul = self.k_ul

        liters: float | None | Unset
        if isinstance(self.liters, Unset):
            liters = UNSET
        else:
            liters = self.liters

        pump_fb: int | None | Unset
        if isinstance(self.pump_fb, Unset):
            pump_fb = UNSET
        else:
            pump_fb = self.pump_fb

        ratio: list[int] | None | Unset
        if isinstance(self.ratio, Unset):
            ratio = UNSET
        elif isinstance(self.ratio, list):
            ratio = self.ratio


        else:
            ratio = self.ratio

        types: list[int] | None | Unset
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, list):
            types = self.types


        else:
            types = self.types

        v: int | None | Unset
        if isinstance(self.v, Unset):
            v = UNSET
        else:
            v = self.v

        wait_min: int | None | Unset
        if isinstance(self.wait_min, Unset):
            wait_min = UNSET
        else:
            wait_min = self.wait_min


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if count_max is not UNSET:
            field_dict["count_max"] = count_max
        if ec_cap is not UNSET:
            field_dict["ec_cap"] = ec_cap
        if ec_on is not UNSET:
            field_dict["ec_on"] = ec_on
        if ec_target is not UNSET:
            field_dict["ec_target"] = ec_target
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fert is not UNSET:
            field_dict["fert"] = fert
        if k_ul is not UNSET:
            field_dict["k_ul"] = k_ul
        if liters is not UNSET:
            field_dict["liters"] = liters
        if pump_fb is not UNSET:
            field_dict["pump_fb"] = pump_fb
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if types is not UNSET:
            field_dict["types"] = types
        if v is not UNSET:
            field_dict["v"] = v
        if wait_min is not UNSET:
            field_dict["wait_min"] = wait_min

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))


        def _parse_count_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count_max = _parse_count_max(d.pop("count_max", UNSET))


        def _parse_ec_cap(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ec_cap = _parse_ec_cap(d.pop("ec_cap", UNSET))


        def _parse_ec_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ec_on = _parse_ec_on(d.pop("ec_on", UNSET))


        def _parse_ec_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ec_target = _parse_ec_target(d.pop("ec_target", UNSET))


        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        def _parse_fert(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fert_type_0 = cast(list[int], data)

                return fert_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        fert = _parse_fert(d.pop("fert", UNSET))


        def _parse_k_ul(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                k_ul_type_0 = cast(list[int], data)

                return k_ul_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        k_ul = _parse_k_ul(d.pop("k_ul", UNSET))


        def _parse_liters(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        liters = _parse_liters(d.pop("liters", UNSET))


        def _parse_pump_fb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pump_fb = _parse_pump_fb(d.pop("pump_fb", UNSET))


        def _parse_ratio(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ratio_type_0 = cast(list[int], data)

                return ratio_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ratio = _parse_ratio(d.pop("ratio", UNSET))


        def _parse_types(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = cast(list[int], data)

                return types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        types = _parse_types(d.pop("types", UNSET))


        def _parse_v(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        v = _parse_v(d.pop("v", UNSET))


        def _parse_wait_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wait_min = _parse_wait_min(d.pop("wait_min", UNSET))


        iot_mcv_cfg_bao_khai = cls(
            count=count,
            count_max=count_max,
            ec_cap=ec_cap,
            ec_on=ec_on,
            ec_target=ec_target,
            enabled=enabled,
            fert=fert,
            k_ul=k_ul,
            liters=liters,
            pump_fb=pump_fb,
            ratio=ratio,
            types=types,
            v=v,
            wait_min=wait_min,
        )

        return iot_mcv_cfg_bao_khai

