from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_bulk_error_dto import OfficeTaskBulkErrorDto





T = TypeVar("T", bound="OfficeTaskBulkResultDto")



@_attrs_define
class OfficeTaskBulkResultDto:
    

    applied: int | Unset = UNSET
    errors: list[OfficeTaskBulkErrorDto] | None | Unset = UNSET
    notified: int | Unset = UNSET
    skipped: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_bulk_error_dto import OfficeTaskBulkErrorDto # noqa: PLC0415
        applied = self.applied

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)


        else:
            errors = self.errors

        notified = self.notified

        skipped = self.skipped


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if applied is not UNSET:
            field_dict["applied"] = applied
        if errors is not UNSET:
            field_dict["errors"] = errors
        if notified is not UNSET:
            field_dict["notified"] = notified
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_bulk_error_dto import OfficeTaskBulkErrorDto # noqa: PLC0415
        d = dict(src_dict)
        applied = d.pop("applied", UNSET)

        def _parse_errors(data: object) -> list[OfficeTaskBulkErrorDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in (_errors_type_0):
                    errors_type_0_item = OfficeTaskBulkErrorDto.from_dict(errors_type_0_item_data)



                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskBulkErrorDto] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))


        notified = d.pop("notified", UNSET)

        skipped = d.pop("skipped", UNSET)

        office_task_bulk_result_dto = cls(
            applied=applied,
            errors=errors,
            notified=notified,
            skipped=skipped,
        )

        return office_task_bulk_result_dto

