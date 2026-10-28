from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_asset_dto import OfficeAssetDto
  from ..models.office_asset_value_summary_dto import OfficeAssetValueSummaryDto





T = TypeVar("T", bound="OfficeAssetListDto")



@_attrs_define
class OfficeAssetListDto:
    

    assets: list[OfficeAssetDto] | None | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    summary: OfficeAssetValueSummaryDto | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_asset_dto import OfficeAssetDto # noqa: PLC0415
        from ..models.office_asset_value_summary_dto import OfficeAssetValueSummaryDto # noqa: PLC0415
        assets: list[dict[str, Any]] | None | Unset
        if isinstance(self.assets, Unset):
            assets = UNSET
        elif isinstance(self.assets, list):
            assets = []
            for assets_type_0_item_data in self.assets:
                assets_type_0_item = assets_type_0_item_data.to_dict()
                assets.append(assets_type_0_item)


        else:
            assets = self.assets

        page = self.page

        page_size = self.page_size

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assets is not UNSET:
            field_dict["assets"] = assets
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if summary is not UNSET:
            field_dict["summary"] = summary
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_asset_dto import OfficeAssetDto # noqa: PLC0415
        from ..models.office_asset_value_summary_dto import OfficeAssetValueSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_assets(data: object) -> list[OfficeAssetDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assets_type_0 = []
                _assets_type_0 = data
                for assets_type_0_item_data in (_assets_type_0):
                    assets_type_0_item = OfficeAssetDto.from_dict(assets_type_0_item_data)



                    assets_type_0.append(assets_type_0_item)

                return assets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAssetDto] | None | Unset, data)

        assets = _parse_assets(d.pop("assets", UNSET))


        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: OfficeAssetValueSummaryDto | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = OfficeAssetValueSummaryDto.from_dict(_summary)




        total = d.pop("total", UNSET)

        office_asset_list_dto = cls(
            assets=assets,
            page=page,
            page_size=page_size,
            summary=summary,
            total=total,
        )

        return office_asset_list_dto

