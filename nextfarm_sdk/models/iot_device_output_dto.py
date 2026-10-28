from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotDeviceOutputDto")



@_attrs_define
class IotDeviceOutputDto:
    

    auto_mode: int | None | Unset = UNSET
    family: None | str | Unset = UNSET
    index: int | Unset = UNSET
    key: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    mcv_actual: int | None | Unset = UNSET
    mcv_set: int | None | Unset = UNSET
    mcv_stat: int | None | Unset = UNSET
    port: int | None | Unset = UNSET
    role: None | str | Unset = UNSET
    state: int | Unset = UNSET
    type_: None | str | Unset = UNSET
    valid_values: list[int] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto_mode: int | None | Unset
        if isinstance(self.auto_mode, Unset):
            auto_mode = UNSET
        else:
            auto_mode = self.auto_mode

        family: None | str | Unset
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        index = self.index

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        mcv_actual: int | None | Unset
        if isinstance(self.mcv_actual, Unset):
            mcv_actual = UNSET
        else:
            mcv_actual = self.mcv_actual

        mcv_set: int | None | Unset
        if isinstance(self.mcv_set, Unset):
            mcv_set = UNSET
        else:
            mcv_set = self.mcv_set

        mcv_stat: int | None | Unset
        if isinstance(self.mcv_stat, Unset):
            mcv_stat = UNSET
        else:
            mcv_stat = self.mcv_stat

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        state = self.state

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        valid_values: list[int] | None | Unset
        if isinstance(self.valid_values, Unset):
            valid_values = UNSET
        elif isinstance(self.valid_values, list):
            valid_values = self.valid_values


        else:
            valid_values = self.valid_values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto_mode is not UNSET:
            field_dict["auto_mode"] = auto_mode
        if family is not UNSET:
            field_dict["family"] = family
        if index is not UNSET:
            field_dict["index"] = index
        if key is not UNSET:
            field_dict["key"] = key
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if mcv_actual is not UNSET:
            field_dict["mcv_actual"] = mcv_actual
        if mcv_set is not UNSET:
            field_dict["mcv_set"] = mcv_set
        if mcv_stat is not UNSET:
            field_dict["mcv_stat"] = mcv_stat
        if port is not UNSET:
            field_dict["port"] = port
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if valid_values is not UNSET:
            field_dict["valid_values"] = valid_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_auto_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_mode = _parse_auto_mode(d.pop("auto_mode", UNSET))


        def _parse_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family = _parse_family(d.pop("family", UNSET))


        index = d.pop("index", UNSET)

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_mcv_actual(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv_actual = _parse_mcv_actual(d.pop("mcv_actual", UNSET))


        def _parse_mcv_set(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv_set = _parse_mcv_set(d.pop("mcv_set", UNSET))


        def _parse_mcv_stat(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv_stat = _parse_mcv_stat(d.pop("mcv_stat", UNSET))


        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        state = d.pop("state", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_valid_values(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                valid_values_type_0 = cast(list[int], data)

                return valid_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        valid_values = _parse_valid_values(d.pop("valid_values", UNSET))


        iot_device_output_dto = cls(
            auto_mode=auto_mode,
            family=family,
            index=index,
            key=key,
            kind=kind,
            label=label,
            mcv_actual=mcv_actual,
            mcv_set=mcv_set,
            mcv_stat=mcv_stat,
            port=port,
            role=role,
            state=state,
            type_=type_,
            valid_values=valid_values,
        )

        return iot_device_output_dto

