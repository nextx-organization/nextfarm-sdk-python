from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="IotEmergencyStopRequest")



@_attrs_define
class IotEmergencyStopRequest:
    

    parcel_id: None | Unset | UUID = UNSET
    reason: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        iot_emergency_stop_request = cls(
            parcel_id=parcel_id,
            reason=reason,
            scope=scope,
        )

        return iot_emergency_stop_request

