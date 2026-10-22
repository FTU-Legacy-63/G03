## **Individual Contribution Report – Vũ Lưu Minh Ngọc**

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

- **Economic model**: [Regression.xlsx](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797); [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true); [WEEK 4](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md)
- **Learning card**: LINK GITHUB LEARNING CARD
- **Backend testing**: LINK GITHUB BACKEND TEST
- **Frontend support and API integration**: LINK GITHUB API

### **4\. How My Work Is Used**

- **Group coordination:** My coordination work helps maintain a clear division of responsibilities and ensures that the backend, economic model, testing, and frontend components develop consistently. By tracking progress, giving feedback, and conducting final checks, I help identify inconsistencies between components and facilitate revisions before the final product is delivered.  
- **Backend system and testing:** The backend file helps process relevant inputs, applies financial calculations and economic rules, and generates simulation results based on the player's decisions. The testing sessions help verify the readiness of the file for connecting with the frontend.  
- **Economic model:** The economic model provides the analytical foundation for the game's monetary policy simulation. The interbank regression and financial formulas help estimate how changes in liquidity conditions and monetary policy decisions may affect interbank interest rates. These simulated interest rate changes are then connected to broader macroeconomic outcomes, particularly GDP growth and inflation. This allows players to explore the possible consequences of their decisions and understand the transmission mechanism from money-market conditions to the wider economy.  
- **Frontend support:** Improves the interface's visual appeal and makes the game more engaging for users.

### **5\. Integration, Testing and Revision**

- **Group Coordination:** Coordinated task allocation, communication, and feedback across team members. Reviewed the feedback and integrated it in the backend, economic model, and frontend, and followed up on necessary revisions during the final checks**.**

- **Backend development and testing:** Integrated the economic model, financial formulas, and game rules into the backend file, which will be connected to the frontend by API file. Members tested the backend against the relevant game scenarios and gave feedback. Suitable adjustments will be implemented into the file to ensure consistency with the economic model.

- **Economic Model:** Integrated the finalized interbank regression into the economic model, which will be integrated into the backend. Team members  checked the consistency between model assumptions, regression outputs, and implemented calculations through Logic Test 2.0 and Logic Test 3.0, then revisions and adjustments will be done where necessary. 

- **Frontend Support:** Contributed to the background, top-bar and overall design and coordinated their integration with the game interface. Reviewed the visual presentation and refined the components based on feedback.

**6\. Remaining Limitation**

  A key limitation is that the economic model remains a simplified representation of real-world economic relationships. 

  Although historical data, regression analysis, and economic research informed its development, some relationships and coefficients were adjusted to make the intended monetary policy transmission mechanism more visible in the simulation. 

  The model has not yet been fully empirically validated, so its outcomes should be interpreted as educational illustrations rather than precise forecasts of actual macroeconomic developments.

