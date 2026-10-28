from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeChatStorageUsageDto")



@_attrs_define
class OfficeChatStorageUsageDto:
    

    attachment_bytes: int | Unset = UNSET
    extra_storage_gb: int | Unset = UNSET
    file_bytes: int | Unset = UNSET
    is_exhausted: bool | Unset = UNSET
    is_measured: bool | Unset = UNSET
    is_near_limit: bool | Unset = UNSET
    limit_bytes: int | Unset = UNSET
    mail_bytes: int | None | Unset = UNSET
    measured_at: datetime.datetime | Unset = UNSET
    paid_seats: int | Unset = UNSET
    record_bytes: int | Unset = UNSET
    recording_bytes: int | Unset = UNSET
    trash_bytes: int | Unset = UNSET
    used_bytes: int | None | Unset = UNSET
    used_percent: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attachment_bytes = self.attachment_bytes

        extra_storage_gb = self.extra_storage_gb

        file_bytes = self.file_bytes

        is_exhausted = self.is_exhausted

        is_measured = self.is_measured

        is_near_limit = self.is_near_limit

        limit_bytes = self.limit_bytes

        mail_bytes: int | None | Unset
        if isinstance(self.mail_bytes, Unset):
            mail_bytes = UNSET
        else:
            mail_bytes = self.mail_bytes

        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        paid_seats = self.paid_seats

        record_bytes = self.record_bytes

        recording_bytes = self.recording_bytes

        trash_bytes = self.trash_bytes

        used_bytes: int | None | Unset
        if isinstance(self.used_bytes, Unset):
            used_bytes = UNSET
        else:
            used_bytes = self.used_bytes

        used_percent: int | None | Unset
        if isinstance(self.used_percent, Unset):
            used_percent = UNSET
        else:
            used_percent = self.used_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachment_bytes is not UNSET:
            field_dict["attachmentBytes"] = attachment_bytes
        if extra_storage_gb is not UNSET:
            field_dict["extraStorageGb"] = extra_storage_gb
        if file_bytes is not UNSET:
            field_dict["fileBytes"] = file_bytes
        if is_exhausted is not UNSET:
            field_dict["isExhausted"] = is_exhausted
        if is_measured is not UNSET:
            field_dict["isMeasured"] = is_measured
        if is_near_limit is not UNSET:
            field_dict["isNearLimit"] = is_near_limit
        if limit_bytes is not UNSET:
            field_dict["limitBytes"] = limit_bytes
        if mail_bytes is not UNSET:
            field_dict["mailBytes"] = mail_bytes
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if paid_seats is not UNSET:
            field_dict["paidSeats"] = paid_seats
        if record_bytes is not UNSET:
            field_dict["recordBytes"] = record_bytes
        if recording_bytes is not UNSET:
            field_dict["recordingBytes"] = recording_bytes
        if trash_bytes is not UNSET:
            field_dict["trashBytes"] = trash_bytes
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes
        if used_percent is not UNSET:
            field_dict["usedPercent"] = used_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_bytes = d.pop("attachmentBytes", UNSET)

        extra_storage_gb = d.pop("extraStorageGb", UNSET)

        file_bytes = d.pop("fileBytes", UNSET)

        is_exhausted = d.pop("isExhausted", UNSET)

        is_measured = d.pop("isMeasured", UNSET)

        is_near_limit = d.pop("isNearLimit", UNSET)

        limit_bytes = d.pop("limitBytes", UNSET)

        def _parse_mail_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mail_bytes = _parse_mail_bytes(d.pop("mailBytes", UNSET))


        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at,  Unset):
            measured_at = UNSET
        else:
            measured_at = datetime.datetime.fromisoformat(_measured_at)




        paid_seats = d.pop("paidSeats", UNSET)

        record_bytes = d.pop("recordBytes", UNSET)

        recording_bytes = d.pop("recordingBytes", UNSET)

        trash_bytes = d.pop("trashBytes", UNSET)

        def _parse_used_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_bytes = _parse_used_bytes(d.pop("usedBytes", UNSET))


        def _parse_used_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_percent = _parse_used_percent(d.pop("usedPercent", UNSET))


        office_chat_storage_usage_dto = cls(
            attachment_bytes=attachment_bytes,
            extra_storage_gb=extra_storage_gb,
            file_bytes=file_bytes,
            is_exhausted=is_exhausted,
            is_measured=is_measured,
            is_near_limit=is_near_limit,
            limit_bytes=limit_bytes,
            mail_bytes=mail_bytes,
            measured_at=measured_at,
            paid_seats=paid_seats,
            record_bytes=record_bytes,
            recording_bytes=recording_bytes,
            trash_bytes=trash_bytes,
            used_bytes=used_bytes,
            used_percent=used_percent,
        )

        return office_chat_storage_usage_dto

