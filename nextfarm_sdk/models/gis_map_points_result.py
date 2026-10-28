from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gis_map_cluster_dto import GisMapClusterDto
  from ..models.gis_map_point_dto import GisMapPointDto





T = TypeVar("T", bound="GisMapPointsResult")



@_attrs_define
class GisMapPointsResult:
    

    clusters: list[GisMapClusterDto] | None | Unset = UNSET
    limit: int | Unset = UNSET
    mode: None | str | Unset = UNSET
    points: list[GisMapPointDto] | None | Unset = UNSET
    total: int | Unset = UNSET
    truncated: bool | Unset = UNSET
    zoom: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_map_cluster_dto import GisMapClusterDto # noqa: PLC0415
        from ..models.gis_map_point_dto import GisMapPointDto # noqa: PLC0415
        clusters: list[dict[str, Any]] | None | Unset
        if isinstance(self.clusters, Unset):
            clusters = UNSET
        elif isinstance(self.clusters, list):
            clusters = []
            for clusters_type_0_item_data in self.clusters:
                clusters_type_0_item = clusters_type_0_item_data.to_dict()
                clusters.append(clusters_type_0_item)


        else:
            clusters = self.clusters

        limit = self.limit

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

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

        total = self.total

        truncated = self.truncated

        zoom: int | None | Unset
        if isinstance(self.zoom, Unset):
            zoom = UNSET
        else:
            zoom = self.zoom


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if limit is not UNSET:
            field_dict["limit"] = limit
        if mode is not UNSET:
            field_dict["mode"] = mode
        if points is not UNSET:
            field_dict["points"] = points
        if total is not UNSET:
            field_dict["total"] = total
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if zoom is not UNSET:
            field_dict["zoom"] = zoom

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_map_cluster_dto import GisMapClusterDto # noqa: PLC0415
        from ..models.gis_map_point_dto import GisMapPointDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_clusters(data: object) -> list[GisMapClusterDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                clusters_type_0 = []
                _clusters_type_0 = data
                for clusters_type_0_item_data in (_clusters_type_0):
                    clusters_type_0_item = GisMapClusterDto.from_dict(clusters_type_0_item_data)



                    clusters_type_0.append(clusters_type_0_item)

                return clusters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisMapClusterDto] | None | Unset, data)

        clusters = _parse_clusters(d.pop("clusters", UNSET))


        limit = d.pop("limit", UNSET)

        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        def _parse_points(data: object) -> list[GisMapPointDto] | None | Unset:
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
                    points_type_0_item = GisMapPointDto.from_dict(points_type_0_item_data)



                    points_type_0.append(points_type_0_item)

                return points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GisMapPointDto] | None | Unset, data)

        points = _parse_points(d.pop("points", UNSET))


        total = d.pop("total", UNSET)

        truncated = d.pop("truncated", UNSET)

        def _parse_zoom(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        zoom = _parse_zoom(d.pop("zoom", UNSET))


        gis_map_points_result = cls(
            clusters=clusters,
            limit=limit,
            mode=mode,
            points=points,
            total=total,
            truncated=truncated,
            zoom=zoom,
        )

        return gis_map_points_result

