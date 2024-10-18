from dataclasses import dataclass


@dataclass
class Transistor:
    overdrive_voltage: float = None
    current: float = None
    current_with_channel_length_mod: float = None
    output_resistance: float = None
    width: float = None
    length: float = None
    early_voltage: float = None
    threshold_voltage: float = None

    def __init__(
        self,
        overdrive_voltage=None,
        current=None,
        current_with_channel_length_mod=None,
        output_resistance=None,
        width=None,
        length=None,
        early_voltage=None,
        threshold_voltage=None,
    ):
        self.overdrive_voltage = overdrive_voltage
        self.current = current
        self.current_with_channel_length_mod = current_with_channel_length_mod
        self.output_resistance = output_resistance
        self.width = width
        self.length = length
        self.early_voltage = early_voltage
        self.threshold_voltage = threshold_voltage


@dataclass
class NMOS(Transistor):
    voltage_gate_source: float = None
    voltage_drain_source: float = None
    voltage_gate_drain: float = None
    transconductance_parameter: float = None

    def __init__(self, voltage_gate_source=None, voltage_drain_source=None, voltage_gate_drain=None, transconductance_parameter=None, **kwargs):
        super().__init__(**kwargs)
        self.voltage_gate_source = voltage_gate_source
        self.voltage_drain_source = voltage_drain_source
        self.voltage_gate_drain = voltage_gate_drain
        self.transconductance_parameter = transconductance_parameter


@dataclass
class PMOS(Transistor):
    voltage_source_gate: float = None
    voltage_source_drain: float = None
    voltage_drain_gate: float = None
    transconductance_parameter: float = None

    def __init__(self, voltage_source_gate=None, voltage_source_drain=None, voltage_drain_gate=None, transconductance_parameter=None, **kwargs):
        super().__init__(**kwargs)
        self.voltage_source_gate = voltage_source_gate
        self.voltage_source_drain = voltage_source_drain
        self.voltage_drain_gate = voltage_drain_gate
        self.transconductance_parameter = transconductance_parameter


def current_equation_solve_for_width(Q: Transistor):
    return 2 * Q.current * Q.length / (Q.transconductance_parameter * Q.overdrive_voltage**2)


def current_equation_with_channel_lenght_modulation_solve_for_width(Q: Transistor):
    if isinstance(Q, PMOS):
        return 2 * Q.current * Q.length / (Q.transconductance_parameter * (Q.overdrive_voltage**2) * (1 + Q.voltage_source_drain / Q.early_voltage))
    else:
        return 2 * Q.current * Q.length / (Q.transconductance_parameter * (Q.overdrive_voltage**2) * (1 + Q.voltage_drain_source / Q.early_voltage))
