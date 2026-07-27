# VoltGuard System Architecture

## Overview

VoltGuard is an interactive Battery Management System simulator designed to model battery monitoring, protection, and control behaviour.

The system is divided into independent modules that communicate with each other.

---

# High-Level Architecture

```
                 User Interface
                      |
                      |
              Dashboard Layer
                      |
                      |
              BMS Controller
                      |
        --------------------------------
        |              |               |
        |              |               |
 Battery Model   Fault Manager   Data Logger
        |
        |
 Battery Cells
```

---

# System Modules

## 1. Battery Model

Responsible for simulating the physical behaviour of the battery.

Responsibilities:
- Cell voltage simulation
- Temperature changes
- State of Charge calculation
- Current flow simulation

---

## 2. BMS Controller

The main decision-making module.

Responsibilities:
- Monitor battery conditions
- Control charging/discharging
- Coordinate protection systems
- Manage battery states

---

## 3. Fault Manager

Responsible for detecting unsafe conditions.

Detects:
- Over-voltage
- Under-voltage
- Over-temperature
- Cell imbalance

Actions:
- Trigger warnings
- Stop charging
- Record faults

---

## 4. Data Logger

Records important system events.

Examples:
- Charging started
- Fault detected
- Battery protection activated

---

## 5. Dashboard Interface

Provides real-time visualization.

Displays:
- Battery health
- State of Charge
- Cell voltages
- Temperature
- Current
- Fault messages
- Live graphs