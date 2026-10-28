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






T = TypeVar("T", bound="HarvestQrCodeDto")



@_attrs_define
class HarvestQrCodeDto:
    

    code: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    effective_to: datetime.date | Unset = UNSET
    first_scanned_at: datetime.datetime | None | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    harvest_record_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    last_scanned_at: datetime.datetime | None | Unset = UNSET
    scan_count: int | Unset = UNSET
    season_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        effective_to: str | Unset = UNSET
        if not isinstance(self.effective_to, Unset):
            effective_to = self.effective_to.isoformat()

        first_scanned_at: None | str | Unset
        if isinstance(self.first_scanned_at, Unset):
            first_scanned_at = UNSET
        elif isinstance(self.first_scanned_at, datetime.datetime):
            first_scanned_at = self.first_scanned_at.isoformat()
        else:
            first_scanned_at = self.first_scanned_at

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        harvest_record_id: None | str | Unset
        if isinstance(self.harvest_record_id, Unset):
            harvest_record_id = UNSET
        elif isinstance(self.harvest_record_id, UUID):
            harvest_record_id = str(self.harvest_record_id)
        else:
            harvest_record_id = self.harvest_record_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_scanned_at: None | str | Unset
        if isinstance(self.last_scanned_at, Unset):
            last_scanned_at = UNSET
        elif isinstance(self.last_scanned_at, datetime.datetime):
            last_scanned_at = self.last_scanned_at.isoformat()
        else:
            last_scanned_at = self.last_scanned_at

        scan_count = self.scan_count

        season_id: str | Unset = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if effective_to is not UNSET:
            field_dict["effective_to"] = effective_to
        if first_scanned_at is not UNSET:
            field_dict["first_scanned_at"] = first_scanned_at
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if harvest_record_id is not UNSET:
            field_dict["harvest_record_id"] = harvest_record_id
        if id is not UNSET:
            field_dict["id"] = id
        if last_scanned_at is not UNSET:
            field_dict["last_scanned_at"] = last_scanned_at
        if scan_count is not UNSET:
            field_dict["scan_count"] = scan_count
        if season_id is not UNSET:
            field_dict["season_id"] = season_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _effective_to = d.pop("effective_to", UNSET)
        effective_to: datetime.date | Unset
        if isinstance(_effective_to,  Unset):
            effective_to = UNSET
        else:
            effective_to = datetime.date.fromisoformat(_effective_to)




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


        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: datetime.date | Unset
        if isinstance(_harvest_date,  Unset):
            harvest_date = UNSET
        else:
            harvest_date = datetime.date.fromisoformat(_harvest_date)




        def _parse_harvest_record_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                harvest_record_id_type_0 = UUID(data)



                return harvest_record_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        harvest_record_id = _parse_harvest_record_id(d.pop("harvest_record_id", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        scan_count = d.pop("scan_count", UNSET)

        _season_id = d.pop("season_id", UNSET)
        season_id: UUID | Unset
        if isinstance(_season_id,  Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)




        harvest_qr_code_dto = cls(
            code=code,
            created_at=created_at,
            effective_to=effective_to,
            first_scanned_at=first_scanned_at,
            harvest_date=harvest_date,
            harvest_record_id=harvest_record_id,
            id=id,
            last_scanned_at=last_scanned_at,
            scan_count=scan_count,
            season_id=season_id,
        )

        return harvest_qr_code_dto

