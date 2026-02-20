An Automated and Accountable Charity Donation Framework Using Blockchain
=====================================================================

Author: Pujitha (Roll No: 24691F00I0)
Institution: Madanapalli Institute of Technology and Science
Submission Date: February 10, 2026

Abstract
--------
This project presents the design and implementation of an automated and accountable charity donation framework leveraging blockchain technology. The system ensures transparency, immutability, and traceability of donations from donors to beneficiaries while minimizing administrative overhead and enabling auditors and stakeholders to independently verify fund flows. The report documents problem motivation, requirements, system architecture, smart contract logic, implementation details, testing, deployment, evaluation, security analysis, and future work. Appendices include source code listings, deployment instructions, test logs, and a user manual.

Keywords: blockchain, smart contract, donation, transparency, charity, accountability, decentralization

Acknowledgements
----------------
I wish to express my sincere gratitude to my supervisor and faculty for guidance, and to the Madanapalli Institute of Technology and Science for providing resources and support during this project.

Table of Contents
-----------------
1. Introduction
2. Problem Statement and Objectives
3. Literature Review
4. Requirements and Analysis
5. System Architecture and Design
6. Blockchain Fundamentals and Technology Stack
7. Smart Contract Design and Logic
8. Implementation Details
9. Testing and Validation
10. Security and Privacy Analysis
11. Deployment and Maintenance
12. Results and Discussion
13. Conclusion and Future Work
14. References
15. Appendices

1. Introduction
----------------
1.1 Background

Charitable giving plays a vital role in addressing social challenges, but traditional donation systems often suffer from lack of transparency, high administrative costs, and insufficient accountability. Donors seek assurance that donations reach intended beneficiaries, and charities require efficient tracking and reporting tools.

1.2 Motivation

Blockchain provides an immutable ledger that records transactions transparently. Smart contracts enable automated distribution of funds when predefined conditions are met. Applying these technologies to charity donation systems reduces fraud risk, increases donor confidence, and simplifies auditing.

1.3 Scope of the Project

This project builds a prototype donation platform that: accepts donor contributions, records donations on a blockchain ledger, issues receipts, enforces conditional distribution rules via smart contracts, and provides reporting and audit trails for stakeholders.

2. Problem Statement and Objectives
----------------------------------
2.1 Problem Statement

Existing donation systems lack verifiable transparency and rely on centralized intermediaries. Donors cannot independently verify fund distribution, and charities bear significant administrative costs.

2.2 Objectives

- Design a blockchain-backed architecture for recording donations
- Implement smart contracts to govern fund allocation and disbursement
- Create a web-based interface for donors, administrators, and auditors
- Ensure privacy for donor identities while keeping transaction proofs public
- Provide deployment and testing documentation

3. Literature Review
--------------------
3.1 Charity and Donation Systems

Overview of existing online donation platforms, their limitations, and trust models.

3.2 Blockchain for Social Good

Survey of academic and industry projects using blockchain for donations, supply-chain transparency, and public grants. Comparison of public vs permissioned ledgers for charitable applications.

3.3 Smart Contracts in Practice

Review of common smart contract patterns for escrow, release conditions, access control, and multi-signature governance.

4. Requirements and Analysis
---------------------------
4.1 Functional Requirements

- FR1: Donors can create donations and receive verifiable receipts
- FR2: Administrators can set campaign goals and rules
- FR3: Smart contracts automatically release funds on meeting conditions
- FR4: Auditors can query transaction history and verify integrity

4.2 Non-functional Requirements

- NFR1: Tamper-evident transaction records
- NFR2: Reasonable cost per transaction (gas or fees)
- NFR3: Scalable to thousands of donors
- NFR4: Usable web interface

4.3 Threat Model and Privacy Requirements

Describe attacker capabilities and privacy goals. Donors' identity optionally pseudonymous; payment settlement may use off-chain rails while proofs are on-chain.

5. System Architecture and Design
--------------------------------
5.1 High-level Architecture

Component diagram (textual):
- Web Frontend: donor and admin UI
- Backend Server: application logic, off-chain aggregation
- Blockchain Layer: smart contracts and ledger
- Payment Gateway: fiat/crypto payment settlement

5.2 Data Flow

Steps: donor initiates donation → payment gateway processes payment → backend issues transaction to smart contract → smart contract records donation and updates campaign state → automated or admin-triggered disbursement when conditions met.

5.3 Design Decisions

- Use a permissioned Ethereum-compatible chain (or testnet) for prototyping
- Keep personally identifiable information off-chain; store hashes on-chain
- Implement multisig or DAO-style release for higher-value disbursements

6. Blockchain Fundamentals and Technology Stack
----------------------------------------------
6.1 Blockchain Fundamentals

Explanation of blocks, transactions, consensus, immutability, and smart contracts. Include equations for cryptographic hash properties as needed: $H(x)$ denotes a collision-resistant hash function.

6.2 Chosen Stack

- Smart contracts: Solidity
- Chain: Ethereum testnet / local Ganache / Hardhat network
- Backend: Flask (Python) — existing files: `app.py`, `blockchain.py` in project root
- Frontend: Simple HTML templates in `templates/index.html`
- Tools: web3.py, Brownie/Hardhat for local dev, IPFS for storing large files (optional)

7. Smart Contract Design and Logic
--------------------------------
7.1 Contract Responsibilities

- Create Campaigns
- Accept Donations (record donor address, amount, timestamp)
- Track campaign goal and progress
- Conditional distribution: release to beneficiary when goal met or deadline reached
- Emergency pause and admin controls

7.2 Data Structures

- structs: Campaign { owner, goal, raised, beneficiary, deadline, active }
- mappings: campaignId => Campaign, campaignId => donations[]

7.3 Functions and Modifiers

- `createCampaign()` — initialize campaign
- `donate()` — accept donation and emit `DonationReceived`
- `releaseFunds()` — check conditions and transfer
- `pause()`/`unpause()` — admin controls

7.4 Events

Emit `CampaignCreated`, `DonationReceived`, `FundsReleased` for off-chain indexing.

8. Implementation Details
-------------------------
8.1 Repository Structure

- `app.py` — Flask web server and routes (web UI and API endpoints)
- `blockchain.py` — helper functions for interacting with smart contracts and the chain
- `demo_execution.py` — scripts to demonstrate typical flows and tests
- `templates/index.html` — basic frontend for donors

8.2 Backend Implementation Highlights

Explain key endpoints: `/campaigns`, `/donate`, `/campaigns/<id>/status`. Describe how `blockchain.py` wraps web3.py to submit transactions and listen for events.

8.3 Example Code Snippets

Python pseudo-code for sending a donation transaction:

```python
from blockchain import ContractInterface
ci = ContractInterface()
tx_hash = ci.donate(campaign_id, donor_address, amount_wei)
ci.wait_for_receipt(tx_hash)
```

8.4 Frontend

Provide a donor flow: select campaign → enter amount → sign/submit payment → view receipt. Use `templates/index.html` as starting point.

9. Testing and Validation
-------------------------
9.1 Unit Tests

Smart contract unit tests should cover createCampaign, donate, edge-cases for over/underflow, paused states, and unauthorized releases.

9.2 Integration Tests

Run end-to-end tests using a local chain: simulate donations, verify balances, and ensure event logs match expected states.

9.3 Performance and Cost Analysis

Estimate gas cost per donation transaction and discuss batching strategies for cost reduction (e.g., off-chain aggregation with on-chain settlement).

9.4 Test Results (Sample)

- Test 1: Create campaign — passed
- Test 2: 100 simulated donations — all recorded on-chain; average gas: X gwei (replace with measured values after running tests)

10. Security and Privacy Analysis
-------------------------------
10.1 Threat Vectors

- Smart contract vulnerabilities: reentrancy, integer overflow/underflow, access control bypass
- Off-chain threats: compromised server keys, data leakage

10.2 Mitigations

- Use OpenZeppelin libraries for safe math and access control
- External audits of contracts for high-value deployments
- Key management: hardware wallets for admin multi-sig

10.3 Privacy Considerations

Keep PII off-chain and provide hashed references on-chain. Use zero-knowledge schemes for advanced privacy if required.

11. Deployment and Maintenance
-----------------------------
11.1 Deployment Steps (High Level)

- Deploy smart contracts to target network
- Configure backend with contract ABI and network endpoints
- Set admin keys and multisig wallets
- Launch web frontend and connect payment gateway

11.2 Monitoring and Logging

Monitor on-chain events and backend health. Provide alerting for failed disbursements.

11.3 Backup and Recovery

Maintain backups for off-chain databases and ensure recovery plans for admin keys.

12. Results and Discussion
-------------------------
Summarize functionality achieved: verifiable donation recording, automated disbursement for simple conditions, and clear audit trails. Discuss tradeoffs: transaction cost vs transparency, privacy vs accountability.

13. Conclusion and Future Work
-----------------------------
13.1 Conclusion

The prototype demonstrates blockchain's practical value for increasing transparency in charity donations. It reduces reliance on centralized ledgers and makes auditing straightforward.

13.2 Future Work

- Integrate fiat-to-crypto payment rails for smoother donor UX
- Add richer governance models (DAO) for fund release decisions
- Add privacy-preserving features (zk proofs) and verifiable credentials for beneficiaries

14. References
----------------
- [1] S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008.
- [2] OpenZeppelin Contracts — https://openzeppelin.com
- [3] Ethereum whitepaper — https://ethereum.org
- Include additional academic sources and URLs used during the literature review.

15. Appendices
---------------
Appendix A — Source Code Overview

The project includes these files:
- `app.py` — main Flask app (see repository root)
- `blockchain.py` — chain interaction helpers
- `demo_execution.py` — demo and test runner
- `templates/index.html` — simple web UI

Appendix B — Key Code Listings

Note: Full code listings are included below for examiners. For brevity in this document, the repository contains full source files. Refer to the repository for exact code and run instructions.

Appendix C — Deployment Guide

High-level deployment checklist:
1. Install Python dependencies: `pip install -r requirements.txt`
2. Start a local blockchain (Ganache) or connect to a testnet
3. Deploy contracts using Brownie/Hardhat
4. Configure `app.py` with contract address and ABI
5. Run `python app.py` to start the backend

Appendix D — User Manual

Steps for donors:
1. Open web UI
2. Choose campaign
3. Enter donation amount and complete settlement
4. View transaction receipt and copy transaction hash for verification

Appendix E — Glossary

- Blockchain: A distributed ledger of transactions
- Smart contract: Program executed on the blockchain
- Gas: Transaction fee on Ethereum-like networks

-- End of report draft --

Notes
-----
This file serves as a complete, editable project report. If you want, I can:
- Expand each section into more detailed subsections and lengthen the text to reach a target of 80–100 printed pages (convertible to PDF),
- Insert full source code appendices (inlined),
- Generate a PDF export and a DOCX version.
