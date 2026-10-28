from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_channel_webhook_dto import OfficeChannelWebhookDto





T = TypeVar("T", bound="OfficeChannelWebhookSecretDto")



@_attrs_define
class OfficeChannelWebhookSecretDto:
    

    url_path: None | str | Unset = UNSET
    webhook: OfficeChannelWebhookDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_channel_webhook_dto import OfficeChannelWebhookDto # noqa: PLC0415
        url_path: None | str | Unset
        if isinstance(self.url_path, Unset):
            url_path = UNSET
        else:
            url_path = self.url_path

        webhook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook, Unset):
            webhook = self.webhook.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if url_path is not UNSET:
            field_dict["urlPath"] = url_path
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_channel_webhook_dto import OfficeChannelWebhookDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_url_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_path = _parse_url_path(d.pop("urlPath", UNSET))


        _webhook = d.pop("webhook", UNSET)
        webhook: OfficeChannelWebhookDto | Unset
        if isinstance(_webhook,  Unset):
            webhook = UNSET
        else:
            webhook = OfficeChannelWebhookDto.from_dict(_webhook)




        office_channel_webhook_secret_dto = cls(
            url_path=url_path,
            webhook=webhook,
        )

        return office_channel_webhook_secret_dto

