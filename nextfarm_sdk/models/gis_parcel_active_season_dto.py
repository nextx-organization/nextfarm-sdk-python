from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisParcelActiveSeasonDto")



@_attrs_define
class GisParcelActiveSeasonDto:
    

    crop_type_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    plot_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        crop_type_id: str | Unset = UNSET
        if not isinstance(self.crop_type_id, Unset):
            crop_type_id = str(self.crop_type_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        plot_id: None | str | Unset
        if isinstance(self.plot_id, Unset):
            plot_id = UNSET
        elif isinstance(self.plot_id, UUID):
            plot_id = str(self.plot_id)
        else:
            plot_id = self.plot_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if crop_type_id is not UNSET:
            field_dict["crop_type_id"] = crop_type_id
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if plot_id is not UNSET:
            field_dict["plot_id"] = plot_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _crop_type_id = d.pop("crop_type_id", UNSET)
        crop_type_id: UUID | Unset
        if isinstance(_crop_type_id,  Unset):
            crop_type_id = UNSET
        else:
            crop_type_id = UUID(_crop_type_id)




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


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


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


        gis_parcel_active_season_dto = cls(
            crop_type_id=crop_type_id,
            id=id,
            kind=kind,
            name=name,
            plot_id=plot_id,
        )

        return gis_parcel_active_season_dto

