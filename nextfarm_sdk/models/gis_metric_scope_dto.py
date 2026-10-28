from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisMetricScopeDto")



@_attrs_define
class GisMetricScopeDto:
    

    branch_id: None | Unset | UUID = UNSET
    crop_type_id: None | Unset | UUID = UNSET
    parcel_ids: list[UUID] | None | Unset = UNSET
    zone_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        crop_type_id: None | str | Unset
        if isinstance(self.crop_type_id, Unset):
            crop_type_id = UNSET
        elif isinstance(self.crop_type_id, UUID):
            crop_type_id = str(self.crop_type_id)
        else:
            crop_type_id = self.crop_type_id

        parcel_ids: list[str] | None | Unset
        if isinstance(self.parcel_ids, Unset):
            parcel_ids = UNSET
        elif isinstance(self.parcel_ids, list):
            parcel_ids = []
            for parcel_ids_type_0_item_data in self.parcel_ids:
                parcel_ids_type_0_item = str(parcel_ids_type_0_item_data)
                parcel_ids.append(parcel_ids_type_0_item)


        else:
            parcel_ids = self.parcel_ids

        zone_id: None | str | Unset
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        elif isinstance(self.zone_id, UUID):
            zone_id = str(self.zone_id)
        else:
            zone_id = self.zone_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if parcel_ids is not UNSET:
            field_dict["parcel_ids"] = parcel_ids
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        def _parse_crop_type_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                crop_type_id_type_0 = UUID(data)



                return crop_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        crop_type_id = _parse_crop_type_id(d.pop("crop_type_id", UNSET))


        def _parse_parcel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parcel_ids_type_0 = []
                _parcel_ids_type_0 = data
                for parcel_ids_type_0_item_data in (_parcel_ids_type_0):
                    parcel_ids_type_0_item = UUID(parcel_ids_type_0_item_data)



                    parcel_ids_type_0.append(parcel_ids_type_0_item)

                return parcel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        parcel_ids = _parse_parcel_ids(d.pop("parcel_ids", UNSET))


        def _parse_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                zone_id_type_0 = UUID(data)



                return zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        zone_id = _parse_zone_id(d.pop("zone_id", UNSET))


        gis_metric_scope_dto = cls(
            branch_id=branch_id,
            crop_type_id=crop_type_id,
            parcel_ids=parcel_ids,
            zone_id=zone_id,
        )

        return gis_metric_scope_dto

