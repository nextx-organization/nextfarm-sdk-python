from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="IotDeviceOutputChannelDto")



@_attrs_define
class IotDeviceOutputChannelDto:
    

    auto_mode: int | None | Unset = UNSET
    eh: int | None | Unset = UNSET
    em: int | None | Unset = UNSET
    idx: int | Unset = UNSET
    kind: int | Unset = UNSET
    label: None | str | Unset = UNSET
    manual_max_min: int | None | Unset = UNSET
    online: bool | Unset = UNSET
    out_a: int | Unset = UNSET
    out_b: int | None | Unset = UNSET
    reported_at: datetime.datetime | Unset = UNSET
    role: None | str | Unset = UNSET
    sh: int | None | Unset = UNSET
    sm: int | None | Unset = UNSET
    thr_off: int | None | Unset = UNSET
    thr_on: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto_mode: int | None | Unset
        if isinstance(self.auto_mode, Unset):
            auto_mode = UNSET
        else:
            auto_mode = self.auto_mode

        eh: int | None | Unset
        if isinstance(self.eh, Unset):
            eh = UNSET
        else:
            eh = self.eh

        em: int | None | Unset
        if isinstance(self.em, Unset):
            em = UNSET
        else:
            em = self.em

        idx = self.idx

        kind = self.kind

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        manual_max_min: int | None | Unset
        if isinstance(self.manual_max_min, Unset):
            manual_max_min = UNSET
        else:
            manual_max_min = self.manual_max_min

        online = self.online

        out_a = self.out_a

        out_b: int | None | Unset
        if isinstance(self.out_b, Unset):
            out_b = UNSET
        else:
            out_b = self.out_b

        reported_at: str | Unset = UNSET
        if not isinstance(self.reported_at, Unset):
            reported_at = self.reported_at.isoformat()

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        sh: int | None | Unset
        if isinstance(self.sh, Unset):
            sh = UNSET
        else:
            sh = self.sh

        sm: int | None | Unset
        if isinstance(self.sm, Unset):
            sm = UNSET
        else:
            sm = self.sm

        thr_off: int | None | Unset
        if isinstance(self.thr_off, Unset):
            thr_off = UNSET
        else:
            thr_off = self.thr_off

        thr_on: int | None | Unset
        if isinstance(self.thr_on, Unset):
            thr_on = UNSET
        else:
            thr_on = self.thr_on


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto_mode is not UNSET:
            field_dict["auto_mode"] = auto_mode
        if eh is not UNSET:
            field_dict["eh"] = eh
        if em is not UNSET:
            field_dict["em"] = em
        if idx is not UNSET:
            field_dict["idx"] = idx
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if manual_max_min is not UNSET:
            field_dict["manual_max_min"] = manual_max_min
        if online is not UNSET:
            field_dict["online"] = online
        if out_a is not UNSET:
            field_dict["out_a"] = out_a
        if out_b is not UNSET:
            field_dict["out_b"] = out_b
        if reported_at is not UNSET:
            field_dict["reported_at"] = reported_at
        if role is not UNSET:
            field_dict["role"] = role
        if sh is not UNSET:
            field_dict["sh"] = sh
        if sm is not UNSET:
            field_dict["sm"] = sm
        if thr_off is not UNSET:
            field_dict["thr_off"] = thr_off
        if thr_on is not UNSET:
            field_dict["thr_on"] = thr_on

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


        def _parse_eh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        eh = _parse_eh(d.pop("eh", UNSET))


        def _parse_em(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        em = _parse_em(d.pop("em", UNSET))


        idx = d.pop("idx", UNSET)

        kind = d.pop("kind", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_manual_max_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        manual_max_min = _parse_manual_max_min(d.pop("manual_max_min", UNSET))


        online = d.pop("online", UNSET)

        out_a = d.pop("out_a", UNSET)

        def _parse_out_b(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        out_b = _parse_out_b(d.pop("out_b", UNSET))


        _reported_at = d.pop("reported_at", UNSET)
        reported_at: datetime.datetime | Unset
        if isinstance(_reported_at,  Unset):
            reported_at = UNSET
        else:
            reported_at = datetime.datetime.fromisoformat(_reported_at)




        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        def _parse_sh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sh = _parse_sh(d.pop("sh", UNSET))


        def _parse_sm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sm = _parse_sm(d.pop("sm", UNSET))


        def _parse_thr_off(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thr_off = _parse_thr_off(d.pop("thr_off", UNSET))


        def _parse_thr_on(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thr_on = _parse_thr_on(d.pop("thr_on", UNSET))


        iot_device_output_channel_dto = cls(
            auto_mode=auto_mode,
            eh=eh,
            em=em,
            idx=idx,
            kind=kind,
            label=label,
            manual_max_min=manual_max_min,
            online=online,
            out_a=out_a,
            out_b=out_b,
            reported_at=reported_at,
            role=role,
            sh=sh,
            sm=sm,
            thr_off=thr_off,
            thr_on=thr_on,
        )

        return iot_device_output_channel_dto

