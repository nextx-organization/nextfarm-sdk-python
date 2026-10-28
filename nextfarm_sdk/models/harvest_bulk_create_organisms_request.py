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
  from ..models.harvest_organism_point_input import HarvestOrganismPointInput
  from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest





T = TypeVar("T", bound="HarvestBulkCreateOrganismsRequest")



@_attrs_define
class HarvestBulkCreateOrganismsRequest:
    

    append: bool | Unset = UNSET
    code_prefix: None | str | Unset = UNSET
    parcel_id: UUID | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET
    points: list[HarvestOrganismPointInput] | None | Unset = UNSET
    profile: HarvestOrganismProfileRequest | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_organism_point_input import HarvestOrganismPointInput # noqa: PLC0415
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        append = self.append

        code_prefix: None | str | Unset
        if isinstance(self.code_prefix, Unset):
            code_prefix = UNSET
        else:
            code_prefix = self.code_prefix

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

        points: list[dict[str, Any]] | None | Unset
        if isinstance(self.points, Unset):
            points = UNSET
        elif isinstance(self.points, list):
            points = []
            for points_type_0_item_data in self.points:
                points_type_0_item = points_type_0_item_data.to_dict()
                points.append(points_type_0_item)


        else:
            points = self.points

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if append is not UNSET:
            field_dict["append"] = append
        if code_prefix is not UNSET:
            field_dict["code_prefix"] = code_prefix
        if parcel_id is not UNSET:
            field_dict["parcel_id"] = parcel_id
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id
        if points is not UNSET:
            field_dict["points"] = points
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_organism_point_input import HarvestOrganismPointInput # noqa: PLC0415
        from ..models.harvest_organism_profile_request import HarvestOrganismProfileRequest # noqa: PLC0415
        d = dict(src_dict)
        append = d.pop("append", UNSET)

        def _parse_code_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_prefix = _parse_code_prefix(d.pop("code_prefix", UNSET))


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


        def _parse_points(data: object) -> list[HarvestOrganismPointInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                points_type_0 = []
                _points_type_0 = data
                for points_type_0_item_data in (_points_type_0):
                    points_type_0_item = HarvestOrganismPointInput.from_dict(points_type_0_item_data)



                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestOrganismPointInput] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))


        _profile = d.pop("profile", UNSET)
        profile: HarvestOrganismProfileRequest | Unset
        if isinstance(_profile,  Unset):
            profile = UNSET
        else:
            profile = HarvestOrganismProfileRequest.from_dict(_profile)




        harvest_bulk_create_organisms_request = cls(
            append=append,
            code_prefix=code_prefix,
            parcel_id=parcel_id,
            plot_id=plot_id,
            points=points,
            profile=profile,
        )

        return harvest_bulk_create_organisms_request

