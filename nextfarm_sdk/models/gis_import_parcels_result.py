from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.gis_import_parcel_error import GisImportParcelError





T = TypeVar("T", bound="GisImportParcelsResult")



@_attrs_define
class GisImportParcelsResult:
    

    created_parcel_ids: list[UUID] | None | Unset = UNSET
    created_zone_count: int | Unset = UNSET
    errors: list[GisImportParcelError] | None | Unset = UNSET
    failed_count: int | Unset = UNSET
    skipped_count: int | Unset = UNSET
    success_count: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_import_parcel_error import GisImportParcelError # noqa: PLC0415
        created_parcel_ids: list[str] | None | Unset
        if isinstance(self.created_parcel_ids, Unset):
            created_parcel_ids = UNSET
        elif isinstance(self.created_parcel_ids, list):
            created_parcel_ids = []
            for created_parcel_ids_type_0_item_data in self.created_parcel_ids:
                created_parcel_ids_type_0_item = str(created_parcel_ids_type_0_item_data)
                created_parcel_ids.append(created_parcel_ids_type_0_item)


        else:
            created_parcel_ids = self.created_parcel_ids

        created_zone_count = self.created_zone_count

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)


        else:
            errors = self.errors

        failed_count = self.failed_count

        skipped_count = self.skipped_count

        success_count = self.success_count

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_parcel_ids is not UNSET:
            field_dict["created_parcel_ids"] = created_parcel_ids
        if created_zone_count is not UNSET:
            field_dict["created_zone_count"] = created_zone_count
        if errors is not UNSET:
            field_dict["errors"] = errors
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if skipped_count is not UNSET:
            field_dict["skipped_count"] = skipped_count
        if success_count is not UNSET:
            field_dict["success_count"] = success_count
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_import_parcel_error import GisImportParcelError # noqa: PLC0415
        d = dict(src_dict)
        def _parse_created_parcel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                created_parcel_ids_type_0 = []
                _created_parcel_ids_type_0 = data
                for created_parcel_ids_type_0_item_data in (_created_parcel_ids_type_0):
                    created_parcel_ids_type_0_item = UUID(created_parcel_ids_type_0_item_data)



                    created_parcel_ids_type_0.append(created_parcel_ids_type_0_item)

                return created_parcel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        created_parcel_ids = _parse_created_parcel_ids(d.pop("created_parcel_ids", UNSET))


        created_zone_count = d.pop("created_zone_count", UNSET)

        def _parse_errors(data: object) -> list[GisImportParcelError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in (_errors_type_0):
                    errors_type_0_item = GisImportParcelError.from_dict(errors_type_0_item_data)



                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisImportParcelError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))


        failed_count = d.pop("failed_count", UNSET)

        skipped_count = d.pop("skipped_count", UNSET)

        success_count = d.pop("success_count", UNSET)

        total = d.pop("total", UNSET)

        gis_import_parcels_result = cls(
            created_parcel_ids=created_parcel_ids,
            created_zone_count=created_zone_count,
            errors=errors,
            failed_count=failed_count,
            skipped_count=skipped_count,
            success_count=success_count,
            total=total,
        )

        return gis_import_parcels_result

