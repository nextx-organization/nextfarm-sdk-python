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
  from ..models.iot_fert_meter_pulse_dto import IotFertMeterPulseDto
  from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto





T = TypeVar("T", bound="IotDeviceFertMetersDto")



@_attrs_define
class IotDeviceFertMetersDto:
    

    channels: list[IotFertMeterPulseDto] | None | Unset = UNSET
    chu_ky_bat_dau_luc: datetime.datetime | None | Unset = UNSET
    device_code: None | str | Unset = UNSET
    flow_pulse: int | None | Unset = UNSET
    muc_tieu_lit_chu_ky: int | None | Unset = UNSET
    pulse_at: datetime.datetime | None | Unset = UNSET
    pulse_ml: int | None | Unset = UNSET
    pulse_ul: int | None | Unset = UNSET
    water_chu_ky_server_tinh: IotTheTichServerTinhDto | Unset = UNSET
    water_server_tinh: IotTheTichServerTinhDto | Unset = UNSET
    water_ulp_operator: int | None | Unset = UNSET
    water_ulp_operator_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_fert_meter_pulse_dto import IotFertMeterPulseDto # noqa: PLC0415
        from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto # noqa: PLC0415
        channels: list[dict[str, Any]] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = []
            for channels_type_0_item_data in self.channels:
                channels_type_0_item = channels_type_0_item_data.to_dict()
                channels.append(channels_type_0_item)


        else:
            channels = self.channels

        chu_ky_bat_dau_luc: None | str | Unset
        if isinstance(self.chu_ky_bat_dau_luc, Unset):
            chu_ky_bat_dau_luc = UNSET
        elif isinstance(self.chu_ky_bat_dau_luc, datetime.datetime):
            chu_ky_bat_dau_luc = self.chu_ky_bat_dau_luc.isoformat()
        else:
            chu_ky_bat_dau_luc = self.chu_ky_bat_dau_luc

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        flow_pulse: int | None | Unset
        if isinstance(self.flow_pulse, Unset):
            flow_pulse = UNSET
        else:
            flow_pulse = self.flow_pulse

        muc_tieu_lit_chu_ky: int | None | Unset
        if isinstance(self.muc_tieu_lit_chu_ky, Unset):
            muc_tieu_lit_chu_ky = UNSET
        else:
            muc_tieu_lit_chu_ky = self.muc_tieu_lit_chu_ky

        pulse_at: None | str | Unset
        if isinstance(self.pulse_at, Unset):
            pulse_at = UNSET
        elif isinstance(self.pulse_at, datetime.datetime):
            pulse_at = self.pulse_at.isoformat()
        else:
            pulse_at = self.pulse_at

        pulse_ml: int | None | Unset
        if isinstance(self.pulse_ml, Unset):
            pulse_ml = UNSET
        else:
            pulse_ml = self.pulse_ml

        pulse_ul: int | None | Unset
        if isinstance(self.pulse_ul, Unset):
            pulse_ul = UNSET
        else:
            pulse_ul = self.pulse_ul

        water_chu_ky_server_tinh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.water_chu_ky_server_tinh, Unset):
            water_chu_ky_server_tinh = self.water_chu_ky_server_tinh.to_dict()

        water_server_tinh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.water_server_tinh, Unset):
            water_server_tinh = self.water_server_tinh.to_dict()

        water_ulp_operator: int | None | Unset
        if isinstance(self.water_ulp_operator, Unset):
            water_ulp_operator = UNSET
        else:
            water_ulp_operator = self.water_ulp_operator

        water_ulp_operator_at: None | str | Unset
        if isinstance(self.water_ulp_operator_at, Unset):
            water_ulp_operator_at = UNSET
        elif isinstance(self.water_ulp_operator_at, datetime.datetime):
            water_ulp_operator_at = self.water_ulp_operator_at.isoformat()
        else:
            water_ulp_operator_at = self.water_ulp_operator_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channels is not UNSET:
            field_dict["channels"] = channels
        if chu_ky_bat_dau_luc is not UNSET:
            field_dict["chu_ky_bat_dau_luc"] = chu_ky_bat_dau_luc
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if flow_pulse is not UNSET:
            field_dict["flow_pulse"] = flow_pulse
        if muc_tieu_lit_chu_ky is not UNSET:
            field_dict["muc_tieu_lit_chu_ky"] = muc_tieu_lit_chu_ky
        if pulse_at is not UNSET:
            field_dict["pulse_at"] = pulse_at
        if pulse_ml is not UNSET:
            field_dict["pulse_ml"] = pulse_ml
        if pulse_ul is not UNSET:
            field_dict["pulse_ul"] = pulse_ul
        if water_chu_ky_server_tinh is not UNSET:
            field_dict["water_chu_ky_server_tinh"] = water_chu_ky_server_tinh
        if water_server_tinh is not UNSET:
            field_dict["water_server_tinh"] = water_server_tinh
        if water_ulp_operator is not UNSET:
            field_dict["water_ulp_operator"] = water_ulp_operator
        if water_ulp_operator_at is not UNSET:
            field_dict["water_ulp_operator_at"] = water_ulp_operator_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_fert_meter_pulse_dto import IotFertMeterPulseDto # noqa: PLC0415
        from ..models.iot_the_tich_server_tinh_dto import IotTheTichServerTinhDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_channels(data: object) -> list[IotFertMeterPulseDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = []
                _channels_type_0 = data
                for channels_type_0_item_data in (_channels_type_0):
                    channels_type_0_item = IotFertMeterPulseDto.from_dict(channels_type_0_item_data)



                    channels_type_0.append(channels_type_0_item)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotFertMeterPulseDto] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))


        def _parse_chu_ky_bat_dau_luc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chu_ky_bat_dau_luc_type_0 = datetime.datetime.fromisoformat(data)



                return chu_ky_bat_dau_luc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        chu_ky_bat_dau_luc = _parse_chu_ky_bat_dau_luc(d.pop("chu_ky_bat_dau_luc", UNSET))


        def _parse_device_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_code = _parse_device_code(d.pop("device_code", UNSET))


        def _parse_flow_pulse(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flow_pulse = _parse_flow_pulse(d.pop("flow_pulse", UNSET))


        def _parse_muc_tieu_lit_chu_ky(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        muc_tieu_lit_chu_ky = _parse_muc_tieu_lit_chu_ky(d.pop("muc_tieu_lit_chu_ky", UNSET))


        def _parse_pulse_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pulse_at_type_0 = datetime.datetime.fromisoformat(data)



                return pulse_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pulse_at = _parse_pulse_at(d.pop("pulse_at", UNSET))


        def _parse_pulse_ml(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pulse_ml = _parse_pulse_ml(d.pop("pulse_ml", UNSET))


        def _parse_pulse_ul(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pulse_ul = _parse_pulse_ul(d.pop("pulse_ul", UNSET))


        _water_chu_ky_server_tinh = d.pop("water_chu_ky_server_tinh", UNSET)
        water_chu_ky_server_tinh: IotTheTichServerTinhDto | Unset
        if isinstance(_water_chu_ky_server_tinh,  Unset):
            water_chu_ky_server_tinh = UNSET
        else:
            water_chu_ky_server_tinh = IotTheTichServerTinhDto.from_dict(_water_chu_ky_server_tinh)




        _water_server_tinh = d.pop("water_server_tinh", UNSET)
        water_server_tinh: IotTheTichServerTinhDto | Unset
        if isinstance(_water_server_tinh,  Unset):
            water_server_tinh = UNSET
        else:
            water_server_tinh = IotTheTichServerTinhDto.from_dict(_water_server_tinh)




        def _parse_water_ulp_operator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        water_ulp_operator = _parse_water_ulp_operator(d.pop("water_ulp_operator", UNSET))


        def _parse_water_ulp_operator_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                water_ulp_operator_at_type_0 = datetime.datetime.fromisoformat(data)



                return water_ulp_operator_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        water_ulp_operator_at = _parse_water_ulp_operator_at(d.pop("water_ulp_operator_at", UNSET))


        iot_device_fert_meters_dto = cls(
            channels=channels,
            chu_ky_bat_dau_luc=chu_ky_bat_dau_luc,
            device_code=device_code,
            flow_pulse=flow_pulse,
            muc_tieu_lit_chu_ky=muc_tieu_lit_chu_ky,
            pulse_at=pulse_at,
            pulse_ml=pulse_ml,
            pulse_ul=pulse_ul,
            water_chu_ky_server_tinh=water_chu_ky_server_tinh,
            water_server_tinh=water_server_tinh,
            water_ulp_operator=water_ulp_operator,
            water_ulp_operator_at=water_ulp_operator_at,
        )

        return iot_device_fert_meters_dto

