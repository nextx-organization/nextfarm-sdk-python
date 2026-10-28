from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_market_price_point_dto import HarvestMarketPricePointDto





T = TypeVar("T", bound="HarvestMarketPriceSeriesDto")



@_attrs_define
class HarvestMarketPriceSeriesDto:
    

    commodity_code: None | str | Unset = UNSET
    commodity_name: None | str | Unset = UNSET
    points: list[HarvestMarketPricePointDto] | None | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_market_price_point_dto import HarvestMarketPricePointDto # noqa: PLC0415
        commodity_code: None | str | Unset
        if isinstance(self.commodity_code, Unset):
            commodity_code = UNSET
        else:
            commodity_code = self.commodity_code

        commodity_name: None | str | Unset
        if isinstance(self.commodity_name, Unset):
            commodity_name = UNSET
        else:
            commodity_name = self.commodity_name

        points: list[dict[str, Any]] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)


        else:
            points = self.points

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if commodity_code is not UNSET:
            field_dict["commodity_code"] = commodity_code
        if commodity_name is not UNSET:
            field_dict["commodity_name"] = commodity_name
        if points is not UNSET:
            field_dict["points"] = points
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_market_price_point_dto import HarvestMarketPricePointDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_commodity_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commodity_code = _parse_commodity_code(d.pop("commodity_code", UNSET))


        def _parse_commodity_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commodity_name = _parse_commodity_name(d.pop("commodity_name", UNSET))


        def _parse_points(data: object) -> list[HarvestMarketPricePointDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in (_points_type_0):
                    points_type_0_item = HarvestMarketPricePointDto.from_dict(points_type_0_item_data)



                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestMarketPricePointDto] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))


        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        harvest_market_price_series_dto = cls(
            commodity_code=commodity_code,
            commodity_name=commodity_name,
            points=points,
            unit=unit,
        )

        return harvest_market_price_series_dto

