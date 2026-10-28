from typing import Literal

OfficeOfficeDashboardWidgetKind = Literal['Money', 'Percentage', 'Stat']

OFFICE_OFFICE_DASHBOARD_WIDGET_KIND_VALUES: set[OfficeOfficeDashboardWidgetKind] = { 'Money', 'Percentage', 'Stat',  }

def check_office_office_dashboard_widget_kind(value: str) -> OfficeOfficeDashboardWidgetKind:
    if value in OFFICE_OFFICE_DASHBOARD_WIDGET_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_OFFICE_DASHBOARD_WIDGET_KIND_VALUES!r}")
