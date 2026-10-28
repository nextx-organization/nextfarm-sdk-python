from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeWebhookKeyNode")



@_attrs_define
class OfficeWebhookKeyNode:
    

    children: list[OfficeWebhookKeyNode] | None | Unset = UNSET
    example: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)


        else:
            children = self.children

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if children is not UNSET:
            field_dict["children"] = children
        if example is not UNSET:
            field_dict["example"] = example
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_children(data: object) -> list[OfficeWebhookKeyNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in (_children_type_0):
                    children_type_0_item = OfficeWebhookKeyNode.from_dict(children_type_0_item_data)



                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeWebhookKeyNode] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))


        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        office_webhook_key_node = cls(
            children=children,
            example=example,
            name=name,
            path=path,
            type_=type_,
        )

        return office_webhook_key_node

