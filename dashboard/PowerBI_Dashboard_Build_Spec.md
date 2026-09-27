# Power BI Dashboard Build Specification

## Data source
Use `../data/Production_Data.csv` as the fact table. Join to station metadata if desired, but all required station-level fields are already present.

## Core measures
- Planned Units = SUM(Planned Qty)
- Actual Units = SUM(Units Processed (units))
- Good Units = SUM(Good Units)
- Plan Attainment = DIVIDE([Actual Units],[Planned Units])
- Good Yield = DIVIDE([Good Units],[Actual Units])
- Unplanned Downtime = SUM(Unplanned Downtime (min))
- Defects = SUM(Defects)
- Availability = DIVIDE(SUM(Operating Time (min)),SUM(Planned Production Time (min)))
- Performance = DIVIDE(SUM(Ideal Cycle Time (sec))*[Actual Units],SUM(Operating Time (min))*60)
- Quality = DIVIDE([Good Units],[Actual Units])
- OEE = [Availability]*[Performance]*[Quality]

## Suggested visuals
1. KPI cards: Plan Attainment, Good Yield, OEE, Unplanned Downtime, Defects.
2. Clustered column: Avg Actual Cycle Time by Station; add a constant 100.8 sec takt reference line.
3. Pareto: Unplanned Downtime by Main Downtime Reason.
4. Pareto: Defects by Defect Mode.
5. Line chart: Daily Plan vs Actual at S10 / Functional Test.
6. Slicer: Date, Shift, Station, Main Downtime Reason, Defect Mode.

## Dashboard story
Current-state diagnosis -> bottleneck -> loss buckets -> quality drivers -> improvement priorities.

**Note:** The source data are synthetic/simulated and do not represent Ather factory data.
