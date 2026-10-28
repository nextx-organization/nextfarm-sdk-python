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






T = TypeVar("T", bound="HarvestTraceBundleListItemDto")



@_attrs_define
class HarvestTraceBundleListItemDto:
    

    anchor_date: datetime.date | None | Unset = UNSET
    anchor_is_backfill: bool | Unset = UNSET
    anchor_status: None | str | Unset = UNSET
    bundle_version: int | Unset = UNSET
    certification: None | str | Unset = UNSET
    content_hash: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    farmer: None | str | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    harvest_record_id: UUID | Unset = UNSET
    has_open_incident: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_locked: bool | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    season_id: None | Unset | UUID = UNSET
    stage_count: int | Unset = UNSET
    zone_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        anchor_date: None | str | Unset
        if isinstance(self.anchor_date, Unset):
            anchor_date = UNSET
        elif isinstance(self.anchor_date, datetime.date):
            anchor_date = self.anchor_date.isoformat()
        else:
            anchor_date = self.anchor_date

        anchor_is_backfill = self.anchor_is_backfill

        anchor_status: None | str | Unset
        if isinstance(self.anchor_status, Unset):
            anchor_status = UNSET
        else:
            anchor_status = self.anchor_status

        bundle_version = self.bundle_version

        certification: None | str | Unset
        if isinstance(self.certification, Unset):
            certification = UNSET
        else:
            certification = self.certification

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        farmer: None | str | Unset
        if isinstance(self.farmer, Unset):
            farmer = UNSET
        else:
            farmer = self.farmer

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        harvest_record_id: str | Unset = UNSET
        if not isinstance(self.harvest_record_id, Unset):
            harvest_record_id = str(self.harvest_record_id)

        has_open_incident = self.has_open_incident

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_locked = self.is_locked

        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        season_id: None | str | Unset
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        stage_count = self.stage_count

        zone_name: None | str | Unset
        if isinstance(self.zone_name, Unset):
            zone_name = UNSET
        else:
            zone_name = self.zone_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_date is not UNSET:
            field_dict["anchor_date"] = anchor_date
        if anchor_is_backfill is not UNSET:
            field_dict["anchor_is_backfill"] = anchor_is_backfill
        if anchor_status is not UNSET:
            field_dict["anchor_status"] = anchor_status
        if bundle_version is not UNSET:
            field_dict["bundle_version"] = bundle_version
        if certification is not UNSET:
            field_dict["certification"] = certification
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if farmer is not UNSET:
            field_dict["farmer"] = farmer
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if harvest_record_id is not UNSET:
            field_dict["harvest_record_id"] = harvest_record_id
        if has_open_incident is not UNSET:
            field_dict["has_open_incident"] = has_open_incident
        if id is not UNSET:
            field_dict["id"] = id
        if is_locked is not UNSET:
            field_dict["is_locked"] = is_locked
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if product is not UNSET:
            field_dict["product"] = product
        if season_id is not UNSET:
            field_dict["season_id"] = season_id
        if stage_count is not UNSET:
            field_dict["stage_count"] = stage_count
        if zone_name is not UNSET:
            field_dict["zone_name"] = zone_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_anchor_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                anchor_date_type_0 = datetime.date.fromisoformat(data)



                return anchor_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        anchor_date = _parse_anchor_date(d.pop("anchor_date", UNSET))


        anchor_is_backfill = d.pop("anchor_is_backfill", UNSET)

        def _parse_anchor_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor_status = _parse_anchor_status(d.pop("anchor_status", UNSET))


        bundle_version = d.pop("bundle_version", UNSET)

        def _parse_certification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certification = _parse_certification(d.pop("certification", UNSET))


        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_farmer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farmer = _parse_farmer(d.pop("farmer", UNSET))


        _harvest_date = d.pop("harvest_date", UNSET)
        harvest_date: datetime.date | Unset
        if isinstance(_harvest_date,  Unset):
            harvest_date = UNSET
        else:
            harvest_date = datetime.date.fromisoformat(_harvest_date)




        _harvest_record_id = d.pop("harvest_record_id", UNSET)
        harvest_record_id: UUID | Unset
        if isinstance(_harvest_record_id,  Unset):
            harvest_record_id = UNSET
        else:
            harvest_record_id = UUID(_harvest_record_id)




        has_open_incident = d.pop("has_open_incident", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_locked = d.pop("is_locked", UNSET)

        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))


        def _parse_season_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)



                return season_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        season_id = _parse_season_id(d.pop("season_id", UNSET))


        stage_count = d.pop("stage_count", UNSET)

        def _parse_zone_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_name = _parse_zone_name(d.pop("zone_name", UNSET))


        harvest_trace_bundle_list_item_dto = cls(
            anchor_date=anchor_date,
            anchor_is_backfill=anchor_is_backfill,
            anchor_status=anchor_status,
            bundle_version=bundle_version,
            certification=certification,
            content_hash=content_hash,
            created_at=created_at,
            farmer=farmer,
            harvest_date=harvest_date,
            harvest_record_id=harvest_record_id,
            has_open_incident=has_open_incident,
            id=id,
            is_locked=is_locked,
            parcel_code=parcel_code,
            product=product,
            season_id=season_id,
            stage_count=stage_count,
            zone_name=zone_name,
        )

        return harvest_trace_bundle_list_item_dto

