## **Individual Contribution Report – Nguyễn Bảo Hiền**

### **1\. My Main Responsibility**

- **Data collection and cleaning (80%):** I was responsible for collecting, compiling, organizing, and cleaning monetary policy, banking, and macroeconomic data from relevant sources. I prepared the database for the team to reference in economic modeling and game development, checking the consistency and usability of the collected information. My contribution covered approximately 80% of this work; regression analysis was conducted by another team member.  
- **Scenario design:** I developed the economic contexts and phase-specific situations that structure the game. This involved defining liquidity conditions, macroeconomic developments, and policy challenges for each phase, so that players would face different circumstances when making open market operation decisions.  
- **Decision evaluation and explanation:** I developed the phase-specific feedback used to assess players’ auction decisions against the prevailing economic conditions. I also designed the overall explanation framework to evaluate the consistency and appropriateness of the player’s decisions across the full game flow.  
- **Test frontend (50%):** I conducted comprehensive frontend testing across five initial phases of the game, covering different auction methods, policy decisions, user interactions, and complete gameplay flows. I also tested input validation, API responses, navigation, and interface responsiveness, documenting the test results and identifying potential issues to ensure the game's functionality, consistency, and usability.

### **2\. My Concrete Outputs**

- **Data:** data.md  
- **Scenario design:** Scenario.md  
- **Decision evaluation:** Scenario.md  
- **Test frontend:** test\_frontend\_v2.cjs

### **3\. Evidence Links**

- **Data:** [DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657)  
- **Scenario design and explanations:** [Scenario 8.0.xlsx](https://docs.google.com/spreadsheets/d/1F29oFFkw-PsIbhjPQ_tk1FUx7LPtVfPh/edit?gid=335857123#gid=335857123)  
- **Test frontend**: [LINK FRONTEND TEST](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_frontend_v2.cjs)

### **4\. How My Work Is Used**

- **Data:** The organized database provides reference information on interest rates, monetary operations, and macroeconomic indicators for the team’s subsequent analysis and game development.   
- **Scenario design:** The scenarios establish the economic background and liquidity conditions for each phase. They provide the context in which players choose auction instruments and actions, allowing the game to present different monetary policy challenges rather than isolated decisions.  
- **Decision evaluation:** The phase-specific explanations help players understand whether their auction choices are appropriate under the given conditions and why. The overall explanation brings these decisions together to assess the coherence of their policy approach throughout the simulation.  
- **Test frontend:** The testing report documents the functionality and reliability of the game across the first five phases. It provides the team with evidence of successful gameplay flows, decision processing, interface responsiveness, and error handling, while identifying areas requiring further verification.

### **5\. Integration, Testing and Revision**

- **Data preparation:** I reviewed the collected information and organized it into a consistent database for use by other project components. This included checking data presentation and cleaning the source material before it was shared with the team.  
- **Scenario development:** I reviewed the progression of economic conditions across phases and refined scenario details to maintain a coherent sequence of policy challenges. I also checked that the contexts were aligned with the decisions players were expected to make.  
- **Decision feedback:** I examined the phase-specific evaluation rules under different possible player choices, including no-action cases and instrument constraints. Where conditions overlapped, feedback was missing, or wording was inconsistent, I revised the relevant rules and explanations. I also reviewed the overall assessment to keep it consistent with the phase-level feedback.   
- **Test frontend:** I tested the game across the first five phases, covering different auction decisions, navigation flows, input validation, and error-handling scenarios. I also examined interface responsiveness and API interactions, identified technical issues, and verified the implemented solutions through repeated testing. The results were documented in a structured testing report, with unverified cases clearly identified.

### **6\. Remaining Limitation**

The scenario simplifies how a real money market works. Liquidity, instruments and shocks are stylized and closed-economy, the scoring thresholds come from design judgment rather than historical data, and the macro results at each checkpoint show the direction of effects without forecasting them.  
This makes the game best suited to practicing liquidity management decisions, not to predicting real policy outcomes.  
