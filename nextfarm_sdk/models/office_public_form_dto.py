from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_public_form_attachment_rules_dto import OfficePublicFormAttachmentRulesDto
  from ..models.office_public_form_field_dto import OfficePublicFormFieldDto





T = TypeVar("T", bound="OfficePublicFormDto")



@_attrs_define
class OfficePublicFormDto:
    

    attachments: OfficePublicFormAttachmentRulesDto | Unset = UNSET
    cover_url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    fields: list[OfficePublicFormFieldDto] | None | Unset = UNSET
    form_token: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    table_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    view_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_public_form_attachment_rules_dto import OfficePublicFormAttachmentRulesDto # noqa: PLC0415
        from ..models.office_public_form_field_dto import OfficePublicFormFieldDto # noqa: PLC0415
        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        cover_url: None | str | Unset
        if isinstance(self.cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = self.cover_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)


        else:
            fields = self.fields

        form_token: None | str | Unset
        if isinstance(self.form_token, Unset):
            form_token = UNSET
        else:
            form_token = self.form_token

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        table_name: None | str | Unset
        if isinstance(self.table_name, Unset):
            table_name = UNSET
        else:
            table_name = self.table_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        view_name: None | str | Unset
        if isinstance(self.view_name, Unset):
            view_name = UNSET
        else:
            view_name = self.view_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if form_token is not UNSET:
            field_dict["formToken"] = form_token
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if title is not UNSET:
            field_dict["title"] = title
        if view_name is not UNSET:
            field_dict["viewName"] = view_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_public_form_attachment_rules_dto import OfficePublicFormAttachmentRulesDto # noqa: PLC0415
        from ..models.office_public_form_field_dto import OfficePublicFormFieldDto # noqa: PLC0415
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: OfficePublicFormAttachmentRulesDto | Unset
        if isinstance(_attachments,  Unset):
            attachments = UNSET
        else:
            attachments = OfficePublicFormAttachmentRulesDto.from_dict(_attachments)




        def _parse_cover_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_url = _parse_cover_url(d.pop("coverUrl", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_fields(data: object) -> list[OfficePublicFormFieldDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in (_fields_type_0):
                    fields_type_0_item = OfficePublicFormFieldDto.from_dict(fields_type_0_item_data)



                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficePublicFormFieldDto] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))


        def _parse_form_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_token = _parse_form_token(d.pop("formToken", UNSET))


        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))


        def _parse_table_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_name = _parse_table_name(d.pop("tableName", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_view_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_name = _parse_view_name(d.pop("viewName", UNSET))


        office_public_form_dto = cls(
            attachments=attachments,
            cover_url=cover_url,
            description=description,
            fields=fields,
            form_token=form_token,
            logo_url=logo_url,
            table_name=table_name,
            title=title,
            view_name=view_name,
        )

        return office_public_form_dto

