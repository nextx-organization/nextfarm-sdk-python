from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeAutomationsControllerUpdateWebhookRequest")



@_attrs_define
class OfficeAutomationsControllerUpdateWebhookRequest:
    

    bearer_enabled: bool | None | Unset = UNSET
    ip_allowlist: list[str] | None | Unset = UNSET
    regenerate_bearer: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bearer_enabled: bool | None | Unset
        if isinstance(self.bearer_enabled, Unset):
            bearer_enabled = UNSET
        else:
            bearer_enabled = self.bearer_enabled

        ip_allowlist: list[str] | None | Unset
        if isinstance(self.ip_allowlist, Unset):
            ip_allowlist = UNSET
        elif isinstance(self.ip_allowlist, list):
            ip_allowlist = self.ip_allowlist


        else:
            ip_allowlist = self.ip_allowlist

        regenerate_bearer = self.regenerate_bearer


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bearer_enabled is not UNSET:
            field_dict["bearerEnabled"] = bearer_enabled
        if ip_allowlist is not UNSET:
            field_dict["ipAllowlist"] = ip_allowlist
        if regenerate_bearer is not UNSET:
            field_dict["regenerateBearer"] = regenerate_bearer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_bearer_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        bearer_enabled = _parse_bearer_enabled(d.pop("bearerEnabled", UNSET))


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


        regenerate_bearer = d.pop("regenerateBearer", UNSET)

        office_automations_controller_update_webhook_request = cls(
            bearer_enabled=bearer_enabled,
            ip_allowlist=ip_allowlist,
            regenerate_bearer=regenerate_bearer,
        )

        return office_automations_controller_update_webhook_request

