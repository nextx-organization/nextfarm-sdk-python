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
  from ..models.iot_schedule_batch_item_request import IotScheduleBatchItemRequest





T = TypeVar("T", bound="IotSaveScheduleBatchRequest")



@_attrs_define
class IotSaveScheduleBatchRequest:
    

    delete_ids: list[UUID] | None | Unset = UNSET
    items: list[IotScheduleBatchItemRequest] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.iot_schedule_batch_item_request import IotScheduleBatchItemRequest # noqa: PLC0415
        delete_ids: list[str] | None | Unset
        if isinstance(self.delete_ids, Unset):
            delete_ids = UNSET
        elif isinstance(self.delete_ids, list):
            delete_ids = []
            for delete_ids_type_0_item_data in self.delete_ids:
                delete_ids_type_0_item = str(delete_ids_type_0_item_data)
                delete_ids.append(delete_ids_type_0_item)


        else:
            delete_ids = self.delete_ids

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if delete_ids is not UNSET:
            field_dict["delete_ids"] = delete_ids
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iot_schedule_batch_item_request import IotScheduleBatchItemRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_delete_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                delete_ids_type_0 = []
                _delete_ids_type_0 = data
                for delete_ids_type_0_item_data in (_delete_ids_type_0):
                    delete_ids_type_0_item = UUID(delete_ids_type_0_item_data)



                    delete_ids_type_0.append(delete_ids_type_0_item)

                return delete_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        delete_ids = _parse_delete_ids(d.pop("delete_ids", UNSET))


        def _parse_items(data: object) -> list[IotScheduleBatchItemRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = IotScheduleBatchItemRequest.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IotScheduleBatchItemRequest] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        iot_save_schedule_batch_request = cls(
            delete_ids=delete_ids,
            items=items,
        )

        return iot_save_schedule_batch_request

