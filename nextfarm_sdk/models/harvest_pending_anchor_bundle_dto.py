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






T = TypeVar("T", bound="HarvestPendingAnchorBundleDto")



@_attrs_define
class HarvestPendingAnchorBundleDto:
    

    bundle_id: UUID | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    sealed_at: datetime.datetime | Unset = UNSET
    version: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bundle_id: str | Unset = UNSET
        if not isinstance(self.bundle_id, Unset):
            bundle_id = str(self.bundle_id)

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

        sealed_at: str | Unset = UNSET
        if not isinstance(self.sealed_at, Unset):
            sealed_at = self.sealed_at.isoformat()

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bundle_id is not UNSET:
            field_dict["bundle_id"] = bundle_id
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if product is not UNSET:
            field_dict["product"] = product
        if sealed_at is not UNSET:
            field_dict["sealed_at"] = sealed_at
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


        _sealed_at = d.pop("sealed_at", UNSET)
        sealed_at: datetime.datetime | Unset
        if isinstance(_sealed_at,  Unset):
            sealed_at = UNSET
        else:
            sealed_at = datetime.datetime.fromisoformat(_sealed_at)




        version = d.pop("version", UNSET)

        harvest_pending_anchor_bundle_dto = cls(
            bundle_id=bundle_id,
            parcel_code=parcel_code,
            product=product,
            sealed_at=sealed_at,
            version=version,
        )

        return harvest_pending_anchor_bundle_dto

