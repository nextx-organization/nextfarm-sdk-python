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






T = TypeVar("T", bound="HarvestTraceIncidentDto")



@_attrs_define
class HarvestTraceIncidentDto:
    

    anchored_hash: None | str | Unset = UNSET
    bundle_version: int | Unset = UNSET
    current_hash: None | str | Unset = UNSET
    detected_at: datetime.datetime | Unset = UNSET
    diff_json: None | str | Unset = UNSET
    has_newer_version: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    parcel_code: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    resolution: None | str | Unset = UNSET
    resolution_note: None | str | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    restore_requested_at: datetime.datetime | None | Unset = UNSET
    restore_requested_by: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    trace_bundle_id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        anchored_hash: None | str | Unset
        if isinstance(self.anchored_hash, Unset):
            anchored_hash = UNSET
        else:
            anchored_hash = self.anchored_hash

        bundle_version = self.bundle_version

        current_hash: None | str | Unset
        if isinstance(self.current_hash, Unset):
            current_hash = UNSET
        else:
            current_hash = self.current_hash

        detected_at: str | Unset = UNSET
        if not isinstance(self.detected_at, Unset):
            detected_at = self.detected_at.isoformat()

        diff_json: None | str | Unset
        if isinstance(self.diff_json, Unset):
            diff_json = UNSET
        else:
            diff_json = self.diff_json

        has_newer_version = self.has_newer_version

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

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

        resolution: None | str | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        resolution_note: None | str | Unset
        if isinstance(self.resolution_note, Unset):
            resolution_note = UNSET
        else:
            resolution_note = self.resolution_note

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        restore_requested_at: None | str | Unset
        if isinstance(self.restore_requested_at, Unset):
            restore_requested_at = UNSET
        elif isinstance(self.restore_requested_at, datetime.datetime):
            restore_requested_at = self.restore_requested_at.isoformat()
        else:
            restore_requested_at = self.restore_requested_at

        restore_requested_by: None | str | Unset
        if isinstance(self.restore_requested_by, Unset):
            restore_requested_by = UNSET
        elif isinstance(self.restore_requested_by, UUID):
            restore_requested_by = str(self.restore_requested_by)
        else:
            restore_requested_by = self.restore_requested_by

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        trace_bundle_id: str | Unset = UNSET
        if not isinstance(self.trace_bundle_id, Unset):
            trace_bundle_id = str(self.trace_bundle_id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchored_hash is not UNSET:
            field_dict["anchored_hash"] = anchored_hash
        if bundle_version is not UNSET:
            field_dict["bundle_version"] = bundle_version
        if current_hash is not UNSET:
            field_dict["current_hash"] = current_hash
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if diff_json is not UNSET:
            field_dict["diff_json"] = diff_json
        if has_newer_version is not UNSET:
            field_dict["has_newer_version"] = has_newer_version
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if product is not UNSET:
            field_dict["product"] = product
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolution_note is not UNSET:
            field_dict["resolution_note"] = resolution_note
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if restore_requested_at is not UNSET:
            field_dict["restore_requested_at"] = restore_requested_at
        if restore_requested_by is not UNSET:
            field_dict["restore_requested_by"] = restore_requested_by
        if status is not UNSET:
            field_dict["status"] = status
        if trace_bundle_id is not UNSET:
            field_dict["trace_bundle_id"] = trace_bundle_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_anchored_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchored_hash = _parse_anchored_hash(d.pop("anchored_hash", UNSET))


        bundle_version = d.pop("bundle_version", UNSET)

        def _parse_current_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_hash = _parse_current_hash(d.pop("current_hash", UNSET))


        _detected_at = d.pop("detected_at", UNSET)
        detected_at: datetime.datetime | Unset
        if isinstance(_detected_at,  Unset):
            detected_at = UNSET
        else:
            detected_at = datetime.datetime.fromisoformat(_detected_at)




        def _parse_diff_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diff_json = _parse_diff_json(d.pop("diff_json", UNSET))


        has_newer_version = d.pop("has_newer_version", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


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


        def _parse_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))


        def _parse_resolution_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution_note = _parse_resolution_note(d.pop("resolution_note", UNSET))


        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)



                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))


        def _parse_restore_requested_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_requested_at_type_0 = datetime.datetime.fromisoformat(data)



                return restore_requested_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        restore_requested_at = _parse_restore_requested_at(d.pop("restore_requested_at", UNSET))


        def _parse_restore_requested_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_requested_by_type_0 = UUID(data)



                return restore_requested_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        restore_requested_by = _parse_restore_requested_by(d.pop("restore_requested_by", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _trace_bundle_id = d.pop("trace_bundle_id", UNSET)
        trace_bundle_id: UUID | Unset
        if isinstance(_trace_bundle_id,  Unset):
            trace_bundle_id = UNSET
        else:
            trace_bundle_id = UUID(_trace_bundle_id)




        _workspace_id = d.pop("workspace_id", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        harvest_trace_incident_dto = cls(
            anchored_hash=anchored_hash,
            bundle_version=bundle_version,
            current_hash=current_hash,
            detected_at=detected_at,
            diff_json=diff_json,
            has_newer_version=has_newer_version,
            id=id,
            kind=kind,
            parcel_code=parcel_code,
            product=product,
            resolution=resolution,
            resolution_note=resolution_note,
            resolved_at=resolved_at,
            restore_requested_at=restore_requested_at,
            restore_requested_by=restore_requested_by,
            status=status,
            trace_bundle_id=trace_bundle_id,
            workspace_id=workspace_id,
        )

        return harvest_trace_incident_dto

