from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="IotDeviceIrrigationOutputDto")



@_attrs_define
class IotDeviceIrrigationOutputDto:
    

    idx: int | Unset = UNSET
    kind: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    manual_max_min_bo: int | None | Unset = UNSET
    mcv_id: int | None | Unset = UNSET
    meter_echo_at: datetime.datetime | None | Unset = UNSET
    meter_id: int | None | Unset = UNSET
    meter_in: int | None | Unset = UNSET
    meter_ulp: int | None | Unset = UNSET
    meter_ulp_operator: int | None | Unset = UNSET
    meter_ulp_operator_at: datetime.datetime | None | Unset = UNSET
    meter_ulp_pushed: int | None | Unset = UNSET
    meter_ulp_pushed_at: datetime.datetime | None | Unset = UNSET
    out: int | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    role: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        idx = self.idx

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

        manual_max_min_bo: int | None | Unset
        if isinstance(self.manual_max_min_bo, Unset):
            manual_max_min_bo = UNSET
        else:
            manual_max_min_bo = self.manual_max_min_bo

        mcv_id: int | None | Unset
        if isinstance(self.mcv_id, Unset):
            mcv_id = UNSET
        else:
            mcv_id = self.mcv_id

        meter_echo_at: None | str | Unset
        if isinstance(self.meter_echo_at, Unset):
            meter_echo_at = UNSET
        elif isinstance(self.meter_echo_at, datetime.datetime):
            meter_echo_at = self.meter_echo_at.isoformat()
        else:
            meter_echo_at = self.meter_echo_at

        meter_id: int | None | Unset
        if isinstance(self.meter_id, Unset):
            meter_id = UNSET
        else:
            meter_id = self.meter_id

        meter_in: int | None | Unset
        if isinstance(self.meter_in, Unset):
            meter_in = UNSET
        else:
            meter_in = self.meter_in

        meter_ulp: int | None | Unset
        if isinstance(self.meter_ulp, Unset):
            meter_ulp = UNSET
        else:
            meter_ulp = self.meter_ulp

        meter_ulp_operator: int | None | Unset
        if isinstance(self.meter_ulp_operator, Unset):
            meter_ulp_operator = UNSET
        else:
            meter_ulp_operator = self.meter_ulp_operator

        meter_ulp_operator_at: None | str | Unset
        if isinstance(self.meter_ulp_operator_at, Unset):
            meter_ulp_operator_at = UNSET
        elif isinstance(self.meter_ulp_operator_at, datetime.datetime):
            meter_ulp_operator_at = self.meter_ulp_operator_at.isoformat()
        else:
            meter_ulp_operator_at = self.meter_ulp_operator_at

        meter_ulp_pushed: int | None | Unset
        if isinstance(self.meter_ulp_pushed, Unset):
            meter_ulp_pushed = UNSET
        else:
            meter_ulp_pushed = self.meter_ulp_pushed

        meter_ulp_pushed_at: None | str | Unset
        if isinstance(self.meter_ulp_pushed_at, Unset):
            meter_ulp_pushed_at = UNSET
        elif isinstance(self.meter_ulp_pushed_at, datetime.datetime):
            meter_ulp_pushed_at = self.meter_ulp_pushed_at.isoformat()
        else:
            meter_ulp_pushed_at = self.meter_ulp_pushed_at

        out = self.out

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if idx is not UNSET:
            field_dict["idx"] = idx
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if manual_max_min_bo is not UNSET:
            field_dict["manual_max_min_bo"] = manual_max_min_bo
        if mcv_id is not UNSET:
            field_dict["mcv_id"] = mcv_id
        if meter_echo_at is not UNSET:
            field_dict["meter_echo_at"] = meter_echo_at
        if meter_id is not UNSET:
            field_dict["meter_id"] = meter_id
        if meter_in is not UNSET:
            field_dict["meter_in"] = meter_in
        if meter_ulp is not UNSET:
            field_dict["meter_ulp"] = meter_ulp
        if meter_ulp_operator is not UNSET:
            field_dict["meter_ulp_operator"] = meter_ulp_operator
        if meter_ulp_operator_at is not UNSET:
            field_dict["meter_ulp_operator_at"] = meter_ulp_operator_at
        if meter_ulp_pushed is not UNSET:
            field_dict["meter_ulp_pushed"] = meter_ulp_pushed
        if meter_ulp_pushed_at is not UNSET:
            field_dict["meter_ulp_pushed_at"] = meter_ulp_pushed_at
        if out is not UNSET:
            field_dict["out"] = out
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if role is not UNSET:
            field_dict["role"] = role
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idx = d.pop("idx", UNSET)

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


        def _parse_manual_max_min_bo(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        manual_max_min_bo = _parse_manual_max_min_bo(d.pop("manual_max_min_bo", UNSET))


        def _parse_mcv_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv_id = _parse_mcv_id(d.pop("mcv_id", UNSET))


        def _parse_meter_echo_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meter_echo_at_type_0 = datetime.datetime.fromisoformat(data)



                return meter_echo_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        meter_echo_at = _parse_meter_echo_at(d.pop("meter_echo_at", UNSET))


        def _parse_meter_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        meter_id = _parse_meter_id(d.pop("meter_id", UNSET))


        def _parse_meter_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        meter_in = _parse_meter_in(d.pop("meter_in", UNSET))


        def _parse_meter_ulp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        meter_ulp = _parse_meter_ulp(d.pop("meter_ulp", UNSET))


        def _parse_meter_ulp_operator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        meter_ulp_operator = _parse_meter_ulp_operator(d.pop("meter_ulp_operator", UNSET))


        def _parse_meter_ulp_operator_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meter_ulp_operator_at_type_0 = datetime.datetime.fromisoformat(data)



                return meter_ulp_operator_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        meter_ulp_operator_at = _parse_meter_ulp_operator_at(d.pop("meter_ulp_operator_at", UNSET))


        def _parse_meter_ulp_pushed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        meter_ulp_pushed = _parse_meter_ulp_pushed(d.pop("meter_ulp_pushed", UNSET))


        def _parse_meter_ulp_pushed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meter_ulp_pushed_at_type_0 = datetime.datetime.fromisoformat(data)



                return meter_ulp_pushed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        meter_ulp_pushed_at = _parse_meter_ulp_pushed_at(d.pop("meter_ulp_pushed_at", UNSET))


        out = d.pop("out", UNSET)

        def _parse_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parcel_id_type_0 = UUID(data)



                return parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parcel_id = _parse_parcel_id(d.pop("parcel_id", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        iot_device_irrigation_output_dto = cls(
            idx=idx,
            kind=kind,
            label=label,
            manual_max_min_bo=manual_max_min_bo,
            mcv_id=mcv_id,
            meter_echo_at=meter_echo_at,
            meter_id=meter_id,
            meter_in=meter_in,
            meter_ulp=meter_ulp,
            meter_ulp_operator=meter_ulp_operator,
            meter_ulp_operator_at=meter_ulp_operator_at,
            meter_ulp_pushed=meter_ulp_pushed,
            meter_ulp_pushed_at=meter_ulp_pushed_at,
            out=out,
            parcel_id=parcel_id,
            role=role,
            updated_at=updated_at,
        )

        return iot_device_irrigation_output_dto

