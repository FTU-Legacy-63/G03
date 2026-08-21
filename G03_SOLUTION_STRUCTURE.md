# SOLUTION STRUCTURE

## 1\. Product Direction

The product is an interactive educational simulation in which the user acts as the Central Bank of Country X.

The stated goal in the current concept is to maintain price stability, support sustainable economic growth and safeguard financial-system stability. Government actions and global events form part of the simulated environment rather than player-controlled decisions.



## 2\. Core User Flow

User → Input → Process → Output → User Action Scenario → Indicators → User Analysis → Policy Decision → Economic Engine → Updated Indicators → Outcome/Report → Market Reaction → Next Phase



## 3\. Initial Required Information

### Economic indicators

* GDP growth
* Inflation
* Unemployment rate
* Public debt

### Banking indicators

* Credit growth
* Liquidity ratio
* Deposit growth

### Financial-market indicators

* 10Y Government Bond Yield
* Equity Market Index
* Real Estate Price Index

### Government information

* Public Debt/GDP
* Government Spending Growth

Not every indicator needs to appear in every phase.



## 4\. Core Process Type

The product uses a multi-stage economic decision simulation. State(t) + Scenario/Shock(t) + User Decision(t) → Economic Engine → State(t+1)

The updated state is carried forward rather than resetting after each phase.



## 5\. MVP Flow

The first implementation can demonstrate one complete decision cycle:

1. Scenario: inflation-related economic situation.
2. Data: show the most relevant indicators.
3. Learning support: indicator explanations using "What is it?", "Why does it matter?", "What happens if it rises/falls?", and "What should I watch with it?"
4. Decision: user chooses a monetary-policy response by changing interest rate and setting expected inflation
5. Economic Engine: simplified relationships estimate changes.
6. Output: updated indicators, market reaction, and decision assessment.
7. Continue: updated state becomes the next starting point.



## 6\. Target Product Direction

The current concept proposes approximately 5--7 phases: 

\- Phase 1: Inflation 

\- Phase 2: Stimulate the Economy 

\- Phase 3: Credit \& Housing Boom 

\- Phase 4: Banking Crisis 

\- Phase 5: Government Bond 

\- Phase 6: Global Shocks

The concept also allows crises to arise from accumulated player decisions, otherwise external problems will cause the same issue.



## 7\. Product Interface

The current concept proposes three main tabs: 

\- Scenario 

\- Decisions 

\- Reports (Dashboard)



## 8\. MVP Scope

Recommended first working scope: 

\- one fictional country 

\- one Central Bank player 

\- common starting economic condition 

\- Phase 1: Inflation 

&#x20; + a limited set of key indicators

&#x20; + interest rate and expected inflation decision

&#x20; + outcome dashboard/report

&#x20; + educational explanation

The purpose is to prove the complete chain: Scenario → Decision → Economic Calculation → Outcome → Learning



## 9\. Target Scope

After the MVP works, expansion may include: 

\- additional phases

\- more monetary-policy tools

\- banking and credit conditions

\- government bond market

\- banking crisis

\- external shocks

\- performance comparison/community functions.



## 10\. Fallback Scope

If implementation becomes too complex: 

\- a small set of core indicators

\- increase / hold / decrease decisions 

\- rule-based calculations 

\- one result dashboard

\- short educational explanation



## 11\. Out of Scope for MVP

* full replication of a real economy
* real-world forecasting
* detailed simulation of every commercial bank
* direct player control of Government decisions
* detailed global-market simulation
* multiplayer decisions affecting one another



## 12\. Initial Rule Hypothesis

The economic engine will use simplified relationships whose coefficients/elasticities are treated as assumptions initially.

Examples of relationships to model include: 

\- interest rate ↔ inflation

\- interest rate ↔ GDP growth

\- GDP growth ↔ unemployment, public debt/GDP

Exact formulas and coefficients still require final validation/calibration.



## 13\. Responsibility by Output

\- Vũ Lưu Minh Ngọc: Developer 

Output: MVP Web Application (Functional implementation of the simulation, game logic, events, progression and game state have been designed by others), connect backend and frontend

\- Nguyễn Bảo Hiền: Economic Analyst

Output: Excel Simulation Model \& Parameter set (economic models, formulas and thresholds), Economic decision matrix (Policy actions available to players with corresponding effects on GDP, inflation, debt and other indicators) - work with game logic member

\- Nguyễn Minh Trang: UI/UX design + Learning experience

Output: Interactive Web Dashboard (Interface for economic indicators, scenarios, decisions, outcomes and player progress), Learning experience system (Contextual knowledge explanations and signals)

\- Nguyễn Khánh Linh: Game Logic \& Scenario 

(Output: Scenario tree \& Event script (Step-by-step branching narrative across economic phases, with news, economic situations, crises), Scenario-specific expected outcomes)

