## **Individual Contribution Report – Vũ Lưu Minh Ngọc**

### **1\. My Main Responsibility**

- **Group coordination:** I was responsible for allocating tasks, coordinating communication between team members, tracking development progress, giving and collecting feedback throughout the project. I also helped ensure that individual contributions were aligned with the overall project objectives.   
- **Backend development:** I developed the main backend file, which serves as the core implementation of the game's economic and simulation logic. My responsibility was to integrate the economic model into a unified backend system. This involved translating the team's economic assumptions and calculation methods into executable logic so that player decisions could generate corresponding simulation outcomes.  
- **Economic model:** I contributed to finalizing the interbank interest rate regression and related financial formulas, testing the game logic, and developing the 40% of game process for backend implementation . I worked on connecting liquidity conditions and monetary policy decisions with the simulated interbank interest rate. I also helped review the consistency between the regression results, economic assumptions, and the rules implemented in the game.  
* **Frontend support (5%):** Contributed to improving the interface design and visual presentation.

### **2\. My Concrete Outputs**

- **Group coordination:** [LINK GAME](https://who-runs-the-world-xajm.onrender.com/?fbclid=IwY2xjawUoEupleHRuA2FlbQIxMQBwZG9mA3NydGMGYXBwX2lkATAAAR6kEa4u7o4Ep7aMkTt9KX398znvPIWS4BzF42W_Cpkc33fQmuHqmzF_zRpGcQ_aem_Ex0eOBSYVbjYu4q0YT11aA)  
- **Backend system:** central\_bank\_engine\_v13.py  
- **Economic model:** w4\_financial\_logic.md  
- **Frontend support:**  omo\_refactored\_v64.html

### **3\. Evidence Links**

- ### **Group coordination: [GROUP COORDINATOR](https://drive.google.com/drive/u/1/folders/1lsXOd0_-NexrzgyhQUKMaGx0UEFfjKte?fbclid=IwY2xjawUPmT9wZG9mA2V4dG4DYWVtAjExAHNydGMGYXBwX2lkATAAAR5yuuR6N53ApqqTQ3321LWSzuKP6dShmM8bVuxARnFUX-2COIvlDJxjl1lfbA_aem_BVqBZcdnn_cm3OlRWQUfXA)**

- **Backend system:** [LINK GITHUB BACKEND](https://github.com/FTU-Legacy-63/G03/blob/main/app/central_bank_engine_v13.py)  
- **Economic model: [Regression.xlsx](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797);** [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true); [LINK GITHUB MODEL](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md); [LOGIC TEST 3.0.xlsx](https://docs.google.com/spreadsheets/d/1ZoAsCYlYXYfGKCg94ibXo2z694SpF1s7/edit?gid=1654191935#gid=1654191935)  
- **Frontend support:** [BG AND TOPBAR](https://drive.google.com/file/d/1faW8OVMWWpNv_xBmucmyuPpJMMtbUUMb/view?usp=sharing); [LINK GITHUB TOPBAR](https://github.com/FTU-Legacy-63/G03/blob/main/app/topbar.png); [LINK GITHUB BG](https://github.com/FTU-Legacy-63/G03/blob/main/app/background.png)

### **4\. How My Work Is Used**

- **Group coordination:** My coordination work helps maintain a clear division of responsibilities and ensures that the backend, economic model, testing, and frontend components develop consistently. By tracking progress, giving feedback, and conducting final checks, I help identify inconsistencies between components and facilitate revisions before the final product is delivered.  
- **Backend system:** The backend file helps process relevant inputs, applies financial calculations and economic rules, and generates simulation results based on the player's decisions.   
- **Economic model:** The economic model provides the analytical foundation for the game's monetary policy simulation. The interbank regression and financial formulas help estimate how changes in liquidity conditions and monetary policy decisions may affect interbank interest rates. These simulated interest rate changes are then connected to broader macroeconomic outcomes, particularly GDP growth and inflation. This allows players to explore the possible consequences of their decisions and understand the transmission mechanism from money-market conditions to the wider economy.  
- **Frontend support:** Improves the interface's visual appeal and makes the game more engaging for users.

### **5\. Integration, Testing and Revision**

- ### **Group Coordination:** Coordinated task allocation, communication, and feedback across team members. Reviewed the feedback and integrated it in the backend, economic model, and frontend, and followed up on necessary revisions during the final checks**.**

- ### **Backend Development:** Integrated the economic model, financial formulas, and game rules into the backend file, which will be connected to frontend by API file. Other members tested the backend against the relevant game scenarios and gave feedback. Suitable adjustments will be implemented into the file to ensure consistency with the economic model.

- ### **Economic Model:** Integrated the finalized interbank regression into the economic model, which will be integrated into the backend. Team members  checked the consistency between model assumptions, regression outputs, and implemented calculations through Logic Test 2.0 and Logic Test 3.0, then revisions and adjustments will be done where necessary. 

- ### **Frontend Support:** Contributed to the background, top-bar and overall design and coordinated their integration with the game interface. Reviewed the visual presentation and refined the components based on feedback.

**6\. Remaining Limitation**

A key limitation of the game is that the economic model remains a simplified representation of real-world economic relationships. 

Although historical data, regression analysis, and economic research informed its development, some relationships and coefficients were adjusted to make the intended monetary policy transmission mechanism more visible in the simulation. 

The model has not yet been fully empirically validated, so its outcomes should be interpreted as educational illustrations rather than precise forecasts of actual macroeconomic developments.

