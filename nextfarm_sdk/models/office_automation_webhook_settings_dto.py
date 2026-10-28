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






T = TypeVar("T", bound="OfficeAutomationWebhookSettingsDto")



@_attrs_define
class OfficeAutomationWebhookSettingsDto:
    

    automation_id: UUID | Unset = UNSET
    bearer_enabled: bool | Unset = UNSET
    bearer_token: None | str | Unset = UNSET
    has_sample: bool | Unset = UNSET
    hook_token: None | str | Unset = UNSET
    ip_allowlist: list[str] | None | Unset = UNSET
    listen_until: datetime.datetime | None | Unset = UNSET
    listening: bool | Unset = UNSET
    sample_at: datetime.datetime | None | Unset = UNSET
    sample_source: None | str | Unset = UNSET
    url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        automation_id: str | Unset = UNSET
        if not isinstance(self.automation_id, Unset):
            automation_id = str(self.automation_id)

        bearer_enabled = self.bearer_enabled

        bearer_token: None | str | Unset
        if isinstance(self.bearer_token, Unset):
            bearer_token = UNSET
        else:
            bearer_token = self.bearer_token

        has_sample = self.has_sample

        hook_token: None | str | Unset
        if isinstance(self.hook_token, Unset):
            hook_token = UNSET
        else:
            hook_token = self.hook_token

        ip_allowlist: list[str] | None | Unset
        if isinstance(self.ip_allowlist, Unset):
            ip_allowlist = UNSET
        elif isinstance(self.ip_allowlist, list):
            ip_allowlist = self.ip_allowlist


        else:
            ip_allowlist = self.ip_allowlist

        listen_until: None | str | Unset
        if isinstance(self.listen_until, Unset):
            listen_until = UNSET
        elif isinstance(self.listen_until, datetime.datetime):
            listen_until = self.listen_until.isoformat()
        else:
            listen_until = self.listen_until

        listening = self.listening

        sample_at: None | str | Unset
        if isinstance(self.sample_at, Unset):
            sample_at = UNSET
        elif isinstance(self.sample_at, datetime.datetime):
            sample_at = self.sample_at.isoformat()
        else:
            sample_at = self.sample_at

        sample_source: None | str | Unset
        if isinstance(self.sample_source, Unset):
            sample_source = UNSET
        else:
            sample_source = self.sample_source

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if automation_id is not UNSET:
            field_dict["automationId"] = automation_id
        if bearer_enabled is not UNSET:
            field_dict["bearerEnabled"] = bearer_enabled
        if bearer_token is not UNSET:
            field_dict["bearerToken"] = bearer_token
        if has_sample is not UNSET:
            field_dict["hasSample"] = has_sample
        if hook_token is not UNSET:
            field_dict["hookToken"] = hook_token
        if ip_allowlist is not UNSET:
            field_dict["ipAllowlist"] = ip_allowlist
        if listen_until is not UNSET:
            field_dict["listenUntil"] = listen_until
        if listening is not UNSET:
            field_dict["listening"] = listening
        if sample_at is not UNSET:
            field_dict["sampleAt"] = sample_at
        if sample_source is not UNSET:
            field_dict["sampleSource"] = sample_source
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _automation_id = d.pop("automationId", UNSET)
        automation_id: UUID | Unset
        if isinstance(_automation_id,  Unset):
            automation_id = UNSET
        else:
            automation_id = UUID(_automation_id)




        bearer_enabled = d.pop("bearerEnabled", UNSET)

        def _parse_bearer_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bearer_token = _parse_bearer_token(d.pop("bearerToken", UNSET))


        has_sample = d.pop("hasSample", UNSET)

        def _parse_hook_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hook_token = _parse_hook_token(d.pop("hookToken", UNSET))


        def _parse_ip_allowlist(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_allowlist_type_0 = cast(list[str], data)

                return ip_allowlist_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ip_allowlist = _parse_ip_allowlist(d.pop("ipAllowlist", UNSET))


        def _parse_listen_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listen_until_type_0 = datetime.datetime.fromisoformat(data)



                return listen_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        listen_until = _parse_listen_until(d.pop("listenUntil", UNSET))


        listening = d.pop("listening", UNSET)

        def _parse_sample_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sample_at_type_0 = datetime.datetime.fromisoformat(data)



                return sample_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sample_at = _parse_sample_at(d.pop("sampleAt", UNSET))


        def _parse_sample_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_source = _parse_sample_source(d.pop("sampleSource", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        office_automation_webhook_settings_dto = cls(
            automation_id=automation_id,
            bearer_enabled=bearer_enabled,
            bearer_token=bearer_token,
            has_sample=has_sample,
            hook_token=hook_token,
            ip_allowlist=ip_allowlist,
            listen_until=listen_until,
            listening=listening,
            sample_at=sample_at,
            sample_source=sample_source,
            url=url,
        )

        return office_automation_webhook_settings_dto

