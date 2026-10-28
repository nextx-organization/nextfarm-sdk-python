from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestFieldLogGrowersDto")



@_attrs_define
class HarvestFieldLogGrowersDto:
    

    owner_ids: list[UUID] | None | Unset = UNSET
    parcel_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_ids: list[str] | None | Unset
        if isinstance(self.owner_ids, Unset):
            owner_ids = UNSET
        elif isinstance(self.owner_ids, list):
            owner_ids = []
            for owner_ids_type_0_item_data in self.owner_ids:
                owner_ids_type_0_item = str(owner_ids_type_0_item_data)
                owner_ids.append(owner_ids_type_0_item)


        else:
            owner_ids = self.owner_ids

        parcel_ids: list[str] | None | Unset
        if isinstance(self.parcel_ids, Unset):
            parcel_ids = UNSET
        elif isinstance(self.parcel_ids, list):
            parcel_ids = []
            for parcel_ids_type_0_item_data in self.parcel_ids:
                parcel_ids_type_0_item = str(parcel_ids_type_0_item_data)
                parcel_ids.append(parcel_ids_type_0_item)


        else:
            parcel_ids = self.parcel_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_ids is not UNSET:
            field_dict["owner_ids"] = owner_ids
        if parcel_ids is not UNSET:
            field_dict["parcel_ids"] = parcel_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_owner_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_ids_type_0 = []
                _owner_ids_type_0 = data
                for owner_ids_type_0_item_data in (_owner_ids_type_0):
                    owner_ids_type_0_item = UUID(owner_ids_type_0_item_data)



                    owner_ids_type_0.append(owner_ids_type_0_item)

                return owner_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        owner_ids = _parse_owner_ids(d.pop("owner_ids", UNSET))


        def _parse_parcel_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parcel_ids_type_0 = []
                _parcel_ids_type_0 = data
                for parcel_ids_type_0_item_data in (_parcel_ids_type_0):
                    parcel_ids_type_0_item = UUID(parcel_ids_type_0_item_data)



                    parcel_ids_type_0.append(parcel_ids_type_0_item)

                return parcel_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        parcel_ids = _parse_parcel_ids(d.pop("parcel_ids", UNSET))


        harvest_field_log_growers_dto = cls(
            owner_ids=owner_ids,
            parcel_ids=parcel_ids,
        )

        return harvest_field_log_growers_dto

