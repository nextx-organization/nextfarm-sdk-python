from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_product_benefit_request import HarvestProductBenefitRequest





T = TypeVar("T", bound="HarvestUpsertProductInfoRequest")



@_attrs_define
class HarvestUpsertProductInfoRequest:
    

    benefits: list[HarvestProductBenefitRequest] | None | Unset = UNSET
    crop_name: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    is_active: bool | Unset = UNSET
    tagline: None | str | Unset = UNSET
    usage_note: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_product_benefit_request import HarvestProductBenefitRequest # noqa: PLC0415
        benefits: list[dict[str, Any]] | None | Unset
        if isinstance(self.benefits, Unset):
            benefits = UNSET
        elif isinstance(self.benefits, list):
            benefits = []
            for benefits_type_0_item_data in self.benefits:
                benefits_type_0_item = benefits_type_0_item_data.to_dict()
                benefits.append(benefits_type_0_item)


        else:
            benefits = self.benefits

        crop_name: None | str | Unset
        if isinstance(self.crop_name, Unset):
            crop_name = UNSET
        else:
            crop_name = self.crop_name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls


        else:
            image_urls = self.image_urls

        is_active = self.is_active

        tagline: None | str | Unset
        if isinstance(self.tagline, Unset):
            tagline = UNSET
        else:
            tagline = self.tagline

        usage_note: None | str | Unset
        if isinstance(self.usage_note, Unset):
            usage_note = UNSET
        else:
            usage_note = self.usage_note


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if benefits is not UNSET:
            field_dict["benefits"] = benefits
        if crop_name is not UNSET:
            field_dict["crop_name"] = crop_name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if tagline is not UNSET:
            field_dict["tagline"] = tagline
        if usage_note is not UNSET:
            field_dict["usage_note"] = usage_note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_product_benefit_request import HarvestProductBenefitRequest # noqa: PLC0415
        d = dict(src_dict)
        def _parse_benefits(data: object) -> list[HarvestProductBenefitRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benefits_type_0 = []
                _benefits_type_0 = data
                for benefits_type_0_item_data in (_benefits_type_0):
                    benefits_type_0_item = HarvestProductBenefitRequest.from_dict(benefits_type_0_item_data)



                    benefits_type_0.append(benefits_type_0_item)

                return benefits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestProductBenefitRequest] | None | Unset, data)

        benefits = _parse_benefits(d.pop("benefits", UNSET))


        def _parse_crop_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crop_name = _parse_crop_name(d.pop("crop_name", UNSET))


        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))


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


        is_active = d.pop("is_active", UNSET)

        def _parse_tagline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tagline = _parse_tagline(d.pop("tagline", UNSET))


        def _parse_usage_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_note = _parse_usage_note(d.pop("usage_note", UNSET))


        harvest_upsert_product_info_request = cls(
            benefits=benefits,
            crop_name=crop_name,
            display_name=display_name,
            image_urls=image_urls,
            is_active=is_active,
            tagline=tagline,
            usage_note=usage_note,
        )

        return harvest_upsert_product_info_request

