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
  from ..models.harvest_qr_scan_day_dto import HarvestQrScanDayDto





T = TypeVar("T", bound="HarvestQrScanSeriesDto")



@_attrs_define
class HarvestQrScanSeriesDto:
    

    code: None | str | Unset = UNSET
    days: list[HarvestQrScanDayDto] | None | Unset = UNSET
    first_scanned_at: datetime.datetime | None | Unset = UNSET
    last_scanned_at: datetime.datetime | None | Unset = UNSET
    qr_code_id: UUID | Unset = UNSET
    scan_count: int | Unset = UNSET
    warn_threshold: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_qr_scan_day_dto import HarvestQrScanDayDto # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        days: list[dict[str, Any]] | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = []
            for days_type_0_item_data in self.days:
                days_type_0_item = days_type_0_item_data.to_dict()
                days.append(days_type_0_item)


        else:
            days = self.days

        first_scanned_at: None | str | Unset
        if isinstance(self.first_scanned_at, Unset):
            first_scanned_at = UNSET
        elif isinstance(self.first_scanned_at, datetime.datetime):
            first_scanned_at = self.first_scanned_at.isoformat()
        else:
            first_scanned_at = self.first_scanned_at

        last_scanned_at: None | str | Unset
        if isinstance(self.last_scanned_at, Unset):
            last_scanned_at = UNSET
        elif isinstance(self.last_scanned_at, datetime.datetime):
            last_scanned_at = self.last_scanned_at.isoformat()
        else:
            last_scanned_at = self.last_scanned_at

        qr_code_id: str | Unset = UNSET
        if not isinstance(self.qr_code_id, Unset):
            qr_code_id = str(self.qr_code_id)

        scan_count = self.scan_count

        warn_threshold = self.warn_threshold


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if days is not UNSET:
            field_dict["days"] = days
        if first_scanned_at is not UNSET:
            field_dict["first_scanned_at"] = first_scanned_at
        if last_scanned_at is not UNSET:
            field_dict["last_scanned_at"] = last_scanned_at
        if qr_code_id is not UNSET:
            field_dict["qr_code_id"] = qr_code_id
        if scan_count is not UNSET:
            field_dict["scan_count"] = scan_count
        if warn_threshold is not UNSET:
            field_dict["warn_threshold"] = warn_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_qr_scan_day_dto import HarvestQrScanDayDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_days(data: object) -> list[HarvestQrScanDayDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = []
                _days_type_0 = data
                for days_type_0_item_data in (_days_type_0):
                    days_type_0_item = HarvestQrScanDayDto.from_dict(days_type_0_item_data)



                    days_type_0.append(days_type_0_item)

                return days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestQrScanDayDto] | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))


        def _parse_first_scanned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_scanned_at_type_0 = datetime.datetime.fromisoformat(data)



                return first_scanned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_scanned_at = _parse_first_scanned_at(d.pop("first_scanned_at", UNSET))


        def _parse_last_scanned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_scanned_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_scanned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_scanned_at = _parse_last_scanned_at(d.pop("last_scanned_at", UNSET))


        _qr_code_id = d.pop("qr_code_id", UNSET)
        qr_code_id: UUID | Unset
        if isinstance(_qr_code_id,  Unset):
            qr_code_id = UNSET
        else:
            qr_code_id = UUID(_qr_code_id)




        scan_count = d.pop("scan_count", UNSET)

        warn_threshold = d.pop("warn_threshold", UNSET)

        harvest_qr_scan_series_dto = cls(
            code=code,
            days=days,
            first_scanned_at=first_scanned_at,
            last_scanned_at=last_scanned_at,
            qr_code_id=qr_code_id,
            scan_count=scan_count,
            warn_threshold=warn_threshold,
        )

        return harvest_qr_scan_series_dto

