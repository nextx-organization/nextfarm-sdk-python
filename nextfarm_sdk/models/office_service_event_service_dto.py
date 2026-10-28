from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_service_event_dto import OfficeServiceEventDto





T = TypeVar("T", bound="OfficeServiceEventServiceDto")



@_attrs_define
class OfficeServiceEventServiceDto:
    

    events: list[OfficeServiceEventDto] | None | Unset = UNSET
    label: None | str | Unset = UNSET
    service: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_service_event_dto import OfficeServiceEventDto # noqa: PLC0415
        events: list[dict[str, Any]] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = []
            for events_type_0_item_data in self.events:
                events_type_0_item = events_type_0_item_data.to_dict()
                events.append(events_type_0_item)


        else:
            events = self.events

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if events is not UNSET:
            field_dict["events"] = events
        if label is not UNSET:
            field_dict["label"] = label
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_service_event_dto import OfficeServiceEventDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_events(data: object) -> list[OfficeServiceEventDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = []
                _events_type_0 = data
                for events_type_0_item_data in (_events_type_0):
                    events_type_0_item = OfficeServiceEventDto.from_dict(events_type_0_item_data)



                    events_type_0.append(events_type_0_item)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeServiceEventDto] | None | Unset, data)

        events = _parse_events(d.pop("events", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))


        office_service_event_service_dto = cls(
            events=events,
            label=label,
            service=service,
        )

        return office_service_event_service_dto

