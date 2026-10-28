from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_spotlight_hit import GisSpotlightHit





T = TypeVar("T", bound="GisGisSearchResult")



@_attrs_define
class GisGisSearchResult:
    

    farmers: list[GisSpotlightHit] | None | Unset = UNSET
    parcels: list[GisSpotlightHit] | None | Unset = UNSET
    seasons: list[GisSpotlightHit] | None | Unset = UNSET
    zones: list[GisSpotlightHit] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_spotlight_hit import GisSpotlightHit # noqa: PLC0415
        farmers: list[dict[str, Any]] | None | Unset
        if isinstance(self.farmers, Unset):
            farmers = UNSET
        elif isinstance(self.farmers, list):
            farmers = []
            for farmers_type_0_item_data in self.farmers:
                farmers_type_0_item = farmers_type_0_item_data.to_dict()
                farmers.append(farmers_type_0_item)


        else:
            farmers = self.farmers

        parcels: list[dict[str, Any]] | None | Unset
        if isinstance(self.parcels, Unset):
            parcels = UNSET
        elif isinstance(self.parcels, list):
            parcels = []
            for parcels_type_0_item_data in self.parcels:
                parcels_type_0_item = parcels_type_0_item_data.to_dict()
                parcels.append(parcels_type_0_item)


        else:
            parcels = self.parcels

        seasons: list[dict[str, Any]] | None | Unset
        if isinstance(self.seasons, Unset):
            seasons = UNSET
        elif isinstance(self.seasons, list):
            seasons = []
            for seasons_type_0_item_data in self.seasons:
                seasons_type_0_item = seasons_type_0_item_data.to_dict()
                seasons.append(seasons_type_0_item)


        else:
            seasons = self.seasons

        zones: list[dict[str, Any]] | None | Unset
        if isinstance(self.zones, Unset):
            zones = UNSET
        elif isinstance(self.zones, list):
            zones = []
            for zones_type_0_item_data in self.zones:
                zones_type_0_item = zones_type_0_item_data.to_dict()
                zones.append(zones_type_0_item)


        else:
            zones = self.zones


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if farmers is not UNSET:
            field_dict["farmers"] = farmers
        if parcels is not UNSET:
            field_dict["parcels"] = parcels
        if seasons is not UNSET:
            field_dict["seasons"] = seasons
        if zones is not UNSET:
            field_dict["zones"] = zones

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_spotlight_hit import GisSpotlightHit # noqa: PLC0415
        d = dict(src_dict)
        def _parse_farmers(data: object) -> list[GisSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                farmers_type_0 = []
                _farmers_type_0 = data
                for farmers_type_0_item_data in (_farmers_type_0):
                    farmers_type_0_item = GisSpotlightHit.from_dict(farmers_type_0_item_data)



                    farmers_type_0.append(farmers_type_0_item)

                return farmers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSpotlightHit] | None | Unset, data)

        farmers = _parse_farmers(d.pop("farmers", UNSET))


        def _parse_parcels(data: object) -> list[GisSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parcels_type_0 = []
                _parcels_type_0 = data
                for parcels_type_0_item_data in (_parcels_type_0):
                    parcels_type_0_item = GisSpotlightHit.from_dict(parcels_type_0_item_data)



                    parcels_type_0.append(parcels_type_0_item)

                return parcels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSpotlightHit] | None | Unset, data)

        parcels = _parse_parcels(d.pop("parcels", UNSET))


        def _parse_seasons(data: object) -> list[GisSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                seasons_type_0 = []
                _seasons_type_0 = data
                for seasons_type_0_item_data in (_seasons_type_0):
                    seasons_type_0_item = GisSpotlightHit.from_dict(seasons_type_0_item_data)



                    seasons_type_0.append(seasons_type_0_item)

                return seasons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSpotlightHit] | None | Unset, data)

        seasons = _parse_seasons(d.pop("seasons", UNSET))


        def _parse_zones(data: object) -> list[GisSpotlightHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                zones_type_0 = []
                _zones_type_0 = data
                for zones_type_0_item_data in (_zones_type_0):
                    zones_type_0_item = GisSpotlightHit.from_dict(zones_type_0_item_data)



                    zones_type_0.append(zones_type_0_item)

                return zones_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisSpotlightHit] | None | Unset, data)

        zones = _parse_zones(d.pop("zones", UNSET))


        gis_gis_search_result = cls(
            farmers=farmers,
            parcels=parcels,
            seasons=seasons,
            zones=zones,
        )

        return gis_gis_search_result

