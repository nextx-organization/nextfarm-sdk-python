from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotDeviceSetpointsDto")



@_attrs_define
class IotDeviceSetpointsDto:
    

    alarm_temp: int | None | Unset = UNSET
    auto_fan: int | None | Unset = UNSET
    auto_shade: int | None | Unset = UNSET
    auto_winch1: int | None | Unset = UNSET
    auto_winch2: int | None | Unset = UNSET
    device_id: UUID | Unset = UNSET
    fert1_rate: int | None | Unset = UNSET
    fert2_rate: int | None | Unset = UNSET
    flow_pulse_ml: int | None | Unset = UNSET
    mcv1: int | None | Unset = UNSET
    mcv2: int | None | Unset = UNSET
    mcv3: int | None | Unset = UNSET
    mcv4: int | None | Unset = UNSET
    mcv5: int | None | Unset = UNSET
    mcv6: int | None | Unset = UNSET
    sched_s_eh: int | None | Unset = UNSET
    sched_s_em: int | None | Unset = UNSET
    sched_s_sh: int | None | Unset = UNSET
    sched_s_sm: int | None | Unset = UNSET
    sched_w_eh: int | None | Unset = UNSET
    sched_w_em: int | None | Unset = UNSET
    sched_w_sh: int | None | Unset = UNSET
    sched_w_sm: int | None | Unset = UNSET
    thresh_fan_hum_off: int | None | Unset = UNSET
    thresh_fan_hum_on: int | None | Unset = UNSET
    thresh_fan_temp_off: int | None | Unset = UNSET
    thresh_fan_temp_on: int | None | Unset = UNSET
    thresh_lux_sh_close: int | None | Unset = UNSET
    thresh_lux_sh_open: int | None | Unset = UNSET
    thresh_lux_w_close: int | None | Unset = UNSET
    thresh_lux_w_open: int | None | Unset = UNSET
    thresh_sh_close: int | None | Unset = UNSET
    thresh_sh_open: int | None | Unset = UNSET
    thresh_w_close: int | None | Unset = UNSET
    thresh_w_open: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        alarm_temp: int | None | Unset
        if isinstance(self.alarm_temp, Unset):
            alarm_temp = UNSET
        else:
            alarm_temp = self.alarm_temp

        auto_fan: int | None | Unset
        if isinstance(self.auto_fan, Unset):
            auto_fan = UNSET
        else:
            auto_fan = self.auto_fan

        auto_shade: int | None | Unset
        if isinstance(self.auto_shade, Unset):
            auto_shade = UNSET
        else:
            auto_shade = self.auto_shade

        auto_winch1: int | None | Unset
        if isinstance(self.auto_winch1, Unset):
            auto_winch1 = UNSET
        else:
            auto_winch1 = self.auto_winch1

        auto_winch2: int | None | Unset
        if isinstance(self.auto_winch2, Unset):
            auto_winch2 = UNSET
        else:
            auto_winch2 = self.auto_winch2

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        fert1_rate: int | None | Unset
        if isinstance(self.fert1_rate, Unset):
            fert1_rate = UNSET
        else:
            fert1_rate = self.fert1_rate

        fert2_rate: int | None | Unset
        if isinstance(self.fert2_rate, Unset):
            fert2_rate = UNSET
        else:
            fert2_rate = self.fert2_rate

        flow_pulse_ml: int | None | Unset
        if isinstance(self.flow_pulse_ml, Unset):
            flow_pulse_ml = UNSET
        else:
            flow_pulse_ml = self.flow_pulse_ml

        mcv1: int | None | Unset
        if isinstance(self.mcv1, Unset):
            mcv1 = UNSET
        else:
            mcv1 = self.mcv1

        mcv2: int | None | Unset
        if isinstance(self.mcv2, Unset):
            mcv2 = UNSET
        else:
            mcv2 = self.mcv2

        mcv3: int | None | Unset
        if isinstance(self.mcv3, Unset):
            mcv3 = UNSET
        else:
            mcv3 = self.mcv3

        mcv4: int | None | Unset
        if isinstance(self.mcv4, Unset):
            mcv4 = UNSET
        else:
            mcv4 = self.mcv4

        mcv5: int | None | Unset
        if isinstance(self.mcv5, Unset):
            mcv5 = UNSET
        else:
            mcv5 = self.mcv5

        mcv6: int | None | Unset
        if isinstance(self.mcv6, Unset):
            mcv6 = UNSET
        else:
            mcv6 = self.mcv6

        sched_s_eh: int | None | Unset
        if isinstance(self.sched_s_eh, Unset):
            sched_s_eh = UNSET
        else:
            sched_s_eh = self.sched_s_eh

        sched_s_em: int | None | Unset
        if isinstance(self.sched_s_em, Unset):
            sched_s_em = UNSET
        else:
            sched_s_em = self.sched_s_em

        sched_s_sh: int | None | Unset
        if isinstance(self.sched_s_sh, Unset):
            sched_s_sh = UNSET
        else:
            sched_s_sh = self.sched_s_sh

        sched_s_sm: int | None | Unset
        if isinstance(self.sched_s_sm, Unset):
            sched_s_sm = UNSET
        else:
            sched_s_sm = self.sched_s_sm

        sched_w_eh: int | None | Unset
        if isinstance(self.sched_w_eh, Unset):
            sched_w_eh = UNSET
        else:
            sched_w_eh = self.sched_w_eh

        sched_w_em: int | None | Unset
        if isinstance(self.sched_w_em, Unset):
            sched_w_em = UNSET
        else:
            sched_w_em = self.sched_w_em

        sched_w_sh: int | None | Unset
        if isinstance(self.sched_w_sh, Unset):
            sched_w_sh = UNSET
        else:
            sched_w_sh = self.sched_w_sh

        sched_w_sm: int | None | Unset
        if isinstance(self.sched_w_sm, Unset):
            sched_w_sm = UNSET
        else:
            sched_w_sm = self.sched_w_sm

        thresh_fan_hum_off: int | None | Unset
        if isinstance(self.thresh_fan_hum_off, Unset):
            thresh_fan_hum_off = UNSET
        else:
            thresh_fan_hum_off = self.thresh_fan_hum_off

        thresh_fan_hum_on: int | None | Unset
        if isinstance(self.thresh_fan_hum_on, Unset):
            thresh_fan_hum_on = UNSET
        else:
            thresh_fan_hum_on = self.thresh_fan_hum_on

        thresh_fan_temp_off: int | None | Unset
        if isinstance(self.thresh_fan_temp_off, Unset):
            thresh_fan_temp_off = UNSET
        else:
            thresh_fan_temp_off = self.thresh_fan_temp_off

        thresh_fan_temp_on: int | None | Unset
        if isinstance(self.thresh_fan_temp_on, Unset):
            thresh_fan_temp_on = UNSET
        else:
            thresh_fan_temp_on = self.thresh_fan_temp_on

        thresh_lux_sh_close: int | None | Unset
        if isinstance(self.thresh_lux_sh_close, Unset):
            thresh_lux_sh_close = UNSET
        else:
            thresh_lux_sh_close = self.thresh_lux_sh_close

        thresh_lux_sh_open: int | None | Unset
        if isinstance(self.thresh_lux_sh_open, Unset):
            thresh_lux_sh_open = UNSET
        else:
            thresh_lux_sh_open = self.thresh_lux_sh_open

        thresh_lux_w_close: int | None | Unset
        if isinstance(self.thresh_lux_w_close, Unset):
            thresh_lux_w_close = UNSET
        else:
            thresh_lux_w_close = self.thresh_lux_w_close

        thresh_lux_w_open: int | None | Unset
        if isinstance(self.thresh_lux_w_open, Unset):
            thresh_lux_w_open = UNSET
        else:
            thresh_lux_w_open = self.thresh_lux_w_open

        thresh_sh_close: int | None | Unset
        if isinstance(self.thresh_sh_close, Unset):
            thresh_sh_close = UNSET
        else:
            thresh_sh_close = self.thresh_sh_close

        thresh_sh_open: int | None | Unset
        if isinstance(self.thresh_sh_open, Unset):
            thresh_sh_open = UNSET
        else:
            thresh_sh_open = self.thresh_sh_open

        thresh_w_close: int | None | Unset
        if isinstance(self.thresh_w_close, Unset):
            thresh_w_close = UNSET
        else:
            thresh_w_close = self.thresh_w_close

        thresh_w_open: int | None | Unset
        if isinstance(self.thresh_w_open, Unset):
            thresh_w_open = UNSET
        else:
            thresh_w_open = self.thresh_w_open


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if alarm_temp is not UNSET:
            field_dict["alarm_temp"] = alarm_temp
        if auto_fan is not UNSET:
            field_dict["auto_fan"] = auto_fan
        if auto_shade is not UNSET:
            field_dict["auto_shade"] = auto_shade
        if auto_winch1 is not UNSET:
            field_dict["auto_winch1"] = auto_winch1
        if auto_winch2 is not UNSET:
            field_dict["auto_winch2"] = auto_winch2
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if fert1_rate is not UNSET:
            field_dict["fert1_rate"] = fert1_rate
        if fert2_rate is not UNSET:
            field_dict["fert2_rate"] = fert2_rate
        if flow_pulse_ml is not UNSET:
            field_dict["flow_pulse_ml"] = flow_pulse_ml
        if mcv1 is not UNSET:
            field_dict["mcv1"] = mcv1
        if mcv2 is not UNSET:
            field_dict["mcv2"] = mcv2
        if mcv3 is not UNSET:
            field_dict["mcv3"] = mcv3
        if mcv4 is not UNSET:
            field_dict["mcv4"] = mcv4
        if mcv5 is not UNSET:
            field_dict["mcv5"] = mcv5
        if mcv6 is not UNSET:
            field_dict["mcv6"] = mcv6
        if sched_s_eh is not UNSET:
            field_dict["sched_s_eh"] = sched_s_eh
        if sched_s_em is not UNSET:
            field_dict["sched_s_em"] = sched_s_em
        if sched_s_sh is not UNSET:
            field_dict["sched_s_sh"] = sched_s_sh
        if sched_s_sm is not UNSET:
            field_dict["sched_s_sm"] = sched_s_sm
        if sched_w_eh is not UNSET:
            field_dict["sched_w_eh"] = sched_w_eh
        if sched_w_em is not UNSET:
            field_dict["sched_w_em"] = sched_w_em
        if sched_w_sh is not UNSET:
            field_dict["sched_w_sh"] = sched_w_sh
        if sched_w_sm is not UNSET:
            field_dict["sched_w_sm"] = sched_w_sm
        if thresh_fan_hum_off is not UNSET:
            field_dict["thresh_fan_hum_off"] = thresh_fan_hum_off
        if thresh_fan_hum_on is not UNSET:
            field_dict["thresh_fan_hum_on"] = thresh_fan_hum_on
        if thresh_fan_temp_off is not UNSET:
            field_dict["thresh_fan_temp_off"] = thresh_fan_temp_off
        if thresh_fan_temp_on is not UNSET:
            field_dict["thresh_fan_temp_on"] = thresh_fan_temp_on
        if thresh_lux_sh_close is not UNSET:
            field_dict["thresh_lux_sh_close"] = thresh_lux_sh_close
        if thresh_lux_sh_open is not UNSET:
            field_dict["thresh_lux_sh_open"] = thresh_lux_sh_open
        if thresh_lux_w_close is not UNSET:
            field_dict["thresh_lux_w_close"] = thresh_lux_w_close
        if thresh_lux_w_open is not UNSET:
            field_dict["thresh_lux_w_open"] = thresh_lux_w_open
        if thresh_sh_close is not UNSET:
            field_dict["thresh_sh_close"] = thresh_sh_close
        if thresh_sh_open is not UNSET:
            field_dict["thresh_sh_open"] = thresh_sh_open
        if thresh_w_close is not UNSET:
            field_dict["thresh_w_close"] = thresh_w_close
        if thresh_w_open is not UNSET:
            field_dict["thresh_w_open"] = thresh_w_open

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_alarm_temp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        alarm_temp = _parse_alarm_temp(d.pop("alarm_temp", UNSET))


        def _parse_auto_fan(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_fan = _parse_auto_fan(d.pop("auto_fan", UNSET))


        def _parse_auto_shade(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_shade = _parse_auto_shade(d.pop("auto_shade", UNSET))


        def _parse_auto_winch1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_winch1 = _parse_auto_winch1(d.pop("auto_winch1", UNSET))


        def _parse_auto_winch2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_winch2 = _parse_auto_winch2(d.pop("auto_winch2", UNSET))


        _device_id = d.pop("device_id", UNSET)
        device_id: UUID | Unset
        if isinstance(_device_id,  Unset):
            device_id = UNSET
        else:
            device_id = UUID(_device_id)




        def _parse_fert1_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert1_rate = _parse_fert1_rate(d.pop("fert1_rate", UNSET))


        def _parse_fert2_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fert2_rate = _parse_fert2_rate(d.pop("fert2_rate", UNSET))


        def _parse_flow_pulse_ml(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flow_pulse_ml = _parse_flow_pulse_ml(d.pop("flow_pulse_ml", UNSET))


        def _parse_mcv1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv1 = _parse_mcv1(d.pop("mcv1", UNSET))


        def _parse_mcv2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv2 = _parse_mcv2(d.pop("mcv2", UNSET))


        def _parse_mcv3(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv3 = _parse_mcv3(d.pop("mcv3", UNSET))


        def _parse_mcv4(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv4 = _parse_mcv4(d.pop("mcv4", UNSET))


        def _parse_mcv5(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv5 = _parse_mcv5(d.pop("mcv5", UNSET))


        def _parse_mcv6(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mcv6 = _parse_mcv6(d.pop("mcv6", UNSET))


        def _parse_sched_s_eh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_s_eh = _parse_sched_s_eh(d.pop("sched_s_eh", UNSET))


        def _parse_sched_s_em(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_s_em = _parse_sched_s_em(d.pop("sched_s_em", UNSET))


        def _parse_sched_s_sh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_s_sh = _parse_sched_s_sh(d.pop("sched_s_sh", UNSET))


        def _parse_sched_s_sm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_s_sm = _parse_sched_s_sm(d.pop("sched_s_sm", UNSET))


        def _parse_sched_w_eh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_w_eh = _parse_sched_w_eh(d.pop("sched_w_eh", UNSET))


        def _parse_sched_w_em(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_w_em = _parse_sched_w_em(d.pop("sched_w_em", UNSET))


        def _parse_sched_w_sh(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_w_sh = _parse_sched_w_sh(d.pop("sched_w_sh", UNSET))


        def _parse_sched_w_sm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sched_w_sm = _parse_sched_w_sm(d.pop("sched_w_sm", UNSET))


        def _parse_thresh_fan_hum_off(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_fan_hum_off = _parse_thresh_fan_hum_off(d.pop("thresh_fan_hum_off", UNSET))


        def _parse_thresh_fan_hum_on(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_fan_hum_on = _parse_thresh_fan_hum_on(d.pop("thresh_fan_hum_on", UNSET))


        def _parse_thresh_fan_temp_off(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_fan_temp_off = _parse_thresh_fan_temp_off(d.pop("thresh_fan_temp_off", UNSET))


        def _parse_thresh_fan_temp_on(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_fan_temp_on = _parse_thresh_fan_temp_on(d.pop("thresh_fan_temp_on", UNSET))


        def _parse_thresh_lux_sh_close(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_lux_sh_close = _parse_thresh_lux_sh_close(d.pop("thresh_lux_sh_close", UNSET))


        def _parse_thresh_lux_sh_open(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_lux_sh_open = _parse_thresh_lux_sh_open(d.pop("thresh_lux_sh_open", UNSET))


        def _parse_thresh_lux_w_close(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_lux_w_close = _parse_thresh_lux_w_close(d.pop("thresh_lux_w_close", UNSET))


        def _parse_thresh_lux_w_open(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_lux_w_open = _parse_thresh_lux_w_open(d.pop("thresh_lux_w_open", UNSET))


        def _parse_thresh_sh_close(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_sh_close = _parse_thresh_sh_close(d.pop("thresh_sh_close", UNSET))


        def _parse_thresh_sh_open(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_sh_open = _parse_thresh_sh_open(d.pop("thresh_sh_open", UNSET))


        def _parse_thresh_w_close(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_w_close = _parse_thresh_w_close(d.pop("thresh_w_close", UNSET))


        def _parse_thresh_w_open(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        thresh_w_open = _parse_thresh_w_open(d.pop("thresh_w_open", UNSET))


        iot_device_setpoints_dto = cls(
            alarm_temp=alarm_temp,
            auto_fan=auto_fan,
            auto_shade=auto_shade,
            auto_winch1=auto_winch1,
            auto_winch2=auto_winch2,
            device_id=device_id,
            fert1_rate=fert1_rate,
            fert2_rate=fert2_rate,
            flow_pulse_ml=flow_pulse_ml,
            mcv1=mcv1,
            mcv2=mcv2,
            mcv3=mcv3,
            mcv4=mcv4,
            mcv5=mcv5,
            mcv6=mcv6,
            sched_s_eh=sched_s_eh,
            sched_s_em=sched_s_em,
            sched_s_sh=sched_s_sh,
            sched_s_sm=sched_s_sm,
            sched_w_eh=sched_w_eh,
            sched_w_em=sched_w_em,
            sched_w_sh=sched_w_sh,
            sched_w_sm=sched_w_sm,
            thresh_fan_hum_off=thresh_fan_hum_off,
            thresh_fan_hum_on=thresh_fan_hum_on,
            thresh_fan_temp_off=thresh_fan_temp_off,
            thresh_fan_temp_on=thresh_fan_temp_on,
            thresh_lux_sh_close=thresh_lux_sh_close,
            thresh_lux_sh_open=thresh_lux_sh_open,
            thresh_lux_w_close=thresh_lux_w_close,
            thresh_lux_w_open=thresh_lux_w_open,
            thresh_sh_close=thresh_sh_close,
            thresh_sh_open=thresh_sh_open,
            thresh_w_close=thresh_w_close,
            thresh_w_open=thresh_w_open,
        )

        return iot_device_setpoints_dto

