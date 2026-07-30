import streamlit as st
import pandas as pd
import os
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="VoltGuard",
    layout="wide"
)
st_autorefresh(
    interval=3000,
    key="soc_refresh"
)

st.markdown(
"""
<div class="brand-header">

<h1>
VoltGuard
</h1>

<p>
Intelligent Battery Management System
</p>

<p>
EV Battery Monitoring • Protection • Balancing
</p>

</div>
""",
unsafe_allow_html=True
)


# Load custom styling

css_path = os.path.join(
    os.path.dirname(__file__),
    "style.css"
)

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
    


# Load telemetry data
data_path = os.path.join(
    os.path.dirname(__file__),
    "../data/telemetry.csv"
)

data = pd.read_csv(data_path)

if "test_mode" not in st.session_state:
    st.session_state.test_mode = "normal"


if st.session_state.test_mode == "temperature":

    data.loc[3, "Temperature"] = 85


elif st.session_state.test_mode == "voltage":

    data.loc[2, "Voltage"] = 4.35


elif st.session_state.test_mode == "imbalance":

    data.loc[3, "Voltage"] = 4.10
    data.loc[0, "Voltage"] = 3.40

# Dynamic SOC simulation

if "current_soc" not in st.session_state:
    st.session_state.current_soc = data["SOC"].mean()


if "mode" not in st.session_state:
    st.session_state.mode = "Charging"



# Update SOC based on operating mode

if st.session_state.mode == "Charging":

    st.session_state.current_soc += 0.1


elif st.session_state.mode == "Discharging":

    st.session_state.current_soc -= 0.1


# Keep SOC between 0 and 100

st.session_state.current_soc = max(
    0,
    min(100, st.session_state.current_soc)
)
# Calculate battery statistics

average_soc = st.session_state.current_soc
average_voltage = data["Voltage"].mean()

average_temperature = data["Temperature"].mean()

# Dynamic current and power simulation

if st.session_state.mode == "Charging":

    current = 25
    power_flow = (average_voltage * len(data) * current) / 1000


elif st.session_state.mode == "Discharging":

    current = -18
    power_flow = (average_voltage * len(data) * current) / 1000


else:

    current = 0
    power_flow = 0

# Pack calculations

highest_voltage = data["Voltage"].max()

lowest_voltage = data["Voltage"].min()

voltage_difference = highest_voltage - lowest_voltage


highest_cell = data.loc[data["Voltage"].idxmax(), "Cell"]

lowest_cell = data.loc[data["Voltage"].idxmin(), "Cell"]


pack_voltage = average_voltage * len(data)


estimated_energy = pack_voltage * 2.5
# Load BMS status

status_file = os.path.join(
    os.path.dirname(__file__),
    "../data/status.txt"
)


if os.path.exists(status_file):

    with open(status_file, "r") as file:
        system_status = file.read()

else:

    system_status = "NO STATUS AVAILABLE"

st.caption(
f"Operating Mode: {st.session_state.mode}"
)

st.markdown(
f"""
<div class="status-card">

<h3>
Operating Mode: {st.session_state.mode}
</h3>

</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="section-title">
OPERATING MODE
</div>
""",
unsafe_allow_html=True
)


mode1, mode2, mode3 = st.columns(3)


with mode1:

    if st.button(" Charging"):
        st.session_state.mode = "Charging"


with mode2:

    if st.button(" Discharging"):
        st.session_state.mode = "Discharging"


with mode3:

    if st.button("⏸ Idle"):
        st.session_state.mode = "Idle"
# Battery Overview

st.markdown(
"""
<div class="section-title">
BATTERY PACK OVERVIEW
</div>
""",
unsafe_allow_html=True
)
# Battery Visualization

st.markdown(
f"""
<div class="battery-container">

<div class="battery-body">

<div class="battery-level" style="width:{average_soc}%;">
</div>

</div>

<div class="battery-tip">
</div>

</div>
""",
unsafe_allow_html=True
)


col1, col2, col3, col4, col5, col6 = st.columns(6)


with col1:

    st.markdown(
    f"""
    <div class="card">

    <h3>STATE OF CHARGE</h3>

    <div class="big-number">
    {average_soc:.1f}%
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    f"""
    <div class="card">

    <h3>TEMPERATURE</h3>

    <div class="big-number">
    {average_temperature:.1f}°C
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )



with col3:

    st.markdown(
    """
    <div class="card">

    <h3>BATTERY HEALTH</h3>

    <div class="big-number">
    98%
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
with col4:

    st.markdown(
    f"""
    <div class="card">

    <h3>PACK VOLTAGE</h3>

    <div class="big-number">
    {average_voltage*4:.2f}V
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
with col5:

    st.markdown(
    f"""
    <div class="card">

    <h3>CURRENT</h3>

    <div class="big-number">
    {current:.1f} A
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )


with col6:

    st.markdown(
    f"""
    <div class="card">

    <h3>POWER FLOW</h3>

    <div class="big-number">
    {power_flow:.2f} kW
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

# BMS Test Mode

st.markdown(
"""
<div class="section-title">
BMS TEST SIMULATION
</div>
""",
unsafe_allow_html=True
)


if "test_mode" not in st.session_state:
    st.session_state.test_mode = "normal"

st.write("")
col1, col2, col3, col4 = st.columns(4)


with col1:

    if st.button("Normal Operation"):
        st.session_state.test_mode = "normal"


with col2:

    if st.button("Inject Over Temperature"):
        st.session_state.test_mode = "temperature"


with col3:

    if st.button("Inject Over Voltage"):
        st.session_state.test_mode = "voltage"


with col4:

    if st.button("Create Imbalance"):
        st.session_state.test_mode = "imbalance"

if st.button("Reset System"):

    st.session_state.test_mode = "normal"

    st.rerun()
# Cell Monitoring

st.markdown(
"""
<div class="section-title">
CELL ARRAY STATUS
</div>
""",
unsafe_allow_html=True
)


cell_columns = st.columns(4)


for index, row in data.iterrows():

    with cell_columns[index]:
        voltage = row["Voltage"]

        temperature = row["Temperature"]


        if temperature >= 60 or voltage >= 4.2 or voltage <= 3.0:

            status = "CRITICAL"

            status_class = "critical"


        elif temperature >= 45 or abs(voltage - average_voltage) > 0.05:

            status = "WARNING"

            status_class = "warning"


        else:

            status = "NORMAL"

            status_class = "normal"
        st.markdown(
        f"""
        <div class="cell-card">

        <h3>CELL {int(row['Cell'])}</h3>

        <div class="cell-voltage">
        {row['Voltage']} V
        </div>

        <p>
        Temperature: {row['Temperature']} °C
        </p>

        <p class="{status_class}">
        ● {status}
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )
    # Battery Pack Health Summary

st.markdown(
"""
<div class="section-title">
BATTERY PACK HEALTH SUMMARY
</div>
""",
unsafe_allow_html=True
)


summary1, summary2, summary3, summary4 = st.columns(4)


with summary1:

    st.metric(
        "Highest Cell",
        f"Cell {int(highest_cell)}"
    )


with summary2:

    st.metric(
        "Lowest Cell",
        f"Cell {int(lowest_cell)}"
    )


with summary3:

    st.metric(
        "Voltage Spread",
        f"{voltage_difference:.3f} V"
    )


with summary4:

    st.metric(
        "Pack Voltage",
        f"{average_voltage*4:.2f} V"
    )


# System Status

st.markdown(
"""
<div class="section-title">
SYSTEM INTELLIGENCE
</div>
""",
unsafe_allow_html=True
)


st.markdown(
f"""
<div class="status-card">

<h2>{system_status}</h2>

<p>
Operating Mode: CHARGING
</p>

<p>
Cell Balancing: MONITORED BY BMS
</p>

<p>
Fault Detection: ACTIVE
</p>

</div>
""",
unsafe_allow_html=True
)
# Live Telemetry Graphs

st.markdown(
"""
<div class="section-title">
LIVE BATTERY TELEMETRY
</div>
""",
unsafe_allow_html=True
)


graph_col1, graph_col2 = st.columns(2)


with graph_col1:

    st.subheader("Cell Voltage")

    voltage_chart = data[["Voltage"]]

    st.line_chart(voltage_chart)



with graph_col2:

    st.subheader("Temperature")

    temperature_chart = data[["Temperature"]]

    st.line_chart(temperature_chart)
# Fault Monitoring Console


st.markdown(
"""
<div class="section-title">
FAULT MONITORING
</div>
""",
unsafe_allow_html=True
)


# Check the current telemetry for faults

fault_detected = False

for index, row in data.iterrows():

    if (
        row["Temperature"] >= 60
        or row["Voltage"] >= 4.2
        or row["Voltage"] <= 3.0
    ):

        fault_detected = True
        break


if fault_detected:

    fault_status = "FAULT DETECTED"
    status_icon = "🔴"

else:

    fault_status = "NO CRITICAL FAULTS"
    status_icon = "🟢"

st.markdown(
f"""
<div class="fault-summary">

<h2>
{status_icon} {fault_status}
</h2>

<p>
Battery protection systems are active.
</p>

</div>
""",
unsafe_allow_html=True
)



st.markdown(
"""
<div class="section-title">
CELL SAFETY CHECK
</div>
""",
unsafe_allow_html=True
)


for index, row in data.iterrows():

    voltage = row["Voltage"]
    temperature = row["Temperature"]


    # Voltage status

    if voltage >= 4.2:

        voltage_status = "🔴 Over Voltage"

    elif voltage <= 3.0:

        voltage_status = "🔴 Under Voltage"

    else:

        voltage_status = "✓ Normal"



    # Temperature status

    if temperature >= 60:

        temperature_status = "🔴 Critical Temperature"

    elif temperature >= 45:

        temperature_status = "🟡 High Temperature"

    else:

        temperature_status = "✓ Normal"



    st.markdown(
    f"""
    <div class="cell-check">

    <h3>
    Cell {int(row['Cell'])}
    </h3>

    <p>
    Voltage: {voltage:.2f} V → {voltage_status}
    </p>

    <p>
    Temperature: {temperature:.2f} °C → {temperature_status}
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )
