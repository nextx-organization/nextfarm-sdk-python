from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.iot_mcv_cfg_ack import IotMcvCfgAck
  from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai





T = TypeVar("T", bound="IotMcvCfgStateDto")



@_attrs_define
class IotMcvCfgStateDto:
    

    ack: IotMcvCfgAck | Unset = UNSET
    desired: IotMcvCfgBaoKhai | Unset = UNSET
    echo_at: datetime.datetime | None | Unset = UNSET
    pushed_at: datetime.datetime | None | Unset = UNSET
    reported: IotMcvCfgBaoKhai | Unset = UNSET
    seq: int | None | Unset = UNSET
    state: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_mcv_cfg_ack import IotMcvCfgAck # noqa: PLC0415
        from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai # noqa: PLC0415
        ack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ack, Unset):
            ack = self.ack.to_dict()

        desired: dict[str, Any] | Unset = UNSET
        if not isinstance(self.desired, Unset):
            desired = self.desired.to_dict()

        echo_at: None | str | Unset
        if isinstance(self.echo_at, Unset):
            echo_at = UNSET
        elif isinstance(self.echo_at, datetime.datetime):
            echo_at = self.echo_at.isoformat()
        else:
            echo_at = self.echo_at

        pushed_at: None | str | Unset
        if isinstance(self.pushed_at, Unset):
            pushed_at = UNSET
        elif isinstance(self.pushed_at, datetime.datetime):
            pushed_at = self.pushed_at.isoformat()
        else:
            pushed_at = self.pushed_at

        reported: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reported, Unset):
            reported = self.reported.to_dict()

        seq: int | None | Unset
        if isinstance(self.seq, Unset):
            seq = UNSET
        else:
            seq = self.seq

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ack is not UNSET:
            field_dict["ack"] = ack
        if desired is not UNSET:
            field_dict["desired"] = desired
        if echo_at is not UNSET:
            field_dict["echo_at"] = echo_at
        if pushed_at is not UNSET:
            field_dict["pushed_at"] = pushed_at
        if reported is not UNSET:
            field_dict["reported"] = reported
        if seq is not UNSET:
            field_dict["seq"] = seq
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_mcv_cfg_ack import IotMcvCfgAck # noqa: PLC0415
        from ..models.iot_mcv_cfg_bao_khai import IotMcvCfgBaoKhai # noqa: PLC0415
        d = dict(src_dict)
        _ack = d.pop("ack", UNSET)
        ack: IotMcvCfgAck | Unset
        if isinstance(_ack,  Unset):
            ack = UNSET
        else:
            ack = IotMcvCfgAck.from_dict(_ack)




        _desired = d.pop("desired", UNSET)
        desired: IotMcvCfgBaoKhai | Unset
        if isinstance(_desired,  Unset):
            desired = UNSET
        else:
            desired = IotMcvCfgBaoKhai.from_dict(_desired)




        def _parse_echo_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                echo_at_type_0 = datetime.datetime.fromisoformat(data)



                return echo_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        echo_at = _parse_echo_at(d.pop("echo_at", UNSET))


        def _parse_pushed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pushed_at_type_0 = datetime.datetime.fromisoformat(data)



                return pushed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pushed_at = _parse_pushed_at(d.pop("pushed_at", UNSET))


        _reported = d.pop("reported", UNSET)
        reported: IotMcvCfgBaoKhai | Unset
        if isinstance(_reported,  Unset):
            reported = UNSET
        else:
            reported = IotMcvCfgBaoKhai.from_dict(_reported)




        def _parse_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seq = _parse_seq(d.pop("seq", UNSET))


        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        iot_mcv_cfg_state_dto = cls(
            ack=ack,
            desired=desired,
            echo_at=echo_at,
            pushed_at=pushed_at,
            reported=reported,
            seq=seq,
            state=state,
        )

        return iot_mcv_cfg_state_dto

