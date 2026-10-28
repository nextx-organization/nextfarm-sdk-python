from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto





T = TypeVar("T", bound="GisCareWeekPlotDto")



@_attrs_define
class GisCareWeekPlotDto:
    

    activation_id: UUID | Unset = UNSET
    delivery: None | str | Unset = UNSET
    items: list[GisCareOccurrenceDto] | None | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    plot_name: None | str | Unset = UNSET
    template_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
        activation_id: str | Unset = UNSET
        if not isinstance(self.activation_id, Unset):
            activation_id = str(self.activation_id)

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        else:
            delivery = self.delivery

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

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        plot_id: None | str | Unset
        if isinstance(self.plot_id, Unset):
            plot_id = UNSET
        elif isinstance(self.plot_id, UUID):
            plot_id = str(self.plot_id)
        else:
            plot_id = self.plot_id

        plot_name: None | str | Unset
        if isinstance(self.plot_name, Unset):
            plot_name = UNSET
        else:
            plot_name = self.plot_name

        template_name: None | str | Unset
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activation_id is not UNSET:
            field_dict["activation_id"] = activation_id
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if items is not UNSET:
            field_dict["items"] = items
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if plot_name is not UNSET:
            field_dict["plot_name"] = plot_name
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_care_occurrence_dto import GisCareOccurrenceDto # noqa: PLC0415
        d = dict(src_dict)
        _activation_id = d.pop("activation_id", UNSET)
        activation_id: UUID | Unset
        if isinstance(_activation_id,  Unset):
            activation_id = UNSET
        else:
            activation_id = UUID(_activation_id)




        def _parse_delivery(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


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


        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_plot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plot_id_type_0 = UUID(data)



                return plot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        plot_id = _parse_plot_id(d.pop("plot_id", UNSET))


        def _parse_plot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plot_name = _parse_plot_name(d.pop("plot_name", UNSET))


        def _parse_template_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_name = _parse_template_name(d.pop("template_name", UNSET))


        gis_care_week_plot_dto = cls(
            activation_id=activation_id,
            delivery=delivery,
            items=items,
            parcel_code=parcel_code,
            parcel_id=parcel_id,
            plot_id=plot_id,
            plot_name=plot_name,
            template_name=template_name,
        )

        return gis_care_week_plot_dto

