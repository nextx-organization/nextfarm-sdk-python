from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto
  from ..models.gis_care_week_group_dto import GisCareWeekGroupDto





T = TypeVar("T", bound="GisCarePreviewDto")



@_attrs_define
class GisCarePreviewDto:
    

    from_: None | str | Unset = UNSET
    items: list[GisCareOccurrenceDto] | None | Unset = UNSET
    to: None | str | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET
    weeks: list[GisCareWeekGroupDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
        from ..models.gis_care_week_group_dto import GisCareWeekGroupDto # noqa: PLC0415
        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings


        else:
            warnings = self.warnings

        weeks: list[dict[str, Any]] | None | Unset
        if isinstance(self.weeks, Unset):
            weeks = UNSET
        elif isinstance(self.weeks, list):
            weeks = []
            for weeks_type_0_item_data in self.weeks:
                weeks_type_0_item = weeks_type_0_item_data.to_dict()
                weeks.append(weeks_type_0_item)


        else:
            weeks = self.weeks


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if items is not UNSET:
            field_dict["items"] = items
        if to is not UNSET:
            field_dict["to"] = to
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if weeks is not UNSET:
            field_dict["weeks"] = weeks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
        from ..models.gis_care_week_group_dto import GisCareWeekGroupDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_items(data: object) -> list[GisCareOccurrenceDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = GisCareOccurrenceDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareOccurrenceDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        def _parse_weeks(data: object) -> list[GisCareWeekGroupDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weeks_type_0 = []
                _weeks_type_0 = data
                for weeks_type_0_item_data in (_weeks_type_0):
                    weeks_type_0_item = GisCareWeekGroupDto.from_dict(weeks_type_0_item_data)



                    weeks_type_0.append(weeks_type_0_item)

                return weeks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareWeekGroupDto] | None | Unset, data)

        weeks = _parse_weeks(d.pop("weeks", UNSET))


        gis_care_preview_dto = cls(
            from_=from_,
            items=items,
            to=to,
            warnings=warnings,
            weeks=weeks,
        )

        return gis_care_preview_dto

