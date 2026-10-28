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

if TYPE_CHECKING:
  from ..models.iot_control_field_dto import IotControlFieldDto
  from ..models.iot_device_output_dto import IotDeviceOutputDto





T = TypeVar("T", bound="IotDeviceControlStateDto")



@_attrs_define
class IotDeviceControlStateDto:
    

    catalog: list[IotControlFieldDto] | None | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    device_outputs: list[IotDeviceOutputDto] | None | Unset = UNSET
    fert1_open: bool | Unset = UNSET
    fert2_open: bool | Unset = UNSET
    fert_open_mask: int | Unset = UNSET
    fert_pump_lock: int | None | Unset = UNSET
    fert_pump_run: int | None | Unset = UNSET
    fert_pump_suy_ra: int | None | Unset = UNSET
    fert_pump_why: int | None | Unset = UNSET
    flow_lmin: float | None | Unset = UNSET
    is_gateway_firmware: bool | Unset = UNSET
    is_online: bool | Unset = UNSET
    mcv_run: Any | Unset = UNSET
    outputs: int | Unset = UNSET
    pump_flushing: bool | Unset = UNSET
    pump_irrigating: bool | Unset = UNSET
    pump_mode: int | None | Unset = UNSET
    pump_on: bool | Unset = UNSET
    reported_at: datetime.datetime | None | Unset = UNSET
    shade: int | None | Unset = UNSET
    shade_closing: bool | Unset = UNSET
    shade_opening: bool | Unset = UNSET
    vol_cur_ml: int | None | Unset = UNSET
    winch1: int | None | Unset = UNSET
    winch1_closing: bool | Unset = UNSET
    winch1_opening: bool | Unset = UNSET
    winch2: int | None | Unset = UNSET
    winch2_closing: bool | Unset = UNSET
    winch2_opening: bool | Unset = UNSET
    zone_open: bool | Unset = UNSET
    zone_open_mask: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_control_field_dto import IotControlFieldDto # noqa: PLC0415
        from ..models.iot_device_output_dto import IotDeviceOutputDto # noqa: PLC0415
        catalog: list[dict[str, Any]] | None | Unset
        if isinstance(self.catalog, Unset):
            catalog = UNSET
        elif isinstance(self.catalog, list):
            catalog = []
            for catalog_type_0_item_data in self.catalog:
                catalog_type_0_item = catalog_type_0_item_data.to_dict()
                catalog.append(catalog_type_0_item)


        else:
            catalog = self.catalog

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        device_outputs: list[dict[str, Any]] | None | Unset
        if isinstance(self.device_outputs, Unset):
            device_outputs = UNSET
        elif isinstance(self.device_outputs, list):
            device_outputs = []
            for device_outputs_type_0_item_data in self.device_outputs:
                device_outputs_type_0_item = device_outputs_type_0_item_data.to_dict()
                device_outputs.append(device_outputs_type_0_item)


        else:
            device_outputs = self.device_outputs

        fert1_open = self.fert1_open

        fert2_open = self.fert2_open

        fert_open_mask = self.fert_open_mask

        fert_pump_lock: int | None | Unset
        if isinstance(self.fert_pump_lock, Unset):
            fert_pump_lock = UNSET
        else:
            fert_pump_lock = self.fert_pump_lock

        fert_pump_run: int | None | Unset
        if isinstance(self.fert_pump_run, Unset):
            fert_pump_run = UNSET
        else:
            fert_pump_run = self.fert_pump_run

        fert_pump_suy_ra: int | None | Unset
        if isinstance(self.fert_pump_suy_ra, Unset):
            fert_pump_suy_ra = UNSET
        else:
            fert_pump_suy_ra = self.fert_pump_suy_ra

        fert_pump_why: int | None | Unset
        if isinstance(self.fert_pump_why, Unset):
            fert_pump_why = UNSET
        else:
            fert_pump_why = self.fert_pump_why

        flow_lmin: float | None | Unset
        if isinstance(self.flow_lmin, Unset):
            flow_lmin = UNSET
        else:
            flow_lmin = self.flow_lmin

        is_gateway_firmware = self.is_gateway_firmware

        is_online = self.is_online

        mcv_run = self.mcv_run

        outputs = self.outputs

        pump_flushing = self.pump_flushing

        pump_irrigating = self.pump_irrigating

        pump_mode: int | None | Unset
        if isinstance(self.pump_mode, Unset):
            pump_mode = UNSET
        else:
            pump_mode = self.pump_mode

        pump_on = self.pump_on

        reported_at: None | str | Unset
        if isinstance(self.reported_at, Unset):
            reported_at = UNSET
        elif isinstance(self.reported_at, datetime.datetime):
            reported_at = self.reported_at.isoformat()
        else:
            reported_at = self.reported_at

        shade: int | None | Unset
        if isinstance(self.shade, Unset):
            shade = UNSET
        else:
            shade = self.shade

        shade_closing = self.shade_closing

        shade_opening = self.shade_opening

        vol_cur_ml: int | None | Unset
        if isinstance(self.vol_cur_ml, Unset):
            vol_cur_ml = UNSET
        else:
            vol_cur_ml = self.vol_cur_ml

        winch1: int | None | Unset
        if isinstance(self.winch1, Unset):
            winch1 = UNSET
        else:
            winch1 = self.winch1

        winch1_closing = self.winch1_closing

        winch1_opening = self.winch1_opening

        winch2: int | None | Unset
        if isinstance(self.winch2, Unset):
            winch2 = UNSET
        else:
            winch2 = self.winch2

        winch2_closing = self.winch2_closing

        winch2_opening = self.winch2_opening

        zone_open = self.zone_open

        zone_open_mask = self.zone_open_mask


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_outputs is not UNSET:
            field_dict["device_outputs"] = device_outputs
        if fert1_open is not UNSET:
            field_dict["fert1_open"] = fert1_open
        if fert2_open is not UNSET:
            field_dict["fert2_open"] = fert2_open
        if fert_open_mask is not UNSET:
            field_dict["fert_open_mask"] = fert_open_mask
        if fert_pump_lock is not UNSET:
            field_dict["fert_pump_lock"] = fert_pump_lock
        if fert_pump_run is not UNSET:
            field_dict["fert_pump_run"] = fert_pump_run
        if fert_pump_suy_ra is not UNSET:
            field_dict["fert_pump_suy_ra"] = fert_pump_suy_ra
        if fert_pump_why is not UNSET:
            field_dict["fert_pump_why"] = fert_pump_why
        if flow_lmin is not UNSET:
            field_dict["flow_lmin"] = flow_lmin
        if is_gateway_firmware is not UNSET:
            field_dict["is_gateway_firmware"] = is_gateway_firmware
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if mcv_run is not UNSET:
            field_dict["mcv_run"] = mcv_run
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if pump_flushing is not UNSET:
            field_dict["pump_flushing"] = pump_flushing
        if pump_irrigating is not UNSET:
            field_dict["pump_irrigating"] = pump_irrigating
        if pump_mode is not UNSET:
            field_dict["pump_mode"] = pump_mode
        if pump_on is not UNSET:
            field_dict["pump_on"] = pump_on
        if reported_at is not UNSET:
            field_dict["reported_at"] = reported_at
        if shade is not UNSET:
            field_dict["shade"] = shade
        if shade_closing is not UNSET:
            field_dict["shade_closing"] = shade_closing
        if shade_opening is not UNSET:
            field_dict["shade_opening"] = shade_opening
        if vol_cur_ml is not UNSET:
            field_dict["vol_cur_ml"] = vol_cur_ml
        if winch1 is not UNSET:
            field_dict["winch1"] = winch1
        if winch1_closing is not UNSET:
            field_dict["winch1_closing"] = winch1_closing
        if winch1_opening is not UNSET:
            field_dict["winch1_opening"] = winch1_opening
        if winch2 is not UNSET:
            field_dict["winch2"] = winch2
        if winch2_closing is not UNSET:
            field_dict["winch2_closing"] = winch2_closing
        if winch2_opening is not UNSET:
            field_dict["winch2_opening"] = winch2_opening
        if zone_open is not UNSET:
            field_dict["zone_open"] = zone_open
        if zone_open_mask is not UNSET:
            field_dict["zone_open_mask"] = zone_open_mask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_control_field_dto import IotControlFieldDto # noqa: PLC0415
        from ..models.iot_device_output_dto import IotDeviceOutputDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_catalog(data: object) -> list[IotControlFieldDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                catalog_type_0 = []
                _catalog_type_0 = data
                for catalog_type_0_item_data in (_catalog_type_0):
                    catalog_type_0_item = IotControlFieldDto.from_dict(catalog_type_0_item_data)



                    catalog_type_0.append(catalog_type_0_item)

                return catalog_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotControlFieldDto] | None | Unset, data)

        catalog = _parse_catalog(d.pop("catalog", UNSET))


        def _parse_device_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_code = _parse_device_code(d.pop("device_code", UNSET))


        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_device_outputs(data: object) -> list[IotDeviceOutputDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                device_outputs_type_0 = []
                _device_outputs_type_0 = data
                for device_outputs_type_0_item_data in (_device_outputs_type_0):
                    device_outputs_type_0_item = IotDeviceOutputDto.from_dict(device_outputs_type_0_item_data)



                    device_outputs_type_0.append(device_outputs_type_0_item)

                return device_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotDeviceOutputDto] | None | Unset, data)

        device_outputs = _parse_device_outputs(d.pop("device_outputs", UNSET))


        fert1_open = d.pop("fert1_open", UNSET)

        fert2_open = d.pop("fert2_open", UNSET)

        fert_open_mask = d.pop("fert_open_mask", UNSET)

        def _parse_fert_pump_lock(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_pump_lock = _parse_fert_pump_lock(d.pop("fert_pump_lock", UNSET))


        def _parse_fert_pump_run(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_pump_run = _parse_fert_pump_run(d.pop("fert_pump_run", UNSET))


        def _parse_fert_pump_suy_ra(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_pump_suy_ra = _parse_fert_pump_suy_ra(d.pop("fert_pump_suy_ra", UNSET))


        def _parse_fert_pump_why(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert_pump_why = _parse_fert_pump_why(d.pop("fert_pump_why", UNSET))


        def _parse_flow_lmin(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flow_lmin = _parse_flow_lmin(d.pop("flow_lmin", UNSET))


        is_gateway_firmware = d.pop("is_gateway_firmware", UNSET)

        is_online = d.pop("is_online", UNSET)

        mcv_run = d.pop("mcv_run", UNSET)

        outputs = d.pop("outputs", UNSET)

        pump_flushing = d.pop("pump_flushing", UNSET)

        pump_irrigating = d.pop("pump_irrigating", UNSET)

        def _parse_pump_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pump_mode = _parse_pump_mode(d.pop("pump_mode", UNSET))


        pump_on = d.pop("pump_on", UNSET)

        def _parse_reported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reported_at_type_0 = datetime.datetime.fromisoformat(data)



                return reported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reported_at = _parse_reported_at(d.pop("reported_at", UNSET))


        def _parse_shade(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shade = _parse_shade(d.pop("shade", UNSET))


        shade_closing = d.pop("shade_closing", UNSET)

        shade_opening = d.pop("shade_opening", UNSET)

        def _parse_vol_cur_ml(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vol_cur_ml = _parse_vol_cur_ml(d.pop("vol_cur_ml", UNSET))


        def _parse_winch1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        winch1 = _parse_winch1(d.pop("winch1", UNSET))


        winch1_closing = d.pop("winch1_closing", UNSET)

        winch1_opening = d.pop("winch1_opening", UNSET)

        def _parse_winch2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        winch2 = _parse_winch2(d.pop("winch2", UNSET))


        winch2_closing = d.pop("winch2_closing", UNSET)

        winch2_opening = d.pop("winch2_opening", UNSET)

        zone_open = d.pop("zone_open", UNSET)

        zone_open_mask = d.pop("zone_open_mask", UNSET)

        iot_device_control_state_dto = cls(
            catalog=catalog,
            device_code=device_code,
            device_id=device_id,
            device_outputs=device_outputs,
            fert1_open=fert1_open,
            fert2_open=fert2_open,
            fert_open_mask=fert_open_mask,
            fert_pump_lock=fert_pump_lock,
            fert_pump_run=fert_pump_run,
            fert_pump_suy_ra=fert_pump_suy_ra,
            fert_pump_why=fert_pump_why,
            flow_lmin=flow_lmin,
            is_gateway_firmware=is_gateway_firmware,
            is_online=is_online,
            mcv_run=mcv_run,
            outputs=outputs,
            pump_flushing=pump_flushing,
            pump_irrigating=pump_irrigating,
            pump_mode=pump_mode,
            pump_on=pump_on,
            reported_at=reported_at,
            shade=shade,
            shade_closing=shade_closing,
            shade_opening=shade_opening,
            vol_cur_ml=vol_cur_ml,
            winch1=winch1,
            winch1_closing=winch1_closing,
            winch1_opening=winch1_opening,
            winch2=winch2,
            winch2_closing=winch2_closing,
            winch2_opening=winch2_opening,
            zone_open=zone_open,
            zone_open_mask=zone_open_mask,
        )

        return iot_device_control_state_dto

