## Critique of "Daily new confirmed COVID-19 cases per million people" 

![](image.png)

**Figure:** Rolling 7-day average of daily COVID-19 cases per million

**Objective:** Evaluate the chart using the checklist for good graphics and suggest improvements


### 1. Analysis Based on the Checklist

The chart is a line plot which is appropriate for time-series data but it has several issues:

| Section | Checklist Item | Verdict | Comments |
| :--- | :--- | :--- | :--- |
| **Data** | Type of graphic fits the data| Good | Line chart is suitable for time-series. |
| **Data** | Confidence intervals visualized | **Fail** | No error bars or indication of variability. This is important because the subtitle notes cases are limited by testing. |
| **Graphical objects** | Scales and units are explicit | **Fail** | The Y-axis is non-linear and unlabelled as such The spacing between 30-50 and 90-200 is inconsistent, exaggerating differences in low-value regions |
| **Annotations** | Axis labels clear and self-contained | **Fail** | Y-axis labels are misleading due to non-linear scaling |
| **Annotations** | Origin at 0 or jusified if not | **Fail** | Y-axis does not start at 0, which exaggerates differences in lower case numbers |
| **Information** | If showing averages error bars included. | **Fail** | Rolling averages are shown, but no error bars provided. |
| **Overall** | Elegant and truthful representation | **Fail** | Non-linear unlabelled Y-axis distorts the data and misrepresents relative trends. |

**Additional Observations:**


The UK line jumps above 200, Germany appears under 100, but the uneven scale exaggerates the gap
7-day rolling average smooths spikes, hiding real variability
Colors alone distinguish curves, which may be hard to interpret in black & white prints.
No X-axis grid lines making it harder to compare dates
The chart seems to deliberately highlight small fluctuations during large increases or drops in cases, adding visual bias

### 3. Recommendations

#### a) Fix the Y-axis

- Make it **linear** and start at 0.
- Tick marks: 0, 50, 100, 150, 200, 250.
- Avoid exaggerating small fluctuations.

#### b) Show Variability

- Add **semi-transparent error bands** (e.g., SD or 95% CI) around each line.
- Helps viewers understand reliability of the rolling average.

#### c) Improve Readability

- Clearly label Y-axis as **"Linear scale"**.
- Add legend: UK (orange), Germany (dashed purple).
- Different line styles help B/W printing.
- Optional: add grid lines for easier comparison.

### 4. Suggested Chart Concept

This graphic has fewer types of issues than the previous one, but the ones it has are quite serious.  

No confidence intervals are shown, so it's hard to judge how precise or reproducible the data really is.  
The Y-axis is a mess: it doesn't follow a consistent spacing, jumps between 30–100 and 100–200 are uneven, and it doesn't even start at 0 despite values below 30. The chart even breaks out of its own frame.  
There are no grid lines for the X-axis, making date comparisons difficult.  
The chart seems biased: small inconsistencies appear to be used to highlight variance during big increases or drops, and it looks zoomed in at the end to exaggerate differences between countries that are actually minor compared to previous months.  