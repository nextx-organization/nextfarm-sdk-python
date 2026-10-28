from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeCalendarLinkStatusDto")



@_attrs_define
class OfficeCalendarLinkStatusDto:
    

    account_email: None | str | Unset = UNSET
    calendar_id: None | str | Unset = UNSET
    connected: bool | Unset = UNSET
    last_error_key: None | str | Unset = UNSET
    last_synced_at: datetime.datetime | None | Unset = UNSET
    provider: None | str | Unset = UNSET
    provider_configured: bool | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_email: None | str | Unset
        if isinstance(self.account_email, Unset):
            account_email = UNSET
        else:
            account_email = self.account_email

        calendar_id: None | str | Unset
        if isinstance(self.calendar_id, Unset):
            calendar_id = UNSET
        else:
            calendar_id = self.calendar_id

        connected = self.connected

        last_error_key: None | str | Unset
        if isinstance(self.last_error_key, Unset):
            last_error_key = UNSET
        else:
            last_error_key = self.last_error_key

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        provider_configured = self.provider_configured

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_email is not UNSET:
            field_dict["accountEmail"] = account_email
        if calendar_id is not UNSET:
            field_dict["calendarId"] = calendar_id
        if connected is not UNSET:
            field_dict["connected"] = connected
        if last_error_key is not UNSET:
            field_dict["lastErrorKey"] = last_error_key
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_configured is not UNSET:
            field_dict["providerConfigured"] = provider_configured
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_email = _parse_account_email(d.pop("accountEmail", UNSET))


        def _parse_calendar_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calendar_id = _parse_calendar_id(d.pop("calendarId", UNSET))


        connected = d.pop("connected", UNSET)

        def _parse_last_error_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error_key = _parse_last_error_key(d.pop("lastErrorKey", UNSET))


        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt", UNSET))


        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        provider_configured = d.pop("providerConfigured", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_calendar_link_status_dto = cls(
            account_email=account_email,
            calendar_id=calendar_id,
            connected=connected,
            last_error_key=last_error_key,
            last_synced_at=last_synced_at,
            provider=provider,
            provider_configured=provider_configured,
            status=status,
        )

        return office_calendar_link_status_dto

