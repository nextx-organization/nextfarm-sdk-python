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
  from ..models.harvest_care_age_bucket_dto import HarvestCareAgeBucketDto





T = TypeVar("T", bound="HarvestCareInputsDto")



@_attrs_define
class HarvestCareInputsDto:
    

    age_buckets: list[HarvestCareAgeBucketDto] | None | Unset = UNSET
    last_flowering_on: datetime.date | None | Unset = UNSET
    last_harvest_on: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_care_age_bucket_dto import HarvestCareAgeBucketDto # noqa: PLC0415
        age_buckets: list[dict[str, Any]] | None | Unset
        if isinstance(self.age_buckets, Unset):
            age_buckets = UNSET
        elif isinstance(self.age_buckets, list):
            age_buckets = []
            for age_buckets_type_0_item_data in self.age_buckets:
                age_buckets_type_0_item = age_buckets_type_0_item_data.to_dict()
                age_buckets.append(age_buckets_type_0_item)


        else:
            age_buckets = self.age_buckets

        last_flowering_on: None | str | Unset
        if isinstance(self.last_flowering_on, Unset):
            last_flowering_on = UNSET
        elif isinstance(self.last_flowering_on, datetime.date):
            last_flowering_on = self.last_flowering_on.isoformat()
        else:
            last_flowering_on = self.last_flowering_on

        last_harvest_on: None | str | Unset
        if isinstance(self.last_harvest_on, Unset):
            last_harvest_on = UNSET
        elif isinstance(self.last_harvest_on, datetime.date):
            last_harvest_on = self.last_harvest_on.isoformat()
        else:
            last_harvest_on = self.last_harvest_on


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if age_buckets is not UNSET:
            field_dict["age_buckets"] = age_buckets
        if last_flowering_on is not UNSET:
            field_dict["last_flowering_on"] = last_flowering_on
        if last_harvest_on is not UNSET:
            field_dict["last_harvest_on"] = last_harvest_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_care_age_bucket_dto import HarvestCareAgeBucketDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_age_buckets(data: object) -> list[HarvestCareAgeBucketDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                age_buckets_type_0 = []
                _age_buckets_type_0 = data
                for age_buckets_type_0_item_data in (_age_buckets_type_0):
                    age_buckets_type_0_item = HarvestCareAgeBucketDto.from_dict(age_buckets_type_0_item_data)



                    age_buckets_type_0.append(age_buckets_type_0_item)

                return age_buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestCareAgeBucketDto] | None | Unset, data)

        age_buckets = _parse_age_buckets(d.pop("age_buckets", UNSET))


        def _parse_last_flowering_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_flowering_on_type_0 = datetime.date.fromisoformat(data)



                return last_flowering_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_flowering_on = _parse_last_flowering_on(d.pop("last_flowering_on", UNSET))


        def _parse_last_harvest_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_harvest_on_type_0 = datetime.date.fromisoformat(data)



                return last_harvest_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_harvest_on = _parse_last_harvest_on(d.pop("last_harvest_on", UNSET))


        harvest_care_inputs_dto = cls(
            age_buckets=age_buckets,
            last_flowering_on=last_flowering_on,
            last_harvest_on=last_harvest_on,
        )

        return harvest_care_inputs_dto

