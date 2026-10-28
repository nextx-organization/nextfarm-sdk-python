from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.harvest_dataset_query_filters_type_0 import HarvestDatasetQueryFiltersType0





T = TypeVar("T", bound="HarvestDatasetQuery")



@_attrs_define
class HarvestDatasetQuery:
    

    dataset: None | str | Unset = UNSET
    filters: HarvestDatasetQueryFiltersType0 | None | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    group_by: list[str] | None | Unset = UNSET
    include_sample: bool | Unset = UNSET
    limit: int | None | Unset = UNSET
    mode: None | str | Unset = UNSET
    to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_dataset_query_filters_type_0 import HarvestDatasetQueryFiltersType0 # noqa: PLC0415
        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, HarvestDatasetQueryFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        group_by: list[str] | None | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, list):
            group_by = self.group_by


        else:
            group_by = self.group_by

        include_sample = self.include_sample

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_ is not UNSET:
            field_dict["from"] = from_
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
        if include_sample is not UNSET:
            field_dict["include_sample"] = include_sample
        if limit is not UNSET:
            field_dict["limit"] = limit
        if mode is not UNSET:
            field_dict["mode"] = mode
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_dataset_query_filters_type_0 import HarvestDatasetQueryFiltersType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        def _parse_filters(data: object) -> HarvestDatasetQueryFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = HarvestDatasetQueryFiltersType0.from_dict(data)



                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HarvestDatasetQueryFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_group_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_by_type_0 = cast(list[str], data)

                return group_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))


        include_sample = d.pop("include_sample", UNSET)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))


        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        harvest_dataset_query = cls(
            dataset=dataset,
            filters=filters,
            from_=from_,
            group_by=group_by,
            include_sample=include_sample,
            limit=limit,
            mode=mode,
            to=to,
        )

        return harvest_dataset_query

