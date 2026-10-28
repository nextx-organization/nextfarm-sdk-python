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
  from ..models.office_chat_search_categories_dto import OfficeChatSearchCategoriesDto





T = TypeVar("T", bound="OfficeChatPreferencesDto")



@_attrs_define
class OfficeChatPreferencesDto:
    

    collapsed_sections: list[str] | None | Unset = UNSET
    recent_emojis: list[str] | None | Unset = UNSET
    right_panel_width: int | None | Unset = UNSET
    search_categories: OfficeChatSearchCategoriesDto | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_search_categories_dto import OfficeChatSearchCategoriesDto # noqa: PLC0415
        collapsed_sections: list[str] | None | Unset
        if isinstance(self.collapsed_sections, Unset):
            collapsed_sections = UNSET
        elif isinstance(self.collapsed_sections, list):
            collapsed_sections = self.collapsed_sections


        else:
            collapsed_sections = self.collapsed_sections

        recent_emojis: list[str] | None | Unset
        if isinstance(self.recent_emojis, Unset):
            recent_emojis = UNSET
        elif isinstance(self.recent_emojis, list):
            recent_emojis = self.recent_emojis


        else:
            recent_emojis = self.recent_emojis

        right_panel_width: int | None | Unset
        if isinstance(self.right_panel_width, Unset):
            right_panel_width = UNSET
        else:
            right_panel_width = self.right_panel_width

        search_categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_categories, Unset):
            search_categories = self.search_categories.to_dict()

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if collapsed_sections is not UNSET:
            field_dict["collapsedSections"] = collapsed_sections
        if recent_emojis is not UNSET:
            field_dict["recentEmojis"] = recent_emojis
        if right_panel_width is not UNSET:
            field_dict["rightPanelWidth"] = right_panel_width
        if search_categories is not UNSET:
            field_dict["searchCategories"] = search_categories
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_search_categories_dto import OfficeChatSearchCategoriesDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_collapsed_sections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collapsed_sections_type_0 = cast(list[str], data)

                return collapsed_sections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collapsed_sections = _parse_collapsed_sections(d.pop("collapsedSections", UNSET))


        def _parse_recent_emojis(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                recent_emojis_type_0 = cast(list[str], data)

                return recent_emojis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        recent_emojis = _parse_recent_emojis(d.pop("recentEmojis", UNSET))


        def _parse_right_panel_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        right_panel_width = _parse_right_panel_width(d.pop("rightPanelWidth", UNSET))


        _search_categories = d.pop("searchCategories", UNSET)
        search_categories: OfficeChatSearchCategoriesDto | Unset
        if isinstance(_search_categories,  Unset):
            search_categories = UNSET
        else:
            search_categories = OfficeChatSearchCategoriesDto.from_dict(_search_categories)




        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        office_chat_preferences_dto = cls(
            collapsed_sections=collapsed_sections,
            recent_emojis=recent_emojis,
            right_panel_width=right_panel_width,
            search_categories=search_categories,
            updated_at=updated_at,
        )

        return office_chat_preferences_dto

