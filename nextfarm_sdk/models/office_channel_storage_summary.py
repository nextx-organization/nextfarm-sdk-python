from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeChannelStorageSummary")



@_attrs_define
class OfficeChannelStorageSummary:
    

    document: int | Unset = UNSET
    links: int | Unset = UNSET
    media: int | Unset = UNSET
    other: int | Unset = UNSET
    presentation: int | Unset = UNSET
    spreadsheet: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document = self.document

        links = self.links

        media = self.media

        other = self.other

        presentation = self.presentation

        spreadsheet = self.spreadsheet


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document is not UNSET:
            field_dict["document"] = document
        if links is not UNSET:
            field_dict["links"] = links
        if media is not UNSET:
            field_dict["media"] = media
        if other is not UNSET:
            field_dict["other"] = other
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if spreadsheet is not UNSET:
            field_dict["spreadsheet"] = spreadsheet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document = d.pop("document", UNSET)

        links = d.pop("links", UNSET)

        media = d.pop("media", UNSET)

        other = d.pop("other", UNSET)

        presentation = d.pop("presentation", UNSET)

        spreadsheet = d.pop("spreadsheet", UNSET)

        office_channel_storage_summary = cls(
            document=document,
            links=links,
            media=media,
            other=other,
            presentation=presentation,
            spreadsheet=spreadsheet,
        )

        return office_channel_storage_summary

