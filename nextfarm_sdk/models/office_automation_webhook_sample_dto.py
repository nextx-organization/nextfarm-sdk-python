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
  from ..models.office_webhook_key_node import OfficeWebhookKeyNode





T = TypeVar("T", bound="OfficeAutomationWebhookSampleDto")



@_attrs_define
class OfficeAutomationWebhookSampleDto:
    

    keys: list[OfficeWebhookKeyNode] | None | Unset = UNSET
    listen_until: datetime.datetime | None | Unset = UNSET
    listening: bool | Unset = UNSET
    sample: Any | Unset = UNSET
    sample_at: datetime.datetime | None | Unset = UNSET
    sample_source: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_webhook_key_node import OfficeWebhookKeyNode # noqa: PLC0415
        keys: list[dict[str, Any]] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = []
            for keys_type_0_item_data in self.keys:
                keys_type_0_item = keys_type_0_item_data.to_dict()
                keys.append(keys_type_0_item)


        else:
            keys = self.keys

        listen_until: None | str | Unset
        if isinstance(self.listen_until, Unset):
            listen_until = UNSET
        elif isinstance(self.listen_until, datetime.datetime):
            listen_until = self.listen_until.isoformat()
        else:
            listen_until = self.listen_until

        listening = self.listening

        sample = self.sample

        sample_at: None | str | Unset
        if isinstance(self.sample_at, Unset):
            sample_at = UNSET
        elif isinstance(self.sample_at, datetime.datetime):
            sample_at = self.sample_at.isoformat()
        else:
            sample_at = self.sample_at

        sample_source: None | str | Unset
        if isinstance(self.sample_source, Unset):
            sample_source = UNSET
        else:
            sample_source = self.sample_source


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if keys is not UNSET:
            field_dict["keys"] = keys
        if listen_until is not UNSET:
            field_dict["listenUntil"] = listen_until
        if listening is not UNSET:
            field_dict["listening"] = listening
        if sample is not UNSET:
            field_dict["sample"] = sample
        if sample_at is not UNSET:
            field_dict["sampleAt"] = sample_at
        if sample_source is not UNSET:
            field_dict["sampleSource"] = sample_source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_webhook_key_node import OfficeWebhookKeyNode # noqa: PLC0415
        d = dict(src_dict)
        def _parse_keys(data: object) -> list[OfficeWebhookKeyNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = []
                _keys_type_0 = data
                for keys_type_0_item_data in (_keys_type_0):
                    keys_type_0_item = OfficeWebhookKeyNode.from_dict(keys_type_0_item_data)



                    keys_type_0.append(keys_type_0_item)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeWebhookKeyNode] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))


        def _parse_listen_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listen_until_type_0 = datetime.datetime.fromisoformat(data)



                return listen_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        listen_until = _parse_listen_until(d.pop("listenUntil", UNSET))


        listening = d.pop("listening", UNSET)

        sample = d.pop("sample", UNSET)

        def _parse_sample_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sample_at_type_0 = datetime.datetime.fromisoformat(data)



                return sample_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sample_at = _parse_sample_at(d.pop("sampleAt", UNSET))


        def _parse_sample_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_source = _parse_sample_source(d.pop("sampleSource", UNSET))


        office_automation_webhook_sample_dto = cls(
            keys=keys,
            listen_until=listen_until,
            listening=listening,
            sample=sample,
            sample_at=sample_at,
            sample_source=sample_source,
        )

        return office_automation_webhook_sample_dto

