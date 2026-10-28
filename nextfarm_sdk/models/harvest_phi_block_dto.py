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






T = TypeVar("T", bound="HarvestPhiBlockDto")



@_attrs_define
class HarvestPhiBlockDto:
    

    active_ingredient: None | str | Unset = UNSET
    field_log_id: UUID | Unset = UNSET
    kind: None | str | Unset = UNSET
    phi_days: int | Unset = UNSET
    product: None | str | Unset = UNSET
    safe_from: datetime.date | Unset = UNSET
    sprayed_on: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_ingredient: None | str | Unset
        if isinstance(self.active_ingredient, Unset):
            active_ingredient = UNSET
        else:
            active_ingredient = self.active_ingredient

        field_log_id: str | Unset = UNSET
        if not isinstance(self.field_log_id, Unset):
            field_log_id = str(self.field_log_id)

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        phi_days = self.phi_days

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        safe_from: str | Unset = UNSET
        if not isinstance(self.safe_from, Unset):
            safe_from = self.safe_from.isoformat()

        sprayed_on: str | Unset = UNSET
        if not isinstance(self.sprayed_on, Unset):
            sprayed_on = self.sprayed_on.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_ingredient is not UNSET:
            field_dict["active_ingredient"] = active_ingredient
        if field_log_id is not UNSET:
            field_dict["field_log_id"] = field_log_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if phi_days is not UNSET:
            field_dict["phi_days"] = phi_days
        if product is not UNSET:
            field_dict["product"] = product
        if safe_from is not UNSET:
            field_dict["safe_from"] = safe_from
        if sprayed_on is not UNSET:
            field_dict["sprayed_on"] = sprayed_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_active_ingredient(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_ingredient = _parse_active_ingredient(d.pop("active_ingredient", UNSET))


        _field_log_id = d.pop("field_log_id", UNSET)
        field_log_id: UUID | Unset
        if isinstance(_field_log_id,  Unset):
            field_log_id = UNSET
        else:
            field_log_id = UUID(_field_log_id)




        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        phi_days = d.pop("phi_days", UNSET)

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))


        _safe_from = d.pop("safe_from", UNSET)
        safe_from: datetime.date | Unset
        if isinstance(_safe_from,  Unset):
            safe_from = UNSET
        else:
            safe_from = datetime.date.fromisoformat(_safe_from)




        _sprayed_on = d.pop("sprayed_on", UNSET)
        sprayed_on: datetime.date | Unset
        if isinstance(_sprayed_on,  Unset):
            sprayed_on = UNSET
        else:
            sprayed_on = datetime.date.fromisoformat(_sprayed_on)




        harvest_phi_block_dto = cls(
            active_ingredient=active_ingredient,
            field_log_id=field_log_id,
            kind=kind,
            phi_days=phi_days,
            product=product,
            safe_from=safe_from,
            sprayed_on=sprayed_on,
        )

        return harvest_phi_block_dto

