# Battery Model Design

## Overview

The Battery Model simulates the behaviour of a battery pack used by VoltGuard.

The battery pack consists of multiple individual cells whose conditions are continuously monitored.

---

# Battery Pack Structure

VoltGuard simulates a 4-cell lithium-ion battery pack.

Each cell contains:

- Voltage
- Temperature
- State of Charge (SOC)
- Health status

---

# Cell Parameters

## Voltage

Represents the electrical potential of the battery cell.

Typical lithium-ion range:

- Fully charged: ~4.2V
- Nominal: ~3.7V
- Empty: ~3.0V

---

## Temperature

Represents the operating temperature.

Used for safety monitoring.

Example:

Normal:
20-45°C

Warning:
45-60°C

Danger:
>60°C

---

## State of Charge (SOC)

Represents remaining battery capacity.

Range:

0% → Empty

100% → Fully charged

---

## Battery Health

Represents the overall condition of the battery.

Range:

0-100%

---

# Simulation Behaviour

During operation:

Charging:
- SOC increases
- Voltage increases
- Temperature slightly increases

Discharging:
- SOC decreases
- Voltage decreases

Fault conditions:
- Temperature may increase
- Cell voltage imbalance may occur

---

# Battery Model Responsibilities

The Battery Model will:

- Store battery parameters
- Update battery values over time
- Simulate charging behaviour
- Simulate discharging behaviour
- Provide data to the BMS Controller

# Battery Simulation Rules

## Charging Mode

When charging:

- State of Charge increases gradually
- Voltage increases gradually
- Temperature increases slightly

## Discharging Mode

When discharging:

- State of Charge decreases gradually
- Voltage decreases gradually
- Temperature changes based on current load

## Safety Limits

Voltage:
- Maximum: 4.2V
- Minimum: 3.0V

Temperature:
- Warning: 45°C
- Critical: 60°C