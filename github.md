# CrewAI Meeting Minutes Project

## Overview
The CrewAI Meeting Minutes project is designed to summarize meeting transcripts, extract key action items, analyze sentiment, and generate structured meeting minutes in Markdown format. The system automates these tasks and writes the results to designated files.

## Features
- **Summarizes Meeting Transcripts**: Extracts key points from the meeting.
- **Identifies Action Items**: Lists tasks assigned during the meeting.
- **Performs Sentiment Analysis**: Analyzes the overall tone of the meeting.
- **Generates Structured Meeting Minutes**: Formats the meeting minutes in Markdown.
- **Drafts an Email with the Meeting Summary**: Creates a draft email containing the meeting minutes.

## Output Files
- `summary.txt`: Contains the summarized key points from the meeting.
- `action_items.txt`: Lists the action items identified during the meeting.
- `sentiment.txt`: Provides a sentiment analysis of the transcript.
- `meeting_minutes.md`: A well-structured markdown file containing the meeting minutes.

## Example Output

### **summary.txt**
```
FinTech Plus reported strong Q2 2023 results with $125 million in revenue, a 25% year-over-year increase. Gross profit margin was 58%, EBITDA reached $37.5 million, and net income rose to $16 million. The company expanded its product lines and investments, achieving a healthy debt-to-equity ratio of 1.5. Organic user growth improved with a 3.5x LTV-CAC ratio. Risk management remains robust with a 99% confidence level. The company forecasts $135 million in Q3 revenue, driven by blockchain and AI solutions. The upcoming IPO of PayPlus is expected to raise $200 million, enhancing liquidity for growth.
```

### **action_items.txt**
```
- Forecast Q3 revenue of $135 million
- Prepare for the IPO of PayPlus to raise $200 million
- Continue monitoring risk management and maintain healthy financial ratios
```

### **sentiment.txt**
```
The sentiment of the meeting transcript is generally positive. The discussion highlights strong financial performance, growth initiatives, and an optimistic outlook for the future. The tone is upbeat, with emphasis on achievements and positive projections, indicating confidence in the company's direction.
```

### **meeting_minutes.md**
```
# Meeting Minutes - TylerAI
**Date:** [Today's Date]  
**Company:** TylerAI  
**Organizer:** Tyler  
**Location:** Zoom  

---

## Attendees
- Tyler (Organizer)
- Alex Johnson (CFO)
- Samantha Lee (CTO)
- Michael Chen (Head of Risk Management)
- Emily Patel (Head of Product Development)
- David Kim (Investor Relations Officer)

---

## Agenda
1. Financial Performance Review (Q2 2023)
2. Product Expansion and Investments Update
3. Risk Management Overview
4. Q3 2023 Forecast and Projections
5. PayPlus IPO Preparation

---

## Discussion

### 1. Financial Performance Review (Q2 2023)
- **Revenue:** $125 million, representing a 25% year-over-year increase.
- **Gross Profit Margin:** 58%, showcasing strong profitability.
- **EBITDA:** $37.5 million, highlighting efficient operations.
- **Net Income:** $16 million, reflecting improved profitability.

### 2. Product Expansion and Investments Update
- Expanded product lines, contributing to revenue growth.
- Strategic investments in blockchain and AI solutions are paying off.
- Debt-to-equity ratio maintained at a healthy 1.5.

### 3. Risk Management Overview
- Robust risk management practices in place.
- 99% confidence level in managing potential risks.

### 4. Q3 2023 Forecast and Projections
- **Revenue Forecast:** $135 million, driven by growth in blockchain and AI solutions.
- Positive outlook for continued growth.

### 5. PayPlus IPO Preparation
- **Expected Raise:** $200 million, enhancing liquidity for future growth.
- IPO preparation is on track.

---

## Action Items
1. **Forecast Q3 Revenue:**  
   - **Responsible:** Alex Johnson (CFO)  
   - **Due Date:** [Specify Due Date]  

2. **Prepare for PayPlus IPO:**  
   - **Responsible:** David Kim (Investor Relations Officer)  
   - **Due Date:** [Specify Due Date]  

3. **Monitor Risk Management:**  
   - **Responsible:** Michael Chen (Head of Risk Management)  
   - **Due Date:** Ongoing  

---

## Closing Remarks
The meeting concluded on a positive note, with the team expressing confidence in the company's strong performance and future growth. Tyler thanked everyone for their contributions and emphasized the importance of maintaining momentum.

---

**Next Meeting:** [Specify Date and Time]  
**Adjourned:** [Specify Time]  

---

**Prepared by:** [Your Name]  
**Title:** Meeting Minutes Writer
```

## How to Run the Project
1. **Install Dependencies**:
   ```bash
   pip install crewai openai
   ```
2. **Run the CrewAI script**:
   ```bash
   python meeting_minutes.py
   ```
3. **Check the `meeting_minutes` directory** for the generated files.

## Conclusion
The CrewAI Meeting Minutes project automates the summarization, action item extraction, sentiment analysis, and formatting of meeting minutes, making it a valuable tool for efficiently documenting business discussions.

