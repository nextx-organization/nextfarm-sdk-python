from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestAddProductInfoImagesRequest")



@_attrs_define
class HarvestAddProductInfoImagesRequest:
    

    image_urls: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls


        else:
            image_urls = self.image_urls


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_image_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_urls = _parse_image_urls(d.pop("image_urls", UNSET))


        harvest_add_product_info_images_request = cls(
            image_urls=image_urls,
        )

        return harvest_add_product_info_images_request

