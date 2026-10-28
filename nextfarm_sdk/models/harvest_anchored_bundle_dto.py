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






T = TypeVar("T", bound="HarvestAnchoredBundleDto")



@_attrs_define
class HarvestAnchoredBundleDto:
    

    bundle_id: UUID | Unset = UNSET
    content_hash: None | str | Unset = UNSET
    harvest_date: datetime.date | Unset = UNSET
    harvest_record_id: UUID | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    version: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bundle_id: str | Unset = UNSET
        if not isinstance(self.bundle_id, Unset):
            bundle_id = str(self.bundle_id)

        content_hash: None | str | Unset
        if isinstance(self.content_hash, Unset):
            content_hash = UNSET
        else:
            content_hash = self.content_hash

        harvest_date: str | Unset = UNSET
        if not isinstance(self.harvest_date, Unset):
            harvest_date = self.harvest_date.isoformat()

        harvest_record_id: str | Unset = UNSET
        if not isinstance(self.harvest_record_id, Unset):
            harvest_record_id = str(self.harvest_record_id)

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

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bundle_id is not UNSET:
            field_dict["bundle_id"] = bundle_id
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if harvest_date is not UNSET:
            field_dict["harvest_date"] = harvest_date
        if harvest_record_id is not UNSET:
            field_dict["harvest_record_id"] = harvest_record_id
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if product is not UNSET:
            field_dict["product"] = product
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _bundle_id = d.pop("bundle_id", UNSET)
        bundle_id: UUID | Unset
        if isinstance(_bundle_id,  Unset):
            bundle_id = UNSET
        else:
            bundle_id = UUID(_bundle_id)




        def _parse_content_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_hash = _parse_content_hash(d.pop("content_hash", UNSET))


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


        version = d.pop("version", UNSET)

        harvest_anchored_bundle_dto = cls(
            bundle_id=bundle_id,
            content_hash=content_hash,
            harvest_date=harvest_date,
            harvest_record_id=harvest_record_id,
            parcel_code=parcel_code,
            product=product,
            version=version,
        )

        return harvest_anchored_bundle_dto

