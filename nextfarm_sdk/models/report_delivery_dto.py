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






T = TypeVar("T", bound="ReportDeliveryDto")



@_attrs_define
class ReportDeliveryDto:
    

    at: datetime.datetime | Unset = UNSET
    channels: list[str] | None | Unset = UNSET
    id: UUID | Unset = UNSET
    period_from: datetime.date | Unset = UNSET
    period_to: datetime.date | Unset = UNSET
    reason: None | str | Unset = UNSET
    recipient_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        channels: list[str] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = self.channels


        else:
            channels = self.channels

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        period_from: str | Unset = UNSET
        if not isinstance(self.period_from, Unset):
            period_from = self.period_from.isoformat()

        period_to: str | Unset = UNSET
        if not isinstance(self.period_to, Unset):
            period_to = self.period_to.isoformat()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        recipient_id: str | Unset = UNSET
        if not isinstance(self.recipient_id, Unset):
            recipient_id = str(self.recipient_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if at is not UNSET:
            field_dict["at"] = at
        if channels is not UNSET:
            field_dict["channels"] = channels
        if id is not UNSET:
            field_dict["id"] = id
        if period_from is not UNSET:
            field_dict["periodFrom"] = period_from
        if period_to is not UNSET:
            field_dict["periodTo"] = period_to
        if reason is not UNSET:
            field_dict["reason"] = reason
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)




        def _parse_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = cast(list[str], data)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _period_from = d.pop("periodFrom", UNSET)
        period_from: datetime.date | Unset
        if isinstance(_period_from,  Unset):
            period_from = UNSET
        else:
            period_from = datetime.date.fromisoformat(_period_from)




        _period_to = d.pop("periodTo", UNSET)
        period_to: datetime.date | Unset
        if isinstance(_period_to,  Unset):
            period_to = UNSET
        else:
            period_to = datetime.date.fromisoformat(_period_to)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        _recipient_id = d.pop("recipientId", UNSET)
        recipient_id: UUID | Unset
        if isinstance(_recipient_id,  Unset):
            recipient_id = UNSET
        else:
            recipient_id = UUID(_recipient_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        report_delivery_dto = cls(
            at=at,
            channels=channels,
            id=id,
            period_from=period_from,
            period_to=period_to,
            reason=reason,
            recipient_id=recipient_id,
            status=status,
        )

        return report_delivery_dto

