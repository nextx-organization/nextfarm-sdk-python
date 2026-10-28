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






T = TypeVar("T", bound="GisCareActivationDto")



@_attrs_define
class GisCareActivationDto:
    

    assignee_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | Unset = UNSET
    delivery: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    enabled_at: datetime.datetime | None | Unset = UNSET
    id: UUID | Unset = UNSET
    notify_user_ids: list[UUID] | None | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    plot_name: None | str | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    template_id: UUID | Unset = UNSET
    template_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        else:
            delivery = self.delivery

        enabled = self.enabled

        enabled_at: None | str | Unset
        if isinstance(self.enabled_at, Unset):
            enabled_at = UNSET
        elif isinstance(self.enabled_at, datetime.datetime):
            enabled_at = self.enabled_at.isoformat()
        else:
            enabled_at = self.enabled_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        template_name: None | str | Unset
        if isinstance(self.template_name, Unset):
            template_name = UNSET
        else:
            template_name = self.template_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_at is not UNSET:
            field_dict["enabled_at"] = enabled_at
        if id is not UNSET:
            field_dict["id"] = id
        if notify_user_ids is not UNSET:
            field_dict["notify_user_ids"] = notify_user_ids
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if plot_name is not UNSET:
            field_dict["plot_name"] = plot_name
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

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


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_delivery(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        enabled = d.pop("enabled", UNSET)

        def _parse_enabled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enabled_at_type_0 = datetime.datetime.fromisoformat(data)



                return enabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        enabled_at = _parse_enabled_at(d.pop("enabled_at", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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




        def _parse_template_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_name = _parse_template_name(d.pop("template_name", UNSET))


        gis_care_activation_dto = cls(
            assignee_id=assignee_id,
            created_at=created_at,
            delivery=delivery,
            enabled=enabled,
            enabled_at=enabled_at,
            id=id,
            notify_user_ids=notify_user_ids,
            parcel_code=parcel_code,
            parcel_id=parcel_id,
            plot_id=plot_id,
            plot_name=plot_name,
            season_id=season_id,
            template_id=template_id,
            template_name=template_name,
        )

        return gis_care_activation_dto

