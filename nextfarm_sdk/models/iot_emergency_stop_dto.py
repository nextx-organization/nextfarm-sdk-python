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

if TYPE_CHECKING:
  from ..models.iot_emergency_channel_result_dto import IotEmergencyChannelResultDto





T = TypeVar("T", bound="IotEmergencyStopDto")



@_attrs_define
class IotEmergencyStopDto:
    

    active: bool | Unset = UNSET
    already_active: bool | Unset = UNSET
    device_ids: list[UUID] | None | Unset = UNSET
    failed_count: int | Unset = UNSET
    id: UUID | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    reason: None | str | Unset = UNSET
    release_note: None | str | Unset = UNSET
    released_at: datetime.datetime | None | Unset = UNSET
    released_by: None | Unset | UUID = UNSET
    repeat_count: int | Unset = UNSET
    results: list[IotEmergencyChannelResultDto] | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    stopped_schedules: int | Unset = UNSET
    triggered_at: datetime.datetime | Unset = UNSET
    triggered_by: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_emergency_channel_result_dto import IotEmergencyChannelResultDto # noqa: PLC0415
        active = self.active

        already_active = self.already_active

        device_ids: list[str] | None | Unset
        if isinstance(self.device_ids, Unset):
            device_ids = UNSET
        elif isinstance(self.device_ids, list):
            device_ids = []
            for device_ids_type_0_item_data in self.device_ids:
                device_ids_type_0_item = str(device_ids_type_0_item_data)
                device_ids.append(device_ids_type_0_item)


        else:
            device_ids = self.device_ids

        failed_count = self.failed_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        release_note: None | str | Unset
        if isinstance(self.release_note, Unset):
            release_note = UNSET
        else:
            release_note = self.release_note

        released_at: None | str | Unset
        if isinstance(self.released_at, Unset):
            released_at = UNSET
        elif isinstance(self.released_at, datetime.datetime):
            released_at = self.released_at.isoformat()
        else:
            released_at = self.released_at

        released_by: None | str | Unset
        if isinstance(self.released_by, Unset):
            released_by = UNSET
        elif isinstance(self.released_by, UUID):
            released_by = str(self.released_by)
        else:
            released_by = self.released_by

        repeat_count = self.repeat_count

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)


        else:
            results = self.results

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        stopped_schedules = self.stopped_schedules

        triggered_at: str | Unset = UNSET
        if not isinstance(self.triggered_at, Unset):
            triggered_at = self.triggered_at.isoformat()

        triggered_by: str | Unset = UNSET
        if not isinstance(self.triggered_by, Unset):
            triggered_by = str(self.triggered_by)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if already_active is not UNSET:
            field_dict["already_active"] = already_active
        if device_ids is not UNSET:
            field_dict["device_ids"] = device_ids
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if id is not UNSET:
            field_dict["id"] = id
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if release_note is not UNSET:
            field_dict["release_note"] = release_note
        if released_at is not UNSET:
            field_dict["released_at"] = released_at
        if released_by is not UNSET:
            field_dict["released_by"] = released_by
        if repeat_count is not UNSET:
            field_dict["repeat_count"] = repeat_count
        if results is not UNSET:
            field_dict["results"] = results
        if scope is not UNSET:
            field_dict["scope"] = scope
        if stopped_schedules is not UNSET:
            field_dict["stopped_schedules"] = stopped_schedules
        if triggered_at is not UNSET:
            field_dict["triggered_at"] = triggered_at
        if triggered_by is not UNSET:
            field_dict["triggered_by"] = triggered_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_emergency_channel_result_dto import IotEmergencyChannelResultDto # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        already_active = d.pop("already_active", UNSET)

        def _parse_device_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                device_ids_type_0 = []
                _device_ids_type_0 = data
                for device_ids_type_0_item_data in (_device_ids_type_0):
                    device_ids_type_0_item = UUID(device_ids_type_0_item_data)



                    device_ids_type_0.append(device_ids_type_0_item)

                return device_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        device_ids = _parse_device_ids(d.pop("device_ids", UNSET))


        failed_count = d.pop("failed_count", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parcel_id_type_0 = UUID(data)



                return parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parcel_id = _parse_parcel_id(d.pop("parcel_id", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_release_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        release_note = _parse_release_note(d.pop("release_note", UNSET))


        def _parse_released_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_at_type_0 = datetime.datetime.fromisoformat(data)



                return released_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        released_at = _parse_released_at(d.pop("released_at", UNSET))


        def _parse_released_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_by_type_0 = UUID(data)



                return released_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        released_by = _parse_released_by(d.pop("released_by", UNSET))


        repeat_count = d.pop("repeat_count", UNSET)

        def _parse_results(data: object) -> list[IotEmergencyChannelResultDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in (_results_type_0):
                    results_type_0_item = IotEmergencyChannelResultDto.from_dict(results_type_0_item_data)



                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotEmergencyChannelResultDto] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        stopped_schedules = d.pop("stopped_schedules", UNSET)

        _triggered_at = d.pop("triggered_at", UNSET)
        triggered_at: datetime.datetime | Unset
        if isinstance(_triggered_at,  Unset):
            triggered_at = UNSET
        else:
            triggered_at = datetime.datetime.fromisoformat(_triggered_at)




        _triggered_by = d.pop("triggered_by", UNSET)
        triggered_by: UUID | Unset
        if isinstance(_triggered_by,  Unset):
            triggered_by = UNSET
        else:
            triggered_by = UUID(_triggered_by)




        iot_emergency_stop_dto = cls(
            active=active,
            already_active=already_active,
            device_ids=device_ids,
            failed_count=failed_count,
            id=id,
            parcel_id=parcel_id,
            reason=reason,
            release_note=release_note,
            released_at=released_at,
            released_by=released_by,
            repeat_count=repeat_count,
            results=results,
            scope=scope,
            stopped_schedules=stopped_schedules,
            triggered_at=triggered_at,
            triggered_by=triggered_by,
        )

        return iot_emergency_stop_dto

