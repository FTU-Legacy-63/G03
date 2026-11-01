# G03 - FINAL INDIVIDUAL CONTRIBUTION VERIFICATION

**1. For each member, identify the most important original contribution to the final economic model, auction engine, scenario system, interface, or testing, and explain where it appears in the product**

| **Member** | **Most important original contribution** | **Where it appears in the product** |
|---|---|---|
| Nguyễn Bảo Hiền - 2412380017 | - Collected, organized, and cleaned monetary policy, banking, and macroeconomic data for the team's analysis and simulation development.<br>- Designed the economic scenarios and phase-specific liquidity conditions, ensuring that players faced different monetary policy challenges throughout the game.<br>- Developed the decision evaluation and feedback framework, explaining whether players' OMO decisions were appropriate under each scenario.<br>- Conducted frontend testing across the first five phases, covering different auction decisions and gameplay flows. | - Data: [DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657)<br>- Scenario and Explanation: [Scenario 8.0.xlsx](https://docs.google.com/spreadsheets/d/1F29oFFkw-PsIbhjPQ_tk1FUx7LPtVfPh/edit?gid=335857123#gid=335857123)<br>- Test frontend: [LINK TEST FRONTEND](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_frontend_v2.cjs) |
| Nguyễn Khánh Linh - 2413380027 | - Conducted data filtering and regression analysis to support the interbank interest rate formula.<br>- Researched and refined the macroeconomic formulas and parameters to establish the relationship between interbank interest rates, GDP growth, and inflation.<br>- Developed approximately 60% of the financial logic and game-process specifications used to guide backend implementation *(specification of responsibility is in the answer for Q3).*<br>- Designed the learning cards to explain key financial and monetary policy concepts to players.<br>- API integration | - Economic model: [Regression.xlsx](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797)<br>[LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true)<br>[LINK GITHUB MODEL](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md)<br>- Learning card: [LINK GITHUB LEARNING CARD](https://github.com/FTU-Legacy-63/G03/blob/main/learning_card.md)<br>- Backend testing: [LINK GITHUB BACKEND TEST](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_engine_v2.py)<br>- Frontend support and API integration: [LINK GITHUB API](https://github.com/FTU-Legacy-63/G03/blob/main/WEEK%206/app.py) |
| Vũ Lưu Minh Ngọc - 2412380037 | - Developed the main backend engine, integrating auction rules, financial calculations, and macroeconomic formulas into a unified system.<br>- Contributed approximately 40% of the game-process and financial logic specifications for backend implementation *(specification of responsibility is in the answer for Q3).*<br>- Coordinated task allocation, communication, and feedback across the team to ensure that different components could be integrated into the final product. | - Group coordination: [GROUP COORDINATOR](https://drive.google.com/drive/u/1/folders/1lsXOd0_-NexrzgyhQUKMaGx0UEFfjKte?fbclid=IwY2xjawUPmT9wZG9mA2V4dG4DYWVtAjExAHNydGMGYXBwX2lkATAAAR5yuuR6N53ApqqTQ3321LWSzuKP6dShmM8bVuxARnFUX-2COIvlDJxjl1lfbA_aem_BVqBZcdnn_cm3OlRWQUfXA)<br>- Backend system: [LINK GITHUB BACKEND](https://github.com/FTU-Legacy-63/G03/blob/main/app/central_bank_engine_v13.py)<br>- Economic model: [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true)<br>[LINK GITHUB MODEL](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md)<br>[LOGIC TEST 3.0.xlsx](https://docs.google.com/spreadsheets/d/1ZoAsCYlYXYfGKCg94ibXo2z694SpF1s7/edit?gid=1654191935#gid=1654191935) |
| Nguyễn Minh Trang - 2412380049 | - Designed the UI/UX structure, including the visual style, information hierarchy, navigation, and layout of the different game screens.<br>- Developed approximately 85% of the frontend implementation using HTML, CSS, and JavaScript.<br>Implemented the interactive interface, including market information, OMO decision controls, auction results, and economic data visualizations. *(specification of responsibility is in the answer for Q3).*<br>- Contributed to financial data preparation and conducted frontend testing across the last 4 phases. | - UI/UX design: [LINK GITHUB HTML](https://github.com/FTU-Legacy-63/G03/blob/main/app/central_bank_engine_v13.py)<br>- Frontend development: [LINK GITHUB FRONTEND](https://github.com/FTU-Legacy-63/G03/blob/main/app/central_bank_engine_v13.py)<br>- Data: [DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657)<br>- Initial prototype: [LINK TO INITIAL PROTOTYPE](https://github.com/kipSoos/WTFAID/blob/main/index.html)<br>- Test frontend: [LINK TEST FRONTEND](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_frontend_v2.cjs) |

<br>

**2. Explain how the economic model, financial data, auction logic, and interface were integrated. Which members were responsible for checking that the combined system produced the intended results?**

**_Step 1: Financial data preparation_**

Bảo Hiền led the collection, organization, and cleaning of historical monetary policy, banking, and macroeconomic data. Minh Trang supported this process by contributing to data preparation.

The resulting database provided reference information for economic analysis, regression testing and scenario development.

**_Step 2: Economic model and Auction logic development_**

Khánh Linh used the prepared data to conduct filtering and regression analysis, particularly for the interbank interest rate formula. She also refined the macroeconomic formulas to clarify the transmission mechanism.

Minh Ngọc worked with Linh to review the regression results, developed the auction-related logic.

**_Step 3: Scenario_**

The scenario system was developed by Bảo Hiền, who defined the economic conditions, liquidity situations and policy challenges across phases.

**_Step 4: Backend Developement_**

Based on the financial logic specifications were translated into executable calculations by Minh Ngọc in the backend engine.

**_Step 5: Frontend development and API integration_**

Minh Trang implemented the main frontend, including the game screens, interactive controls and data visualizations.

Khánh Linh implemented the Flask API integration in app.py and supported frontend coding when Trang was unavailable. Ngọc supported the visual components.

**_Step 6: Integration Testing and Revision_**

- Bảo Hiền: Tested the first five phases from the frontend perspective, including decision scenarios, input validation, navigation, and API responses.

- Khánh Linh: Tested backend decision outcomes against the intended financial logic and checked the consistency between model calculations and implemented results.

- Minh Ngọc: Self-testing her backend outcome; Coordinated task allocation, communication, and feedback collection to support the overall integration process.

- Minh Trang: Tested the last four phases, focusing on user interactions, interface responsiveness, navigation, and the presentation of backend results.

All team members participated in testing the game by playing through its different components and providing feedback on each part. Based on these discussions and feedback, each member made revisions within their scope of responsibility.

<br>

**3. Some activities, including data preparation, economic modelling, frontend development, and testing, involved overlapping responsibilities. How were these responsibilities actually divided, and what evidence supports each member's claimed share of the work?**

The following specifications are just for shared responsibilities; tasks conducted primarily by one member only are stated in the answer for Q1. The percentages are estimates of contributions within the respective workstreams.

**_Financial logic Specifications_**
- Nguyễn Khánh Linh - 60%: Primarily responsible for developing the financial logic related to maturity cash flows, liquidity conditions, interbank interest rate and macroeconomic transmission mechanism (Evidence: [LINK GITHUB MODEL](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md), [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true), [Regression.xlsx](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797))

- Vũ Lưu Minh Ngọc - 40%: Primarily responsible for developing the auction-related logic, including forecasted liquidity demand, bid demand, cash bid calculation, bidding rates and transaction pricing (Evidence: [LINK GITHUB MODEL](https://github.com/FTU-Legacy-63/G03/blob/main/docs/w4_financial_logic.md), [LOGIC TEST 2.0](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?rtpof=true), [Regression.xlsx](https://docs.google.com/spreadsheets/d/1eN3w-isF81GoeVL2Vetykxyp2056th1-/edit?gid=2130499797#gid=2130499797))

Both members collaborated and revised each other’s work.

**_Data Preparation_**

- Nguyễn Bảo Hiền - 80%: Mainly responsible for preparing and organizing data used in the game, including data processing and preparing scenario-related inputs (Evidence: [DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657))

- Nguyễn Minh Trang - 20%: Supported data preparation and database-related tasks. Trang mainly supported in collecting interbank rate and win rate of auction (Evidence: [DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657))

**_Backend Development and Integration_**

- Vũ Lưu Minh Ngọc: Mainly responsible for implementing the backend engine, integrating the financial and auction logic, and coordinating the connection between different system components (Evidence: [LINK GITHUB BACKEND](https://github.com/FTU-Legacy-63/G03/blob/main/app/central_bank_engine_v13.py)).

- Nguyễn Khánh Linh: Supported backend testing, API integration, and checking whether the implemented calculations were consistent with the agreed financial logic (Evidence: [LINK GITHUB API](https://github.com/FTU-Legacy-63/G03/blob/main/WEEK%206/app.py), [LINK GITHUB BACKEND TEST](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_engine_v2.py)).

**_Frontend Development_**

- Nguyễn Minh Trang - 85%: Primarily responsible for implementing the frontend, including the main interface structure, page layouts, visual components and user interactions (Evidence: [LINK GITHUB HTML](https://github.com/FTU-Legacy-63/G03/blob/main/app/omo_refactored_v64.html))

- Nguyễn Khánh Linh - approximately 10%: Supported frontend coding by implementing additional changes when feedback from the team required revisions and Trang was unavailable. Since these coding tasks depended on feedback during development, they were not assigned to specific fixed components. Some big components that worth mentioning: Guide & Learning cards; Integration of liquidity conditions, CB bills inventory and Repo positions in accordance with the backend; Integration of post-phase auction results and economic conditions for 6 phases (Evidence: [LINK GITHUB HTML](https://github.com/FTU-Legacy-63/G03/blob/main/app/omo_refactored_v64.html))

- Vũ Lưu Minh Ngọc - approximately 5%: Contributed to the visual design of the frontend, including designing interface elements such as the background (Evidence: [BG AND TOPBAR](https://drive.google.com/file/d/1faW8OVMWWpNv_xBmucmyuPpJMMtbUUMb/view?usp=sharing), [LINK GITHUB TOPBAR](https://github.com/FTU-Legacy-63/G03/blob/main/app/topbar.png), [LINK GITHUB BG](https://github.com/FTU-Legacy-63/G03/blob/main/app/background.png))

**_Testing and Quality Review_**

- Backend testing: Khánh Linh checked calculation accuracy and the consistency of backend outputs (80 tests); Minh Ngọc added 20 tests (Evidence: [LINK GITHUB BACKEND TEST](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_engine_v2.py))

- Frontend testing: Bảo Hiền tested the first 5 phases, while Minh Trang tested the remaining 4 phases (Evidence: [LINK TEST FRONTEND](https://github.com/FTU-Legacy-63/G03/blob/main/tests/test_frontend_v2.cjs))

- Joint testing: All four members played through the game, reviewed each component, provided feedback, and discussed necessary revisions.
