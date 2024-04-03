from enum import Enum


class AbsenceReasonEnum(Enum):
    """Enum para los motivos de ausencia."""

    ILLNESS = "ILLNESS"
    PERSONAL_MATTER = "PERSONAL MATTER"
    MEDICAL_APPOINTMENT = "MEDICAL APPOINTMENT"
    RAINY_DAY = "RAINY DAY"
    OTHER = "OTHER"
