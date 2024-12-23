"""Representation of BMD CLI parameters."""

import dataclasses


@dataclasses.dataclass
class BMDParam:
    """BMD CLI parameter.

    CLI paramters that don't require a value can be generated by
    setting only the parameter key (e.g. `/FINISH`).
    """

    key: str
    value: str | None = None

    def __str__(self) -> str:
        if self.value:
            return f"/{self.key}={self.value}"
        else:
            return f"/{self.key}"


def bmd_params_from_dict(d: dict[str, str]) -> list[BMDParam]:
    """Convert a dictionary to a list of BMD parameters."""
    return [BMDParam(key=k, value=v) for k, v in d.items()]
