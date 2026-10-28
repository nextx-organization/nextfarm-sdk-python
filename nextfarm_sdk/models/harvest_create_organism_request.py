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
  from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest





T = TypeVar("T", bound="HarvestCreateOrganismRequest")



@_attrs_define
class HarvestCreateOrganismRequest:
    

    code: None | str | Unset = UNSET
    group_id: None | Unset | UUID = UNSET
    kind: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    position_in_row: int | None | Unset = UNSET
    profile: HarvestOrganismProfileRequest | Unset = UNSET
    quantity: int | Unset = UNSET
    row_no: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        parcel_id: str | Unset = UNSET
        if not isinstance(self.parcel_id, Unset):
            parcel_id = str(self.parcel_id)

        plot_id: None | str | Unset
        if isinstance(self.plot_id, Unset):
            plot_id = UNSET
        elif isinstance(self.plot_id, UUID):
            plot_id = str(self.plot_id)
        else:
            plot_id = self.plot_id

        position_in_row: int | None | Unset
        if isinstance(self.position_in_row, Unset):
            position_in_row = UNSET
        else:
            position_in_row = self.position_in_row

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        quantity = self.quantity

        row_no: int | None | Unset
        if isinstance(self.row_no, Unset):
            row_no = UNSET
        else:
            row_no = self.row_no


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if position_in_row is not UNSET:
            field_dict["position_in_row"] = position_in_row
        if profile is not UNSET:
            field_dict["profile"] = profile
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if row_no is not UNSET:
            field_dict["row_no"] = row_no

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        _parcel_id = d.pop("parcel_id", UNSET)
        parcel_id: UUID | Unset
        if isinstance(_parcel_id,  Unset):
            parcel_id = UNSET
        else:
            parcel_id = UUID(_parcel_id)




        def _parse_plot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                plot_id_type_0 = UUID(data)



                return plot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        plot_id = _parse_plot_id(d.pop("plot_id", UNSET))


        def _parse_position_in_row(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_in_row = _parse_position_in_row(d.pop("position_in_row", UNSET))


        _profile = d.pop("profile", UNSET)
        profile: HarvestOrganismProfileRequest | Unset
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = HarvestOrganismProfileRequest.from_dict(_profile)




        quantity = d.pop("quantity", UNSET)

        def _parse_row_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_no = _parse_row_no(d.pop("row_no", UNSET))


        harvest_create_organism_request = cls(
            code=code,
            group_id=group_id,
            kind=kind,
            latitude=latitude,
            longitude=longitude,
            parcel_id=parcel_id,
            plot_id=plot_id,
            position_in_row=position_in_row,
            profile=profile,
            quantity=quantity,
            row_no=row_no,
        )

        return harvest_create_organism_request

