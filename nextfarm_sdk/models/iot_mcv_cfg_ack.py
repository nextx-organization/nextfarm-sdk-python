from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai





T = TypeVar("T", bound="IotMcvCfgAck")



@_attrs_define
class IotMcvCfgAck:
    

    applied: IotMcvCfgBaoKhai | Unset = UNSET
    applied_at: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    err: None | str | Unset = UNSET
    ok: bool | Unset = UNSET
    seq: int | Unset = UNSET
    ts: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai # noqa: PLC0415
        applied: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied.to_dict()

        applied_at: None | str | Unset
        if isinstance(self.applied_at, Unset):
            applied_at = UNSET
        else:
            applied_at = self.applied_at

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        err: None | str | Unset
        if isinstance(self.err, Unset):
            err = UNSET
        else:
            err = self.err

        ok = self.ok

        seq = self.seq

        ts: int | None | Unset
        if isinstance(self.ts, Unset):
            ts = UNSET
        else:
            ts = self.ts


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if applied is not UNSET:
            field_dict["applied"] = applied
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at
        if detail is not UNSET:
            field_dict["detail"] = detail
        if err is not UNSET:
            field_dict["err"] = err
        if ok is not UNSET:
            field_dict["ok"] = ok
        if seq is not UNSET:
            field_dict["seq"] = seq
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai # noqa: PLC0415
        d = dict(src_dict)
        _applied = d.pop("applied", UNSET)
        applied: IotMcvCfgBaoKhai | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = IotMcvCfgBaoKhai.from_dict(_applied)




        def _parse_applied_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_at = _parse_applied_at(d.pop("applied_at", UNSET))


        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        def _parse_err(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        err = _parse_err(d.pop("err", UNSET))


        ok = d.pop("ok", UNSET)

        seq = d.pop("seq", UNSET)

        def _parse_ts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ts = _parse_ts(d.pop("ts", UNSET))


        iot_mcv_cfg_ack = cls(
            applied=applied,
            applied_at=applied_at,
            detail=detail,
            err=err,
            ok=ok,
            seq=seq,
            ts=ts,
        )

        return iot_mcv_cfg_ack

