# EV Assembly Line Optimization using Lean, OEE & Bottleneck Analysis

> **Portfolio / academic project using realistic synthetic manufacturing data**
>
> This project simulates an EV scooter assembly line and applies Lean Manufacturing, OEE, Takt Time, line-balance, loss analysis, RCA, PFMEA and a future-state improvement model to understand why final output falls below plan.
>
> **Important:** The dataset and analysis are simulated for portfolio/academic use. They do **not** represent Ather Energy's proprietary factory data, internal KPIs, processes or actual performance.

---

## 1. Project Overview

### Business problem

An EV assembly line is consistently producing below its planned daily output. Management needs a structured way to answer:

- Which station is constraining line capacity?
- How does actual cycle time compare with takt time?
- Where are the largest downtime and quality losses?
- Which losses are operationally actionable?
- What improvement actions should be tested first?
- What is the expected capacity effect of those actions?

### Objective

Build a data-driven manufacturing improvement model that connects:

**Production data → KPI calculation → Bottleneck identification → Loss analysis → Root-cause hypotheses → PFMEA / control actions → Future-state scenario → Management dashboard**

The project is designed to demonstrate practical manufacturing-operations skills relevant to assembly, Lean, throughput, quality, capacity and visual performance management.

---

## 2. Assembly-Line Model

The simulated line contains **10 assembly / verification stations**:

| Station | Process |
|---|---|
| S01 | Frame Prep |
| S02 | Motor Install |
| S03 | Battery Install |
| S04 | Controller & Wiring |
| S05 | Wheel & Brake |
| S06 | Body Panels |
| S07 | Seat & Finishing |
| S08 | Software / ECU Check |
| S09 | Final Inspection |
| S10 | Functional Test |

The model intentionally gives each station different work content, cycle-time characteristics and loss exposure. This is important because a realistic production system should **not** make every station behave identically.

### Production reference

- Production days: **30**
- Shifts: **2 shifts/day**
- Simulated station-shift records: **600**
- Reference daily demand: **500 units/day**
- Reference takt time: **100.8 sec/unit**

---

## 3. Dataset Design

The project uses a station-shift level dataset with operational variation across:

- planned production
- actual units processed
- planned downtime / changeover
- breakdowns
- material waiting
- quality holds
- minor stops
- tool changes
- operator availability
- waiting time
- cycle time
- good units
- defects
- rework
- manpower
- downtime reason
- defect mode

The data is deliberately **unbalanced and correlated around plausible operational patterns**. For example:

- S05 carries the strongest cycle-time / tooling constraint signal.
- S03 has more material-related loss exposure.
- S04 has higher wiring/rework quality exposure.
- Downstream stations can show lower OEE because they are affected by starvation from an upstream constraint.

This structure is intended to support diagnosis rather than make every station equally problematic.

---

## 4. Key KPIs

### Takt Time

```text
Takt Time = Available Production Time / Customer Demand
```

### Availability

```text
Availability = Operating Time / Planned Production Time
```

### Performance

```text
Performance = (Ideal Cycle Time × Total Units) / Operating Time
```

### Quality

```text
Quality = Good Units / Total Units
```

### OEE

```text
OEE = Availability × Performance × Quality
```

### Plan Attainment

```text
Plan Attainment = Actual Output / Planned Output
```

### Cycle-Time Gap

```text
Cycle-Time Gap = Actual Cycle Time − Takt Time
```

These metrics are used together rather than in isolation. A station can have acceptable availability but still constrain throughput because of cycle time or performance.

---

## 5. Analytical Approach

The analysis follows a practical manufacturing-improvement sequence.

### Step 1 — Establish the baseline

Calculate line and station KPIs from the raw production data.

### Step 2 — Compare cycle time with takt

Identify stations where actual cycle time is above the reference takt.

### Step 3 — Identify the constraint

Use station-level cycle time, output and loss patterns to identify the primary line constraint.

### Step 4 — Quantify losses

Break unplanned downtime into categories and analyze their contribution. Perform the same exercise for defect modes.

### Step 5 — Root-cause hypothesis

Use a **5-Why analysis** to connect the S05 cycle-time problem with tooling variability, fitment/alignment, adjustment/rework and the need for stronger process controls.

> The 5-Why sheet is a portfolio-level hypothesis framework. In a real factory, each hypothesis would need to be verified at the Gemba using time studies, observations, quality records and operator input.

### Step 6 — PFMEA / control actions

Use an illustrative PFMEA for S05 to connect failure modes with severity, occurrence, detection, RPN, current controls and recommended countermeasures.

### Step 7 — Model a future state

Test explicit improvement assumptions such as:

- cycle-time reduction through line balancing and fixture/tool improvement
- reduced S05 unplanned downtime through quick-change / preventive actions
- reduced material-shortage loss through kitting / replenishment controls
- reduced wiring defects through standard work and poka-yoke

The future-state model is a **scenario**, not a claim of actual factory improvement.

---

## 6. Baseline Findings

The current-state model indicates:

- **Final plan attainment: ~74.6%**
- **Final S10 OEE: ~69.0%**
- **Final good yield: ~97.1%**
- **S05 average actual cycle time: ~117.5 sec**
- **Reference takt time: 100.8 sec**

The model therefore identifies **S05 Wheel & Brake** as the primary cycle-time constraint in the simulated line.

### Loss structure

The dataset contains meaningful but unequal loss contributions. Examples include:

- **Material shortage:** largest single unplanned-downtime category at the dataset level.
- **Fitment / alignment:** largest defect mode.
- **Wiring / connector:** second-largest defect mode.

These patterns are used to prioritize improvement discussions, not to represent actual Ather factory loss percentages.

---

## 7. Root-Cause & Process-Control Work

### S05 Wheel & Brake — problem statement

> Average actual cycle time is above the reference takt, constraining simulated line capacity.

### Key 5-Why logic

1. **Why is S05 a constraint?**
   - Average actual cycle time is ~117.5 sec vs. 100.8 sec takt.
2. **Why is cycle time high?**
   - Manual alignment and tool handling are plausible contributors to variation and adjustment time.
3. **Why does variation persist?**
   - Tool-change and rework / clearance losses extend station time.
4. **Why can defects create extra work?**
   - Fitment / alignment is the largest defect mode in the model.
5. **Why is the issue not fully prevented?**
   - Stronger visual CT/OEE review, fixture controls and escalation mechanisms can help close the feedback loop.

### Illustrative S05 PFMEA

High-RPN examples in the model include:

- wheel misalignment
- brake torque out of specification
- caliper position error
- fastener missing / loose
- tool-change delay
- repeated adjustment / rework

Suggested controls include:

- fixture locators
- poka-yoke
- torque verification
- go/no-go controls
- kitting / presence controls
- standard work
- first-piece checks

---

## 8. Future-State Improvement Scenario

The modeled first improvement wave targets the current constraint and selected loss contributors.

| Metric | Current | Modeled Future State | Basis |
|---|---:|---:|---|
| S05 Avg Actual CT | ~117.5 sec | ~99.5 sec | Line balancing + fixture/tool improvement |
| S05 Unplanned Downtime | 961 min | ~721 min | 25% reduction assumption |
| S03 Material Shortage DT | 517 min | ~310 min | 40% reduction assumption |
| S04 Defects | 461 units | ~323 units | 30% reduction assumption |

The modeled S05 cycle time moves just below takt, after which **S04 becomes the next tight capacity constraint** in the scenario.

This demonstrates an important operations principle: **removing one constraint can expose the next constraint.**

The future-state numbers are scenario outputs and should be validated through pilot production before being treated as real performance commitments.

---

## 9. Dashboard

The project includes a management-style dashboard covering:

- Reference takt
- Final plan attainment
- Final good yield
- Final S10 OEE
- Station cycle time vs. takt
- Daily plan vs. actual
- OEE components
- Downtime loss structure
- Defect structure
- Capacity scenario

The workbook also includes the analysis layers behind the dashboard so the KPI story can be traced back to the source data.

---

## 10. Project Files

```text
Ather_EV_Assembly_Optimization_Project_Package/
│
├── README.md
├── MANIFEST.txt
│
├── data/
│   ├── Production_Data.csv
│   ├── Ather_EV_Assembly_Optimization_Project.xlsx
│   └── Ather_EV_Assembly_Realistic_Synthetic_Dataset.xlsx
│
├── analysis/
│   ├── Ather_EV_Assembly_Analysis.py
│   ├── metrics.json
│   └── S05_Control_Plan.csv
│
├── dashboard/
│   └── PowerBI_Dashboard_Build_Spec.md
│
├── report/
│   ├── Ather_EV_Assembly_Optimization_Report.pdf
│   └── Ather_EV_Assembly_Optimization_Report.docx
│
├── charts/
│   ├── 01_cycle_time_vs_takt.png
│   ├── 02_oee_components_s10.png
│   ├── 03_downtime_pareto.png
│   ├── 04_defect_pareto.png
│   ├── 05_daily_plan_vs_actual.png
│   ├── 06_capacity_scenario.png
│   └── 07_process_flow.png
│
└── presentation/
    └── Ather_EV_Assembly_Optimization_Presentation.pptx
```

---

## 11. How to Use the Project

### Excel

Open:

```text
Ather_EV_Assembly_Optimization_Project.xlsx
```

Recommended flow:

```text
Production_Data
      ↓
Daily_Summary / Station_Summary
      ↓
Line Balance / OEE / Loss Analysis
      ↓
RCA / PFMEA
      ↓
Improvement Model
      ↓
Dashboard
```

### Python

The analysis script is intended for reproducibility and quick KPI validation.

Example:

```bash
python analysis/Ather_EV_Assembly_Analysis.py
```

### Power BI

Use the provided dashboard build specification to reproduce the management dashboard using the CSV/Excel source data.

---

## 12. Skills Demonstrated

### Manufacturing / Operations

- Lean Manufacturing
- OEE
- Takt Time
- Cycle-Time Analysis
- Line Balancing
- Throughput Analysis
- Plan vs. Actual
- Capacity Thinking
- Downtime Analysis
- Quality Loss Analysis
- Poka-Yoke
- PFMEA
- Root-Cause Analysis

### Analytics / Tools

- Advanced Excel
- Python
- Power BI
- Data Cleaning
- KPI Modeling
- Dashboard Design
- Visual Management

---

## 13. Portfolio Positioning

This project is best presented as a **manufacturing operations / operational excellence case study** rather than as an Ather factory case.

### One-line summary

> **Analyzed a 10-station simulated EV assembly line using Lean, OEE and takt-time analysis to identify a primary cycle-time constraint, quantify operational losses, develop process-control actions, and model a future-state capacity improvement scenario.**

### Resume-ready project title

**EV Assembly Line Optimization using Lean, OEE & Bottleneck Analysis**

---

## 14. Data & Modeling Disclaimer

This is a **realistic synthetic dataset** created specifically for an academic / portfolio case study.

- It is not collected from Ather Energy.
- It is not an internal Ather dataset.
- The PFMEA is illustrative and not an audited factory PFMEA.
- Root-cause statements are hypotheses intended for verification at the Gemba.
- Future-state results are scenario calculations based on explicit assumptions.

The project is designed to demonstrate the **method and analytical thinking**, not to claim proprietary operational results.

---

## 15. Suggested Interview Narrative

A strong way to explain the project is:

> “I modeled an EV assembly line and started with plan-vs-actual and OEE rather than jumping directly to a dashboard. I compared station cycle times with takt, identified S05 Wheel & Brake as the primary constraint, analyzed downtime and quality losses, built a 5-Why and illustrative PFMEA around the constraint, and then modeled a future state where the constraint is relieved and the next capacity constraint becomes visible. The dataset is synthetic, so the value of the project is the end-to-end problem-solving approach.”

---

## 16. License / Usage

Use freely for **academic, portfolio and interview demonstration purposes**. Do not present the synthetic data as real company data.
