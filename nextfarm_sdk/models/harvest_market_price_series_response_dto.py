from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_market_price_series_dto import HarvestMarketPriceSeriesDto





T = TypeVar("T", bound="HarvestMarketPriceSeriesResponseDto")



@_attrs_define
class HarvestMarketPriceSeriesResponseDto:
    

    series: list[HarvestMarketPriceSeriesDto] | None | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_market_price_series_dto import HarvestMarketPriceSeriesDto # noqa: PLC0415
        series: list[dict[str, Any]] | None | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        elif isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)


        else:
            series = self.series

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if series is not UNSET:
            field_dict["series"] = series
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_market_price_series_dto import HarvestMarketPriceSeriesDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_series(data: object) -> list[HarvestMarketPriceSeriesDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in (_series_type_0):
                    series_type_0_item = HarvestMarketPriceSeriesDto.from_dict(series_type_0_item_data)



                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestMarketPriceSeriesDto] | None | Unset, data)

        series = _parse_series(d.pop("series", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        harvest_market_price_series_response_dto = cls(
            series=series,
            unit=unit,
        )

        return harvest_market_price_series_response_dto

