from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeApprovalsControllerAddNodeRequest")



@_attrs_define
class OfficeApprovalsControllerAddNodeRequest:
    

    activation_condition: None | str | Unset = UNSET
    allow_add_sign: bool | Unset = UNSET
    allow_transfer: bool | Unset = UNSET
    approver_config: None | str | Unset = UNSET
    approver_mode: None | str | Unset = UNSET
    due_hours: int | None | Unset = UNSET
    escalate_on_overdue: bool | Unset = UNSET
    join_mode: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    node_type: None | str | Unset = UNSET
    on_reject: None | str | Unset = UNSET
    position: int | Unset = UNSET
    return_to_node_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        activation_condition: None | str | Unset
        if isinstance(self.activation_condition, Unset):
            activation_condition = UNSET
        else:
            activation_condition = self.activation_condition

        allow_add_sign = self.allow_add_sign

        allow_transfer = self.allow_transfer

        approver_config: None | str | Unset
        if isinstance(self.approver_config, Unset):
            approver_config = UNSET
        else:
            approver_config = self.approver_config

        approver_mode: None | str | Unset
        if isinstance(self.approver_mode, Unset):
            approver_mode = UNSET
        else:
            approver_mode = self.approver_mode

        due_hours: int | None | Unset
        if isinstance(self.due_hours, Unset):
            due_hours = UNSET
        else:
            due_hours = self.due_hours

        escalate_on_overdue = self.escalate_on_overdue

        join_mode: None | str | Unset
        if isinstance(self.join_mode, Unset):
            join_mode = UNSET
        else:
            join_mode = self.join_mode

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        node_type: None | str | Unset
        if isinstance(self.node_type, Unset):
            node_type = UNSET
        else:
            node_type = self.node_type

        on_reject: None | str | Unset
        if isinstance(self.on_reject, Unset):
            on_reject = UNSET
        else:
            on_reject = self.on_reject

        position = self.position

        return_to_node_id: None | str | Unset
        if isinstance(self.return_to_node_id, Unset):
            return_to_node_id = UNSET
        elif isinstance(self.return_to_node_id, UUID):
            return_to_node_id = str(self.return_to_node_id)
        else:
            return_to_node_id = self.return_to_node_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activation_condition is not UNSET:
            field_dict["activationCondition"] = activation_condition
        if allow_add_sign is not UNSET:
            field_dict["allowAddSign"] = allow_add_sign
        if allow_transfer is not UNSET:
            field_dict["allowTransfer"] = allow_transfer
        if approver_config is not UNSET:
            field_dict["approverConfig"] = approver_config
        if approver_mode is not UNSET:
            field_dict["approverMode"] = approver_mode
        if due_hours is not UNSET:
            field_dict["dueHours"] = due_hours
        if escalate_on_overdue is not UNSET:
            field_dict["escalateOnOverdue"] = escalate_on_overdue
        if join_mode is not UNSET:
            field_dict["joinMode"] = join_mode
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if on_reject is not UNSET:
            field_dict["onReject"] = on_reject
        if position is not UNSET:
            field_dict["position"] = position
        if return_to_node_id is not UNSET:
            field_dict["returnToNodeId"] = return_to_node_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_activation_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_condition = _parse_activation_condition(d.pop("activationCondition", UNSET))


        allow_add_sign = d.pop("allowAddSign", UNSET)

        allow_transfer = d.pop("allowTransfer", UNSET)

        def _parse_approver_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approver_config = _parse_approver_config(d.pop("approverConfig", UNSET))


        def _parse_approver_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approver_mode = _parse_approver_mode(d.pop("approverMode", UNSET))


        def _parse_due_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        due_hours = _parse_due_hours(d.pop("dueHours", UNSET))


        escalate_on_overdue = d.pop("escalateOnOverdue", UNSET)

        def _parse_join_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        join_mode = _parse_join_mode(d.pop("joinMode", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_node_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_type = _parse_node_type(d.pop("nodeType", UNSET))


        def _parse_on_reject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_reject = _parse_on_reject(d.pop("onReject", UNSET))


        position = d.pop("position", UNSET)

        def _parse_return_to_node_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                return_to_node_id_type_0 = UUID(data)



                return return_to_node_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        return_to_node_id = _parse_return_to_node_id(d.pop("returnToNodeId", UNSET))


        office_approvals_controller_add_node_request = cls(
            activation_condition=activation_condition,
            allow_add_sign=allow_add_sign,
            allow_transfer=allow_transfer,
            approver_config=approver_config,
            approver_mode=approver_mode,
            due_hours=due_hours,
            escalate_on_overdue=escalate_on_overdue,
            join_mode=join_mode,
            name=name,
            node_type=node_type,
            on_reject=on_reject,
            position=position,
            return_to_node_id=return_to_node_id,
        )

        return office_approvals_controller_add_node_request

