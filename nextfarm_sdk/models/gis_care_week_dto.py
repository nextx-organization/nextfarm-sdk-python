from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_care_week_plot_dto import GisCareWeekPlotDto





T = TypeVar("T", bound="GisCareWeekDto")



@_attrs_define
class GisCareWeekDto:
    

    plots: list[GisCareWeekPlotDto] | None | Unset = UNSET
    week_end: None | str | Unset = UNSET
    week_start: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_week_plot_dto import GisCareWeekPlotDto # noqa: PLC0415
        plots: list[dict[str, Any]] | None | Unset
        if isinstance(self.plots, Unset):
            plots = UNSET
        elif isinstance(self.plots, list):
            plots = []
            for plots_type_0_item_data in self.plots:
                plots_type_0_item = plots_type_0_item_data.to_dict()
                plots.append(plots_type_0_item)


        else:
            plots = self.plots

        week_end: None | str | Unset
        if isinstance(self.week_end, Unset):
            week_end = UNSET
        else:
            week_end = self.week_end

        week_start: None | str | Unset
        if isinstance(self.week_start, Unset):
            week_start = UNSET
        else:
            week_start = self.week_start


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if plots is not UNSET:
            field_dict["plots"] = plots
        if week_end is not UNSET:
            field_dict["week_end"] = week_end
        if week_start is not UNSET:
            field_dict["week_start"] = week_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_week_plot_dto import GisCareWeekPlotDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_plots(data: object) -> list[GisCareWeekPlotDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                plots_type_0 = []
                _plots_type_0 = data
                for plots_type_0_item_data in (_plots_type_0):
                    plots_type_0_item = GisCareWeekPlotDto.from_dict(plots_type_0_item_data)



                    plots_type_0.append(plots_type_0_item)

                return plots_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisCareWeekPlotDto] | None | Unset, data)

        plots = _parse_plots(d.pop("plots", UNSET))


        def _parse_week_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_end = _parse_week_end(d.pop("week_end", UNSET))


        def _parse_week_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        week_start = _parse_week_start(d.pop("week_start", UNSET))


        gis_care_week_dto = cls(
            plots=plots,
            week_end=week_end,
            week_start=week_start,
        )

        return gis_care_week_dto

