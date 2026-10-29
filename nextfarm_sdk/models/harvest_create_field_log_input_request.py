from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="HarvestCreateFieldLogInputRequest")



@_attrs_define
class HarvestCreateFieldLogInputRequest:
    

    inventory_issue_id: None | Unset | UUID = UNSET
    item_id: UUID | Unset = UNSET
    item_name: None | str | Unset = UNSET
    lot_no: None | str | Unset = UNSET
    quantity: float | Unset = UNSET
    unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        inventory_issue_id: None | str | Unset
        if isinstance(self.inventory_issue_id, Unset):
            inventory_issue_id = UNSET
        elif isinstance(self.inventory_issue_id, UUID):
            inventory_issue_id = str(self.inventory_issue_id)
        else:
            inventory_issue_id = self.inventory_issue_id

        item_id: str | Unset = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        item_name: None | str | Unset
        if isinstance(self.item_name, Unset):
            item_name = UNSET
        else:
            item_name = self.item_name

        lot_no: None | str | Unset
        if isinstance(self.lot_no, Unset):
            lot_no = UNSET
        else:
            lot_no = self.lot_no

        quantity = self.quantity

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if inventory_issue_id is not UNSET:
            field_dict["inventory_issue_id"] = inventory_issue_id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if item_name is not UNSET:
            field_dict["item_name"] = item_name
        if lot_no is not UNSET:
            field_dict["lot_no"] = lot_no
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_inventory_issue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inventory_issue_id_type_0 = UUID(data)



                return inventory_issue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        inventory_issue_id = _parse_inventory_issue_id(d.pop("inventory_issue_id", UNSET))


        _item_id = d.pop("item_id", UNSET)
        item_id: UUID | Unset
        if isinstance(_item_id,  Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)




        def _parse_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_name = _parse_item_name(d.pop("item_name", UNSET))


        def _parse_lot_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_no = _parse_lot_no(d.pop("lot_no", UNSET))


        quantity = d.pop("quantity", UNSET)

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        harvest_create_field_log_input_request = cls(
            inventory_issue_id=inventory_issue_id,
            item_id=item_id,
            item_name=item_name,
            lot_no=lot_no,
            quantity=quantity,
            unit=unit,
        )

        return harvest_create_field_log_input_request

