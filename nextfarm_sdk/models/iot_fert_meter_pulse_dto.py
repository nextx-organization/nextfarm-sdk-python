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
  from ..models.iot_dong_bo_he_so_dto import IotDongBoHeSoDto
  from ..models.iot_lit_phan_chu_ky_dto import IotLitPhanChuKyDto
  from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto





T = TypeVar("T", bound="IotFertMeterPulseDto")



@_attrs_define
class IotFertMeterPulseDto:
    

    chu_ky_ly_do: None | str | Unset = UNSET
    chu_ky_server_tinh: IotLitPhanChuKyDto | Unset = UNSET
    cu_truoc_lit: float | None | Unset = UNSET
    dong_bo: IotDongBoHeSoDto | Unset = UNSET
    idx: int | Unset = UNSET
    meter_id: int | None | Unset = UNSET
    meter_in: int | None | Unset = UNSET
    meter_ulp: int | None | Unset = UNSET
    meter_ulp_operator: int | None | Unset = UNSET
    meter_ulp_operator_at: datetime.datetime | None | Unset = UNSET
    pulse: int | None | Unset = UNSET
    server_tinh: IotTheTichServerTinhDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_dong_bo_he_so_dto import IotDongBoHeSoDto # noqa: PLC0415
        from ..models.iot_lit_phan_chu_ky_dto import IotLitPhanChuKyDto # noqa: PLC0415
        from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto # noqa: PLC0415
        chu_ky_ly_do: None | str | Unset
        if isinstance(self.chu_ky_ly_do, Unset):
            chu_ky_ly_do = UNSET
        else:
            chu_ky_ly_do = self.chu_ky_ly_do

        chu_ky_server_tinh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chu_ky_server_tinh, Unset):
            chu_ky_server_tinh = self.chu_ky_server_tinh.to_dict()

        cu_truoc_lit: float | None | Unset
        if isinstance(self.cu_truoc_lit, Unset):
            cu_truoc_lit = UNSET
        else:
            cu_truoc_lit = self.cu_truoc_lit

        dong_bo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dong_bo, Unset):
            dong_bo = self.dong_bo.to_dict()

        idx = self.idx

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

        pulse: int | None | Unset
        if isinstance(self.pulse, Unset):
            pulse = UNSET
        else:
            pulse = self.pulse

        server_tinh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_tinh, Unset):
            server_tinh = self.server_tinh.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if chu_ky_ly_do is not UNSET:
            field_dict["chu_ky_ly_do"] = chu_ky_ly_do
        if chu_ky_server_tinh is not UNSET:
            field_dict["chu_ky_server_tinh"] = chu_ky_server_tinh
        if cu_truoc_lit is not UNSET:
            field_dict["cu_truoc_lit"] = cu_truoc_lit
        if dong_bo is not UNSET:
            field_dict["dong_bo"] = dong_bo
        if idx is not UNSET:
            field_dict["idx"] = idx
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
        if pulse is not UNSET:
            field_dict["pulse"] = pulse
        if server_tinh is not UNSET:
            field_dict["server_tinh"] = server_tinh

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_dong_bo_he_so_dto import IotDongBoHeSoDto # noqa: PLC0415
        from ..models.iot_lit_phan_chu_ky_dto import IotLitPhanChuKyDto # noqa: PLC0415
        from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_chu_ky_ly_do(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chu_ky_ly_do = _parse_chu_ky_ly_do(d.pop("chu_ky_ly_do", UNSET))


        _chu_ky_server_tinh = d.pop("chu_ky_server_tinh", UNSET)
        chu_ky_server_tinh: IotLitPhanChuKyDto | Unset
        if isinstance(_chu_ky_server_tinh,  Unset):
            chu_ky_server_tinh = UNSET
        else:
            chu_ky_server_tinh = IotLitPhanChuKyDto.from_dict(_chu_ky_server_tinh)




        def _parse_cu_truoc_lit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cu_truoc_lit = _parse_cu_truoc_lit(d.pop("cu_truoc_lit", UNSET))


        _dong_bo = d.pop("dong_bo", UNSET)
        dong_bo: IotDongBoHeSoDto | Unset
        if isinstance(_dong_bo,  Unset):
            dong_bo = UNSET
        else:
            dong_bo = IotDongBoHeSoDto.from_dict(_dong_bo)




        idx = d.pop("idx", UNSET)

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


        def _parse_pulse(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pulse = _parse_pulse(d.pop("pulse", UNSET))


        _server_tinh = d.pop("server_tinh", UNSET)
        server_tinh: IotTheTichServerTinhDto | Unset
        if isinstance(_server_tinh,  Unset):
            server_tinh = UNSET
        else:
            server_tinh = IotTheTichServerTinhDto.from_dict(_server_tinh)




        iot_fert_meter_pulse_dto = cls(
            chu_ky_ly_do=chu_ky_ly_do,
            chu_ky_server_tinh=chu_ky_server_tinh,
            cu_truoc_lit=cu_truoc_lit,
            dong_bo=dong_bo,
            idx=idx,
            meter_id=meter_id,
            meter_in=meter_in,
            meter_ulp=meter_ulp,
            meter_ulp_operator=meter_ulp_operator,
            meter_ulp_operator_at=meter_ulp_operator_at,
            pulse=pulse,
            server_tinh=server_tinh,
        )

        return iot_fert_meter_pulse_dto

