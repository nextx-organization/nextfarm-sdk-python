from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_care_dose import GisCareDose





T = TypeVar("T", bound="GisCareRule")



@_attrs_define
class GisCareRule:
    

    age_from: int | None | Unset = UNSET
    age_to: int | None | Unset = UNSET
    anchor: None | str | Unset = UNSET
    day: int | None | Unset = UNSET
    day_offset: int | None | Unset = UNSET
    doses: list[GisCareDose] | None | Unset = UNSET
    event: None | str | Unset = UNSET
    every_days: int | None | Unset = UNSET
    from_day: int | None | Unset = UNSET
    from_month: int | None | Unset = UNSET
    key: None | str | Unset = UNSET
    material: None | str | Unset = UNSET
    month: int | None | Unset = UNSET
    note: None | str | Unset = UNSET
    offset_days: int | None | Unset = UNSET
    task_type: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    to_day: int | None | Unset = UNSET
    to_month: int | None | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_dose import GisCareDose # noqa: PLC0415
        age_from: int | None | Unset
        if isinstance(self.age_from, Unset):
            age_from = UNSET
        else:
            age_from = self.age_from

        age_to: int | None | Unset
        if isinstance(self.age_to, Unset):
            age_to = UNSET
        else:
            age_to = self.age_to

        anchor: None | str | Unset
        if isinstance(self.anchor, Unset):
            anchor = UNSET
        else:
            anchor = self.anchor

        day: int | None | Unset
        if isinstance(self.day, Unset):
            day = UNSET
        else:
            day = self.day

        day_offset: int | None | Unset
        if isinstance(self.day_offset, Unset):
            day_offset = UNSET
        else:
            day_offset = self.day_offset

        doses: list[dict[str, Any]] | None | Unset
        if isinstance(self.doses, Unset):
            doses = UNSET
        elif isinstance(self.doses, list):
            doses = []
            for doses_type_0_item_data in self.doses:
                doses_type_0_item = doses_type_0_item_data.to_dict()
                doses.append(doses_type_0_item)


        else:
            doses = self.doses

        event: None | str | Unset
        if isinstance(self.event, Unset):
            event = UNSET
        else:
            event = self.event

        every_days: int | None | Unset
        if isinstance(self.every_days, Unset):
            every_days = UNSET
        else:
            every_days = self.every_days

        from_day: int | None | Unset
        if isinstance(self.from_day, Unset):
            from_day = UNSET
        else:
            from_day = self.from_day

        from_month: int | None | Unset
        if isinstance(self.from_month, Unset):
            from_month = UNSET
        else:
            from_month = self.from_month

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        month: int | None | Unset
        if isinstance(self.month, Unset):
            month = UNSET
        else:
            month = self.month

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        offset_days: int | None | Unset
        if isinstance(self.offset_days, Unset):
            offset_days = UNSET
        else:
            offset_days = self.offset_days

        task_type: None | str | Unset
        if isinstance(self.task_type, Unset):
            task_type = UNSET
        else:
            task_type = self.task_type

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        to_day: int | None | Unset
        if isinstance(self.to_day, Unset):
            to_day = UNSET
        else:
            to_day = self.to_day

        to_month: int | None | Unset
        if isinstance(self.to_month, Unset):
            to_month = UNSET
        else:
            to_month = self.to_month

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if age_from is not UNSET:
            field_dict["age_from"] = age_from
        if age_to is not UNSET:
            field_dict["age_to"] = age_to
        if anchor is not UNSET:
            field_dict["anchor"] = anchor
        if day is not UNSET:
            field_dict["day"] = day
        if day_offset is not UNSET:
            field_dict["day_offset"] = day_offset
        if doses is not UNSET:
            field_dict["doses"] = doses
        if event is not UNSET:
            field_dict["event"] = event
        if every_days is not UNSET:
            field_dict["every_days"] = every_days
        if from_day is not UNSET:
            field_dict["from_day"] = from_day
        if from_month is not UNSET:
            field_dict["from_month"] = from_month
        if key is not UNSET:
            field_dict["key"] = key
        if material is not UNSET:
            field_dict["material"] = material
        if month is not UNSET:
            field_dict["month"] = month
        if note is not UNSET:
            field_dict["note"] = note
        if offset_days is not UNSET:
            field_dict["offset_days"] = offset_days
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if to_day is not UNSET:
            field_dict["to_day"] = to_day
        if to_month is not UNSET:
            field_dict["to_month"] = to_month
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_dose import GisCareDose # noqa: PLC0415
        d = dict(src_dict)
        def _parse_age_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_from = _parse_age_from(d.pop("age_from", UNSET))


        def _parse_age_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age_to = _parse_age_to(d.pop("age_to", UNSET))


        def _parse_anchor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor = _parse_anchor(d.pop("anchor", UNSET))


        def _parse_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day = _parse_day(d.pop("day", UNSET))


        def _parse_day_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day_offset = _parse_day_offset(d.pop("day_offset", UNSET))


        def _parse_doses(data: object) -> list[GisCareDose] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                doses_type_0 = []
                _doses_type_0 = data
                for doses_type_0_item_data in (_doses_type_0):
                    doses_type_0_item = GisCareDose.from_dict(doses_type_0_item_data)



                    doses_type_0.append(doses_type_0_item)

                return doses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareDose] | None | Unset, data)

        doses = _parse_doses(d.pop("doses", UNSET))


        def _parse_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event = _parse_event(d.pop("event", UNSET))


        def _parse_every_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        every_days = _parse_every_days(d.pop("every_days", UNSET))


        def _parse_from_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        from_day = _parse_from_day(d.pop("from_day", UNSET))


        def _parse_from_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        from_month = _parse_from_month(d.pop("from_month", UNSET))


        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("material", UNSET))


        def _parse_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        month = _parse_month(d.pop("month", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_offset_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset_days = _parse_offset_days(d.pop("offset_days", UNSET))


        def _parse_task_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_type = _parse_task_type(d.pop("task_type", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_to_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        to_day = _parse_to_day(d.pop("to_day", UNSET))


        def _parse_to_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        to_month = _parse_to_month(d.pop("to_month", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        gis_care_rule = cls(
            age_from=age_from,
            age_to=age_to,
            anchor=anchor,
            day=day,
            day_offset=day_offset,
            doses=doses,
            event=event,
            every_days=every_days,
            from_day=from_day,
            from_month=from_month,
            key=key,
            material=material,
            month=month,
            note=note,
            offset_days=offset_days,
            task_type=task_type,
            title=title,
            to_day=to_day,
            to_month=to_month,
            unit=unit,
        )

        return gis_care_rule

