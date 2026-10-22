## **Individual Contribution Report - Nguyễn Khánh Linh**

### **1\. My Main Responsibility**

- **Economic model**: Responsible for data filtering and regression testing (for interbank rate formula), refining macroeconomic formulas and coefficients to clarify monetary policy transmission from the money market to the broader economy, and developing game processes for backend (60%).
- **Learning card**: Designed learning cards to explain key economic concepts.
- **Backend testing**: Tested decision outcomes, checking whether the implemented rules produced results consistent with the intended logic and identifying areas requiring revision.
- **Frontend support and API integration**: Assisted with frontend implementation and implemented API integration to connect the backend and the frontend.

### **2\. My Concrete Outputs**

- **Economic model**: w4_financial_logic.md
- **Learning card**: learning_card.md
- **Backend testing**: test_engine_v2.py
- **Frontend support**: omo_refactored_v64.html
- **API integration**: app.py

### **3\. Evidence Links**

- **Economic model**: [Regression](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797); [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true); [w4_financial_logic.md](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md)
- **Learning card**: [learning_card.md](https://github.com/FTU-Legacy-63/G03/blob/main/learning_card.md)
- **Backend testing**: [test_engine_v2.py](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_engine_v2.py)
- **Frontend support and API integration**: [app.py](https://github.com/FTU-Legacy-63/G03/blob/main/WEEK%206/app.py)

### **4\. How My Work Is Used**

- **Economic model**: Connects the player's decisions with auction outcomes, estimated interbank interest rates and its consequences on GDP growth and inflation. The formulas and parameter choices also make the transmission from the money market to the broader economy more explicit.
- **Learning card**: Helps players interpret the underlying concepts, improving learning experience.
- **Backend testing**: Checks whether the implemented rules and simulation outcomes are consistent with the intended logic across different decisions and liquidity conditions.
- **Frontend support and API integration**: Connects the user interface with the backend through API, enabling players’ actions to be processed and simulation results to be displayed in the game.

### **5\. Integration, Testing and Revision**

- **Economic model**: Integrated the interbank rate regression and revised macroeconomic formulas and coefficients in coordination with the backend implementation. Checked the consistency between regression outputs, and implemented calculations.
- **Learning cards**: Integrated learning cards into the game interface to explain key economic concepts in context, supporting players in understanding the economic rationale behind their decisions.
- **Backend testing**: Tested the game under different liquidity conditions and player decisions to check whether the implemented rules produced outcomes consistent with the intended economic logic.
- **Frontend support and API integration**: Connected the backend and frontend through Flask APIs and supported the integration of backend results into the game interface. Reviewed the data flow and displayed results during testing and made adjustments where needed to improve consistency between backend calculations and frontend presentation.

### **6\. Remaining Limitation**

A key limitation is that the economic model is not yet fully empirically validated. Although formula research, historical data collection and regression analysis informed its development, some relationships rely on economic intuition, and some formulas and coefficients were adjusted to make the intended transmission mechanism more visible. 
Consequently, the model is better understood as a simplified educational simulation than as a validated tool for forecasting actual macroeconomic outcomes.

  Although historical data, regression analysis, and economic research informed its development, some relationships and coefficients were adjusted to make the intended monetary policy transmission mechanism more visible in the simulation. 

  The model has not yet been fully empirically validated, so its outcomes should be interpreted as educational illustrations rather than precise forecasts of actual macroeconomic developments.

