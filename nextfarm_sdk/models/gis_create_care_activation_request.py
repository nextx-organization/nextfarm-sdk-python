from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCreateCareActivationRequest")



@_attrs_define
class GisCreateCareActivationRequest:
    

    assignee_id: None | Unset | UUID = UNSET
    delivery: None | str | Unset = UNSET
    notify_user_ids: list[UUID] | None | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    season_id: None | Unset | UUID = UNSET
    template_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        else:
            delivery = self.delivery

        notify_user_ids: list[str] | None | Unset
        if isinstance(self.notify_user_ids, Unset):
            notify_user_ids = UNSET
        elif isinstance(self.notify_user_ids, list):
            notify_user_ids = []
            for notify_user_ids_type_0_item_data in self.notify_user_ids:
                notify_user_ids_type_0_item = str(notify_user_ids_type_0_item_data)
                notify_user_ids.append(notify_user_ids_type_0_item)


        else:
            notify_user_ids = self.notify_user_ids

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

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        template_id: str | Unset = UNSET
        if not isinstance(self.template_id, Unset):
            template_id = str(self.template_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if notify_user_ids is not UNSET:
            field_dict["notify_user_ids"] = notify_user_ids
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)



                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id", UNSET))


        def _parse_delivery(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        def _parse_notify_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_user_ids_type_0 = []
                _notify_user_ids_type_0 = data
                for notify_user_ids_type_0_item_data in (_notify_user_ids_type_0):
                    notify_user_ids_type_0_item = UUID(notify_user_ids_type_0_item_data)



                    notify_user_ids_type_0.append(notify_user_ids_type_0_item)

                return notify_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        notify_user_ids = _parse_notify_user_ids(d.pop("notify_user_ids", UNSET))


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


        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        _template_id = d.pop("template_id", UNSET)
        template_id: UUID | Unset
        if isinstance(_template_id,  Unset):
            template_id = UNSET
        else:
            template_id = UUID(_template_id)




        gis_create_care_activation_request = cls(
            assignee_id=assignee_id,
            delivery=delivery,
            notify_user_ids=notify_user_ids,
            parcel_id=parcel_id,
            plot_id=plot_id,
            season_id=season_id,
            template_id=template_id,
        )

        return gis_create_care_activation_request

