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






T = TypeVar("T", bound="IotSensorReadingDto")



@_attrs_define
class IotSensorReadingDto:
    

    activity_pct: float | None | Unset = UNSET
    air_humidity_pct: float | None | Unset = UNSET
    air_humidity_pct1: float | None | Unset = UNSET
    air_humidity_pct2: float | None | Unset = UNSET
    air_humidity_pct3: float | None | Unset = UNSET
    air_temp_c: float | None | Unset = UNSET
    air_temp_c1: float | None | Unset = UNSET
    air_temp_c2: float | None | Unset = UNSET
    air_temp_c3: float | None | Unset = UNSET
    co2_ppm: float | None | Unset = UNSET
    device_code: None | str | Unset = UNSET
    device_id: UUID | Unset = UNSET
    do_mg_l: float | None | Unset = UNSET
    ec_us_cm: float | None | Unset = UNSET
    feed_level_pct1: float | None | Unset = UNSET
    feed_level_pct2: float | None | Unset = UNSET
    feed_weight_kg1: float | None | Unset = UNSET
    feed_weight_kg2: float | None | Unset = UNSET
    fert_ec_us_cm: float | None | Unset = UNSET
    fert_ph: float | None | Unset = UNSET
    fw_ver: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    light_lux: float | None | Unset = UNSET
    nh3_ppm: float | None | Unset = UNSET
    orp_mv: float | None | Unset = UNSET
    ph: float | None | Unset = UNSET
    rssi: int | None | Unset = UNSET
    salinity_ppt: float | None | Unset = UNSET
    soil_ec_us_cm: float | None | Unset = UNSET
    soil_moisture_pct1: float | None | Unset = UNSET
    soil_moisture_pct2: float | None | Unset = UNSET
    soil_moisture_pct3: float | None | Unset = UNSET
    soil_moisture_pct4: float | None | Unset = UNSET
    soil_moisture_pct5: float | None | Unset = UNSET
    soil_temp_c: float | None | Unset = UNSET
    ts: datetime.datetime | Unset = UNSET
    turbidity_ntu: float | None | Unset = UNSET
    vertical: None | str | Unset = UNSET
    water_flow_lpm: float | None | Unset = UNSET
    water_level_cm: float | None | Unset = UNSET
    water_temp_c1: float | None | Unset = UNSET
    water_temp_c2: float | None | Unset = UNSET
    water_temp_c3: float | None | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    zone_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        activity_pct: float | None | Unset
        if isinstance(self.activity_pct, Unset):
            activity_pct = UNSET
        else:
            activity_pct = self.activity_pct

        air_humidity_pct: float | None | Unset
        if isinstance(self.air_humidity_pct, Unset):
            air_humidity_pct = UNSET
        else:
            air_humidity_pct = self.air_humidity_pct

        air_humidity_pct1: float | None | Unset
        if isinstance(self.air_humidity_pct1, Unset):
            air_humidity_pct1 = UNSET
        else:
            air_humidity_pct1 = self.air_humidity_pct1

        air_humidity_pct2: float | None | Unset
        if isinstance(self.air_humidity_pct2, Unset):
            air_humidity_pct2 = UNSET
        else:
            air_humidity_pct2 = self.air_humidity_pct2

        air_humidity_pct3: float | None | Unset
        if isinstance(self.air_humidity_pct3, Unset):
            air_humidity_pct3 = UNSET
        else:
            air_humidity_pct3 = self.air_humidity_pct3

        air_temp_c: float | None | Unset
        if isinstance(self.air_temp_c, Unset):
            air_temp_c = UNSET
        else:
            air_temp_c = self.air_temp_c

        air_temp_c1: float | None | Unset
        if isinstance(self.air_temp_c1, Unset):
            air_temp_c1 = UNSET
        else:
            air_temp_c1 = self.air_temp_c1

        air_temp_c2: float | None | Unset
        if isinstance(self.air_temp_c2, Unset):
            air_temp_c2 = UNSET
        else:
            air_temp_c2 = self.air_temp_c2

        air_temp_c3: float | None | Unset
        if isinstance(self.air_temp_c3, Unset):
            air_temp_c3 = UNSET
        else:
            air_temp_c3 = self.air_temp_c3

        co2_ppm: float | None | Unset
        if isinstance(self.co2_ppm, Unset):
            co2_ppm = UNSET
        else:
            co2_ppm = self.co2_ppm

        device_code: None | str | Unset
        if isinstance(self.device_code, Unset):
            device_code = UNSET
        else:
            device_code = self.device_code

        device_id: str | Unset = UNSET
        if not isinstance(self.device_id, Unset):
            device_id = str(self.device_id)

        do_mg_l: float | None | Unset
        if isinstance(self.do_mg_l, Unset):
            do_mg_l = UNSET
        else:
            do_mg_l = self.do_mg_l

        ec_us_cm: float | None | Unset
        if isinstance(self.ec_us_cm, Unset):
            ec_us_cm = UNSET
        else:
            ec_us_cm = self.ec_us_cm

        feed_level_pct1: float | None | Unset
        if isinstance(self.feed_level_pct1, Unset):
            feed_level_pct1 = UNSET
        else:
            feed_level_pct1 = self.feed_level_pct1

        feed_level_pct2: float | None | Unset
        if isinstance(self.feed_level_pct2, Unset):
            feed_level_pct2 = UNSET
        else:
            feed_level_pct2 = self.feed_level_pct2

        feed_weight_kg1: float | None | Unset
        if isinstance(self.feed_weight_kg1, Unset):
            feed_weight_kg1 = UNSET
        else:
            feed_weight_kg1 = self.feed_weight_kg1

        feed_weight_kg2: float | None | Unset
        if isinstance(self.feed_weight_kg2, Unset):
            feed_weight_kg2 = UNSET
        else:
            feed_weight_kg2 = self.feed_weight_kg2

        fert_ec_us_cm: float | None | Unset
        if isinstance(self.fert_ec_us_cm, Unset):
            fert_ec_us_cm = UNSET
        else:
            fert_ec_us_cm = self.fert_ec_us_cm

        fert_ph: float | None | Unset
        if isinstance(self.fert_ph, Unset):
            fert_ph = UNSET
        else:
            fert_ph = self.fert_ph

        fw_ver: None | str | Unset
        if isinstance(self.fw_ver, Unset):
            fw_ver = UNSET
        else:
            fw_ver = self.fw_ver

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        light_lux: float | None | Unset
        if isinstance(self.light_lux, Unset):
            light_lux = UNSET
        else:
            light_lux = self.light_lux

        nh3_ppm: float | None | Unset
        if isinstance(self.nh3_ppm, Unset):
            nh3_ppm = UNSET
        else:
            nh3_ppm = self.nh3_ppm

        orp_mv: float | None | Unset
        if isinstance(self.orp_mv, Unset):
            orp_mv = UNSET
        else:
            orp_mv = self.orp_mv

        ph: float | None | Unset
        if isinstance(self.ph, Unset):
            ph = UNSET
        else:
            ph = self.ph

        rssi: int | None | Unset
        if isinstance(self.rssi, Unset):
            rssi = UNSET
        else:
            rssi = self.rssi

        salinity_ppt: float | None | Unset
        if isinstance(self.salinity_ppt, Unset):
            salinity_ppt = UNSET
        else:
            salinity_ppt = self.salinity_ppt

        soil_ec_us_cm: float | None | Unset
        if isinstance(self.soil_ec_us_cm, Unset):
            soil_ec_us_cm = UNSET
        else:
            soil_ec_us_cm = self.soil_ec_us_cm

        soil_moisture_pct1: float | None | Unset
        if isinstance(self.soil_moisture_pct1, Unset):
            soil_moisture_pct1 = UNSET
        else:
            soil_moisture_pct1 = self.soil_moisture_pct1

        soil_moisture_pct2: float | None | Unset
        if isinstance(self.soil_moisture_pct2, Unset):
            soil_moisture_pct2 = UNSET
        else:
            soil_moisture_pct2 = self.soil_moisture_pct2

        soil_moisture_pct3: float | None | Unset
        if isinstance(self.soil_moisture_pct3, Unset):
            soil_moisture_pct3 = UNSET
        else:
            soil_moisture_pct3 = self.soil_moisture_pct3

        soil_moisture_pct4: float | None | Unset
        if isinstance(self.soil_moisture_pct4, Unset):
            soil_moisture_pct4 = UNSET
        else:
            soil_moisture_pct4 = self.soil_moisture_pct4

        soil_moisture_pct5: float | None | Unset
        if isinstance(self.soil_moisture_pct5, Unset):
            soil_moisture_pct5 = UNSET
        else:
            soil_moisture_pct5 = self.soil_moisture_pct5

        soil_temp_c: float | None | Unset
        if isinstance(self.soil_temp_c, Unset):
            soil_temp_c = UNSET
        else:
            soil_temp_c = self.soil_temp_c

        ts: str | Unset = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.isoformat()

        turbidity_ntu: float | None | Unset
        if isinstance(self.turbidity_ntu, Unset):
            turbidity_ntu = UNSET
        else:
            turbidity_ntu = self.turbidity_ntu

        vertical: None | str | Unset
        if isinstance(self.vertical, Unset):
            vertical = UNSET
        else:
            vertical = self.vertical

        water_flow_lpm: float | None | Unset
        if isinstance(self.water_flow_lpm, Unset):
            water_flow_lpm = UNSET
        else:
            water_flow_lpm = self.water_flow_lpm

        water_level_cm: float | None | Unset
        if isinstance(self.water_level_cm, Unset):
            water_level_cm = UNSET
        else:
            water_level_cm = self.water_level_cm

        water_temp_c1: float | None | Unset
        if isinstance(self.water_temp_c1, Unset):
            water_temp_c1 = UNSET
        else:
            water_temp_c1 = self.water_temp_c1

        water_temp_c2: float | None | Unset
        if isinstance(self.water_temp_c2, Unset):
            water_temp_c2 = UNSET
        else:
            water_temp_c2 = self.water_temp_c2

        water_temp_c3: float | None | Unset
        if isinstance(self.water_temp_c3, Unset):
            water_temp_c3 = UNSET
        else:
            water_temp_c3 = self.water_temp_c3

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        zone_id: str | Unset = UNSET
        if not isinstance(self.zone_id, Unset):
            zone_id = str(self.zone_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activity_pct is not UNSET:
            field_dict["activity_pct"] = activity_pct
        if air_humidity_pct is not UNSET:
            field_dict["air_humidity_pct"] = air_humidity_pct
        if air_humidity_pct1 is not UNSET:
            field_dict["air_humidity_pct1"] = air_humidity_pct1
        if air_humidity_pct2 is not UNSET:
            field_dict["air_humidity_pct2"] = air_humidity_pct2
        if air_humidity_pct3 is not UNSET:
            field_dict["air_humidity_pct3"] = air_humidity_pct3
        if air_temp_c is not UNSET:
            field_dict["air_temp_c"] = air_temp_c
        if air_temp_c1 is not UNSET:
            field_dict["air_temp_c1"] = air_temp_c1
        if air_temp_c2 is not UNSET:
            field_dict["air_temp_c2"] = air_temp_c2
        if air_temp_c3 is not UNSET:
            field_dict["air_temp_c3"] = air_temp_c3
        if co2_ppm is not UNSET:
            field_dict["co2_ppm"] = co2_ppm
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if do_mg_l is not UNSET:
            field_dict["do_mg_l"] = do_mg_l
        if ec_us_cm is not UNSET:
            field_dict["ec_us_cm"] = ec_us_cm
        if feed_level_pct1 is not UNSET:
            field_dict["feed_level_pct1"] = feed_level_pct1
        if feed_level_pct2 is not UNSET:
            field_dict["feed_level_pct2"] = feed_level_pct2
        if feed_weight_kg1 is not UNSET:
            field_dict["feed_weight_kg1"] = feed_weight_kg1
        if feed_weight_kg2 is not UNSET:
            field_dict["feed_weight_kg2"] = feed_weight_kg2
        if fert_ec_us_cm is not UNSET:
            field_dict["fert_ec_us_cm"] = fert_ec_us_cm
        if fert_ph is not UNSET:
            field_dict["fert_ph"] = fert_ph
        if fw_ver is not UNSET:
            field_dict["fw_ver"] = fw_ver
        if id is not UNSET:
            field_dict["id"] = id
        if light_lux is not UNSET:
            field_dict["light_lux"] = light_lux
        if nh3_ppm is not UNSET:
            field_dict["nh3_ppm"] = nh3_ppm
        if orp_mv is not UNSET:
            field_dict["orp_mv"] = orp_mv
        if ph is not UNSET:
            field_dict["ph"] = ph
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if salinity_ppt is not UNSET:
            field_dict["salinity_ppt"] = salinity_ppt
        if soil_ec_us_cm is not UNSET:
            field_dict["soil_ec_us_cm"] = soil_ec_us_cm
        if soil_moisture_pct1 is not UNSET:
            field_dict["soil_moisture_pct1"] = soil_moisture_pct1
        if soil_moisture_pct2 is not UNSET:
            field_dict["soil_moisture_pct2"] = soil_moisture_pct2
        if soil_moisture_pct3 is not UNSET:
            field_dict["soil_moisture_pct3"] = soil_moisture_pct3
        if soil_moisture_pct4 is not UNSET:
            field_dict["soil_moisture_pct4"] = soil_moisture_pct4
        if soil_moisture_pct5 is not UNSET:
            field_dict["soil_moisture_pct5"] = soil_moisture_pct5
        if soil_temp_c is not UNSET:
            field_dict["soil_temp_c"] = soil_temp_c
        if ts is not UNSET:
            field_dict["ts"] = ts
        if turbidity_ntu is not UNSET:
            field_dict["turbidity_ntu"] = turbidity_ntu
        if vertical is not UNSET:
            field_dict["vertical"] = vertical
        if water_flow_lpm is not UNSET:
            field_dict["water_flow_lpm"] = water_flow_lpm
        if water_level_cm is not UNSET:
            field_dict["water_level_cm"] = water_level_cm
        if water_temp_c1 is not UNSET:
            field_dict["water_temp_c1"] = water_temp_c1
        if water_temp_c2 is not UNSET:
            field_dict["water_temp_c2"] = water_temp_c2
        if water_temp_c3 is not UNSET:
            field_dict["water_temp_c3"] = water_temp_c3
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_activity_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        activity_pct = _parse_activity_pct(d.pop("activity_pct", UNSET))


        def _parse_air_humidity_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_humidity_pct = _parse_air_humidity_pct(d.pop("air_humidity_pct", UNSET))


        def _parse_air_humidity_pct1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_humidity_pct1 = _parse_air_humidity_pct1(d.pop("air_humidity_pct1", UNSET))


        def _parse_air_humidity_pct2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_humidity_pct2 = _parse_air_humidity_pct2(d.pop("air_humidity_pct2", UNSET))


        def _parse_air_humidity_pct3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_humidity_pct3 = _parse_air_humidity_pct3(d.pop("air_humidity_pct3", UNSET))


        def _parse_air_temp_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_temp_c = _parse_air_temp_c(d.pop("air_temp_c", UNSET))


        def _parse_air_temp_c1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_temp_c1 = _parse_air_temp_c1(d.pop("air_temp_c1", UNSET))


        def _parse_air_temp_c2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_temp_c2 = _parse_air_temp_c2(d.pop("air_temp_c2", UNSET))


        def _parse_air_temp_c3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        air_temp_c3 = _parse_air_temp_c3(d.pop("air_temp_c3", UNSET))


        def _parse_co2_ppm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        co2_ppm = _parse_co2_ppm(d.pop("co2_ppm", UNSET))


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




        def _parse_do_mg_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        do_mg_l = _parse_do_mg_l(d.pop("do_mg_l", UNSET))


        def _parse_ec_us_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ec_us_cm = _parse_ec_us_cm(d.pop("ec_us_cm", UNSET))


        def _parse_feed_level_pct1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_level_pct1 = _parse_feed_level_pct1(d.pop("feed_level_pct1", UNSET))


        def _parse_feed_level_pct2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_level_pct2 = _parse_feed_level_pct2(d.pop("feed_level_pct2", UNSET))


        def _parse_feed_weight_kg1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_weight_kg1 = _parse_feed_weight_kg1(d.pop("feed_weight_kg1", UNSET))


        def _parse_feed_weight_kg2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        feed_weight_kg2 = _parse_feed_weight_kg2(d.pop("feed_weight_kg2", UNSET))


        def _parse_fert_ec_us_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fert_ec_us_cm = _parse_fert_ec_us_cm(d.pop("fert_ec_us_cm", UNSET))


        def _parse_fert_ph(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fert_ph = _parse_fert_ph(d.pop("fert_ph", UNSET))


        def _parse_fw_ver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fw_ver = _parse_fw_ver(d.pop("fw_ver", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_light_lux(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        light_lux = _parse_light_lux(d.pop("light_lux", UNSET))


        def _parse_nh3_ppm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nh3_ppm = _parse_nh3_ppm(d.pop("nh3_ppm", UNSET))


        def _parse_orp_mv(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        orp_mv = _parse_orp_mv(d.pop("orp_mv", UNSET))


        def _parse_ph(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ph = _parse_ph(d.pop("ph", UNSET))


        def _parse_rssi(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rssi = _parse_rssi(d.pop("rssi", UNSET))


        def _parse_salinity_ppt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        salinity_ppt = _parse_salinity_ppt(d.pop("salinity_ppt", UNSET))


        def _parse_soil_ec_us_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_ec_us_cm = _parse_soil_ec_us_cm(d.pop("soil_ec_us_cm", UNSET))


        def _parse_soil_moisture_pct1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_moisture_pct1 = _parse_soil_moisture_pct1(d.pop("soil_moisture_pct1", UNSET))


        def _parse_soil_moisture_pct2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_moisture_pct2 = _parse_soil_moisture_pct2(d.pop("soil_moisture_pct2", UNSET))


        def _parse_soil_moisture_pct3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_moisture_pct3 = _parse_soil_moisture_pct3(d.pop("soil_moisture_pct3", UNSET))


        def _parse_soil_moisture_pct4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_moisture_pct4 = _parse_soil_moisture_pct4(d.pop("soil_moisture_pct4", UNSET))


        def _parse_soil_moisture_pct5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_moisture_pct5 = _parse_soil_moisture_pct5(d.pop("soil_moisture_pct5", UNSET))


        def _parse_soil_temp_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soil_temp_c = _parse_soil_temp_c(d.pop("soil_temp_c", UNSET))


        _ts = d.pop("ts", UNSET)
        ts: datetime.datetime | Unset
        if isinstance(_ts,  Unset):
            ts = UNSET
        else:
            ts = datetime.datetime.fromisoformat(_ts)




        def _parse_turbidity_ntu(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        turbidity_ntu = _parse_turbidity_ntu(d.pop("turbidity_ntu", UNSET))


        def _parse_vertical(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vertical = _parse_vertical(d.pop("vertical", UNSET))


        def _parse_water_flow_lpm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_flow_lpm = _parse_water_flow_lpm(d.pop("water_flow_lpm", UNSET))


        def _parse_water_level_cm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_level_cm = _parse_water_level_cm(d.pop("water_level_cm", UNSET))


        def _parse_water_temp_c1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_temp_c1 = _parse_water_temp_c1(d.pop("water_temp_c1", UNSET))


        def _parse_water_temp_c2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_temp_c2 = _parse_water_temp_c2(d.pop("water_temp_c2", UNSET))


        def _parse_water_temp_c3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_temp_c3 = _parse_water_temp_c3(d.pop("water_temp_c3", UNSET))


        _workspace_id = d.pop("workspace_id", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        _zone_id = d.pop("zone_id", UNSET)
        zone_id: UUID | Unset
        if isinstance(_zone_id,  Unset):
            zone_id = UNSET
        else:
            zone_id = UUID(_zone_id)




        iot_sensor_reading_dto = cls(
            activity_pct=activity_pct,
            air_humidity_pct=air_humidity_pct,
            air_humidity_pct1=air_humidity_pct1,
            air_humidity_pct2=air_humidity_pct2,
            air_humidity_pct3=air_humidity_pct3,
            air_temp_c=air_temp_c,
            air_temp_c1=air_temp_c1,
            air_temp_c2=air_temp_c2,
            air_temp_c3=air_temp_c3,
            co2_ppm=co2_ppm,
            device_code=device_code,
            device_id=device_id,
            do_mg_l=do_mg_l,
            ec_us_cm=ec_us_cm,
            feed_level_pct1=feed_level_pct1,
            feed_level_pct2=feed_level_pct2,
            feed_weight_kg1=feed_weight_kg1,
            feed_weight_kg2=feed_weight_kg2,
            fert_ec_us_cm=fert_ec_us_cm,
            fert_ph=fert_ph,
            fw_ver=fw_ver,
            id=id,
            light_lux=light_lux,
            nh3_ppm=nh3_ppm,
            orp_mv=orp_mv,
            ph=ph,
            rssi=rssi,
            salinity_ppt=salinity_ppt,
            soil_ec_us_cm=soil_ec_us_cm,
            soil_moisture_pct1=soil_moisture_pct1,
            soil_moisture_pct2=soil_moisture_pct2,
            soil_moisture_pct3=soil_moisture_pct3,
            soil_moisture_pct4=soil_moisture_pct4,
            soil_moisture_pct5=soil_moisture_pct5,
            soil_temp_c=soil_temp_c,
            ts=ts,
            turbidity_ntu=turbidity_ntu,
            vertical=vertical,
            water_flow_lpm=water_flow_lpm,
            water_level_cm=water_level_cm,
            water_temp_c1=water_temp_c1,
            water_temp_c2=water_temp_c2,
            water_temp_c3=water_temp_c3,
            workspace_id=workspace_id,
            zone_id=zone_id,
        )

        return iot_sensor_reading_dto

