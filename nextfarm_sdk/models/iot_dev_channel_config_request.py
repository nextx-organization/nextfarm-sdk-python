from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IotDevChannelConfigRequest")



@_attrs_define
class IotDevChannelConfigRequest:
    

    auto: int | None | Unset = UNSET
    eh: int | None | Unset = UNSET
    em: int | None | Unset = UNSET
    idx: int | Unset = UNSET
    kind: int | None | Unset = UNSET
    label: None | str | Unset = UNSET
    lim_a: int | None | Unset = UNSET
    lim_b: int | None | Unset = UNSET
    out_a: int | None | Unset = UNSET
    out_b: int | None | Unset = UNSET
    sh: int | None | Unset = UNSET
    sm: int | None | Unset = UNSET
    thr_off: int | None | Unset = UNSET
    thr_on: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto: int | None | Unset
        if isinstance(self.auto, Unset):
            auto = UNSET
        else:
            auto = self.auto

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

        kind: int | None | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        lim_a: int | None | Unset
        if isinstance(self.lim_a, Unset):
            lim_a = UNSET
        else:
            lim_a = self.lim_a

        lim_b: int | None | Unset
        if isinstance(self.lim_b, Unset):
            lim_b = UNSET
        else:
            lim_b = self.lim_b

        out_a: int | None | Unset
        if isinstance(self.out_a, Unset):
            out_a = UNSET
        else:
            out_a = self.out_a

        out_b: int | None | Unset
        if isinstance(self.out_b, Unset):
            out_b = UNSET
        else:
            out_b = self.out_b

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
        if auto is not UNSET:
            field_dict["auto"] = auto
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
        if lim_a is not UNSET:
            field_dict["lim_a"] = lim_a
        if lim_b is not UNSET:
            field_dict["lim_b"] = lim_b
        if out_a is not UNSET:
            field_dict["out_a"] = out_a
        if out_b is not UNSET:
            field_dict["out_b"] = out_b
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
        def _parse_auto(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto = _parse_auto(d.pop("auto", UNSET))


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

        def _parse_kind(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_lim_a(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lim_a = _parse_lim_a(d.pop("lim_a", UNSET))


        def _parse_lim_b(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lim_b = _parse_lim_b(d.pop("lim_b", UNSET))


        def _parse_out_a(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        out_a = _parse_out_a(d.pop("out_a", UNSET))


        def _parse_out_b(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        out_b = _parse_out_b(d.pop("out_b", UNSET))


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


        iot_dev_channel_config_request = cls(
            auto=auto,
            eh=eh,
            em=em,
            idx=idx,
            kind=kind,
            label=label,
            lim_a=lim_a,
            lim_b=lim_b,
            out_a=out_a,
            out_b=out_b,
            sh=sh,
            sm=sm,
            thr_off=thr_off,
            thr_on=thr_on,
        )

        return iot_dev_channel_config_request

