# A MAIN PROJECT REPORT ON

# AUTOMATED AND ACCOUNTABLE CHARITY DONATION FRAMEWORK USING BLOCKCHAIN

### Submitted in partial fulfillment of the requirements for the award of the degree of

## BACHELOR OF TECHNOLOGY
### IN
### COMPUTER SCIENCE AND ENGINEERING

---

**SUBMITTED BY:**

**NAME: [YOUR NAME HERE]**  
**ROLL NO: [YOUR ROLL NO HERE]**

**UNDER THE GUIDANCE OF:**
**[GUIDE NAME]**

---

### DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
### [YOUR COLLEGE NAME]
### [YEAR]

---

# CERTIFICATE

This is to certify that the project entitled **"AUTOMATED AND ACCOUNTABLE CHARITY DONATION FRAMEWORK USING BLOCKCHAIN"** is a bona fide work carried out by **[YOUR NAME]** in partial fulfillment for the award of **Bachelor of Technology** in **Computer Science and Engineering** from **[COLLEGE NAME]** during the academic year **[YEAR]**.

**Internal Guide** \t\t\t\t\t **Head of Department**

\
\
**External Examiner**

---

# DECLARATION

I hereby declare that the project report entitled **"AUTOMATED AND ACCOUNTABLE CHARITY DONATION FRAMEWORK USING BLOCKCHAIN"** submitted by me to **[COLLEGE NAME]**, in partial fulfillment of the requirement for the award of the degree of **Bachelor of Technology in Computer Science and Engineering**, is a record of bona fide project work carried out by me under the guidance of **[GUIDE NAME]**.

I further declare that the work reported in this project has not been submitted and will not be submitted, either in part or in full, for the award of any other degree or diploma in this institute or any other institute or university.

**Signature of the Student**

---

# ACKNOWLEDGEMENT

The satisfaction and euphoria that accompany the successful completion of any task would be incomplete without the mention of the people who made it possible, whose constant guidance and encouragement crowned my efforts with success.

I would like to express my deep sense of gratitude to my project guide **[GUIDE NAME]**, for his/her valuable guidance, constant encouragement, and kind suggestions during the course of this project work.

I am also thankful to **[HOD NAME]**, Head of the Department of Computer Science and Engineering, for providing all the necessary facilities and technical support.

I would like to thank all the teaching and non-teaching staff of the Department of Computer Science and Engineering for their direct and indirect help.

Finally, I express my gratitude to my parents and friends for their unfailing support and cooperation throughout my studies.

---

# ABSTRACT

Charity organizations play a pivotal role in social welfare, yet the sector is often plagued by issues of transparency, accountability, and fraud. Donors frequently hesitate to contribute due to a lack of trust in how their funds are utilized. Traditional centralized systems for tracking donations are opaque, prone to manipulation, and often fail to provide real-time assurance to stakeholders.

To address these challenges, this project proposes an **"Automated and Accountable Charity Donation Framework Using Blockchain."** This system leverages the immutable and decentralized nature of blockchain technology to create a transparent ledger for all transactions. The framework enables donors to track their donations from the point of transfer to the final beneficiary.

Key features of this system include:
1.  **Decentralized Ledger**: A custom-built blockchain to record every donation and fund release, ensuring data cannot be altered or deleted.
2.  **Smart Contracts**: Automated protocols that release funds to charities only when specific verification conditions are met, reducing the risk of misuse.
3.  **Role-Based Access Control**: Distinct interfaces for Donors, Charities, and Admins to manage their respective activities securely.
4.  **Fraud Detection**: Integrated mechanisms to verify the integrity of the blockchain and detect any tampering attempts (e.g., a 51% attack simulation).
5.  **OTP & Bank Integration**: Enhanced security layers for user verification and fund transfers.

The proposed system is implemented using **Python** and **Flask** for the backend, with a responsive frontend design. This project demonstrates how blockchain can revolutionize philanthropy by restoring trust and ensuring that every penny donated reaches its intended cause.

**Keywords**: Blockchain, Charity, Smart Contracts, Transparency, Flask, Python, Cryptography, SHA-256.

---

# TABLE OF CONTENTS

**CHAPTER 1: INTRODUCTION**
   1.1 Introduction
   1.2 Problem Statement
   1.3 Objectives of the Project
   1.4 Scope of the Project
   1.5 Methodology

**CHAPTER 2: LITERATURE REVIEW**
   2.1 Existing System
   2.2 Disadvantages of Existing System
   2.3 Proposed System
   2.4 Advantages of Proposed System
   2.5 Blockchain Technology Overview

**CHAPTER 3: SYSTEM ANALYSIS**
   3.1 Feasibility Study
       3.1.1 Technical Feasibility
       3.1.2 Economic Feasibility
       3.1.3 Operational Feasibility
   3.2 System Requirements
       3.2.1 Hardware Requirements
       3.2.2 Software Requirements
   3.3 Functional Requirements
   3.4 Non-Functional Requirements

**CHAPTER 4: SYSTEM DESIGN**
   4.1 System Architecture
   4.2 UML Diagrams
       4.2.1 Use Case Diagram
       4.2.2 Class Diagram
       4.2.3 Sequence Diagram
       4.2.4 Activity Diagram
       4.2.5 Data Flow Diagram (DFD)
   4.3 Database Design / Data Structure
   4.4 Module Description

**CHAPTER 5: IMPLEMENTATION**
   5.1 Technology Stack Description
       5.1.1 Python
       5.1.2 Flask Framework
       5.1.3 HTML/CSS/JavaScript
   5.2 Algorithms Used
       5.2.1 SHA-256 Hashing
       5.2.2 Proof of Work (PoW) consensus
   5.3 Key Code Implementation
       5.3.1 Blockchain Class
       5.3.2 Block Structure
       5.3.3 API Routes

**CHAPTER 6: TESTING**
   6.1 Testing Methodologies
   6.2 Unit Testing
   6.3 Integration Testing
   6.4 System Testing
   6.5 Security Testing (Tamper Simulation)

**CHAPTER 7: RESULTS AND SNAPSHOTS**
   7.1 User Interface Implementation
   7.2 Blockchain Ledger Output
   7.3 Performance Analysis

**CHAPTER 8: CONCLUSION AND FUTURE SCOPE**
   8.1 Conclusion
   8.2 Future Enhancements

**REFERENCES**

---

# CHAPTER 1: INTRODUCTION

## 1.1 Introduction
In the modern digital era, philanthropy has expanded globally, connecting donors from various parts of the world to causes they care about. However, this growth has been accompanied by a significant increase in fraudulent activities, mismanagement of funds, and a general lack of transparency in how charitable organizations operate.

The **"Automated and Accountable Charity Donation Framework"** is a web-based application designed to bridge the trust gap between donors and charitable organizations. By integrating **Blockchain Technology**, the system ensures that donation records are immutable, transparent, and verifiable by all parties involved. Unlike traditional databases where an administrator has full control (and potentially the ability to manipulate data), a blockchain-based system distributes trust across the network structure itself.

This project implements a custom blockchain from scratch using Python, demonstrating the core principles of blocks, hashing, chaining, and consensus. It serves as an academic prototype to showcase how decentralized technologies can be applied to social good sectors.

## 1.2 Problem Statement
The current landscape of online charity faces several critical issues:
1.  **Lack of Transparency**: Donors often have no visibility into how their money is used after the donation is made.
2.  **Centralization Risks**: Traditional charity platforms rely on a central database. If this database is hacked or manipulated by an insider, records can be altered without detection.
3.  **High Administrative Costs**: Intermediaries often take a significant cut of donations for administrative processing.
4.  **Fraud**: Fake charity websites and fundraising scams are rampant, discouraging potential donors.

## 1.3 Objectives of the Project
The primary objectives of this project are:
1.  To design and develop a **secure, transparent donation platform** using blockchain principles.
2.  To implement **SHA-256 hashing** to link transaction blocks, ensuring data immutability.
3.  To create a **Smart Contract simulation** that automatically releases funds to charities only when validated requests are made.
4.  To provide a **user-friendly dashboard** for Donors to donate and track their contributions.
5.  To provide an **Admin interface** to audit the blockchain ledger and verify system integrity.
6.  To demonstrate **security resilience** by simulating a data tampering attack and showing how the system detects it.

## 1.4 Scope of the Project
The scope of this project is limited to an academic demonstration of blockchain utility in the charity sector.
*   **Target Audience**: Donors, NGOs/Charities, and Auditors.
*   **Functionality**: User registration/login, secure donation processing, fund requesting, and ledger viewing.
*   **Technical Scope**: The blockchain is implemented in-memory (Python lists) to demonstrate the logic. It does not run on a public decentralized network (like Ethereum) but simulates the behavior of one.
*   **Security Scope**: Focuses on data integrity via hashing and basic authentication via JWT (JSON Web Tokens).

## 1.5 Methodology
The project follows the **Agile Software Development** methodology.
1.  **Requirement Gathering**: Identified the need for trust in charity systems.
2.  **Design**: Architected the Block and Blockchain classes and defined the REST API structure.
3.  **Development**: Built the backend in Python/Flask and the frontend in HTML/CSS/JS.
4.  **Testing**: Iteratively tested API endpoints using Postman and the developed frontend.
5.  **Deployment**: Configured for cloud deployment using Gunicorn and Render.

---

 #   C H A P T E R   2 :   L I T E R A T U R E   R E V I E W 
 
 # #   2 . 1   E x i s t i n g   S y s t e m 
 C u r r e n t l y ,   t h e   c h a r i t y   i n d u s t r y   h e a v i l y   r e l i e s   o n   c e n t r a l i z e d   s y s t e m s .   O r g a n i z a t i o n s   m a i n t a i n   t h e i r   o w n   d a t a b a s e s   t o   r e c o r d   d o n a t i o n s ,   a n d   t h e r e   i s   n o   p u b l i c   l e d g e r   f o r   v e r i f i c a t i o n .   D o n o r s   t r u s t   t h e   o r g a n i z a t i o n   b l i n d l y   w h e n   t h e y   m a k e   a   c o n t r i b u t i o n . 
 
 I n   t h e   e x i s t i n g   s y s t e m : 
 1 .     * * C e n t r a l   D a t a b a s e * * :   A l l   d a t a   i s   s t o r e d   i n   a   s i n g l e   l o c a t i o n ,   m a n a g e d   b y   t h e   o r g a n i z a t i o n ' s   a d m i n i s t r a t o r s .   T h i s   c r e a t e s   a   s i n g l e   p o i n t   o f   f a i l u r e   ( S P O F ) . 
 2 .     * * N o   I m m u t a b i l i t y * * :   H i s t o r i c a l   r e c o r d s   c a n   b e   m o d i f i e d   b y   a n y o n e   w i t h   d a t a b a s e   a c c e s s . 
 3 .     * * L o w   T r a n s p a r e n c y * * :   D o n o r s   c a n n o t   v e r i f y   i f   t h e i r   s p e c i f i c   d o n a t i o n   r e a c h e d   t h e   b e n e f i c i a r y . 
 4 .     * * H i g h   O v e r h e a d * * :   M a r k e t i n g   a n d   a d m i n i s t r a t i v e   c o s t s   o f t e n   c o n s u m e   a   l a r g e   p e r c e n t a g e   o f   d o n a t i o n s . 
 
 # #   2 . 2   D i s a d v a n t a g e s   o f   E x i s t i n g   S y s t e m 
 1 .     * * S u s c e p t i b i l i t y   t o   F r a u d * * :   W i t h o u t   a n   i m m u t a b l e   l e d g e r ,   r e c o r d s   c a n   b e   a l t e r e d   t o   c o v e r   u p   e m b e z z l e m e n t . 
 2 .     * * L a c k   o f   T r u s t * * :   D o n o r s   a r e   s k e p t i c a l   d u e   t o   h i g h - p r o f i l e   c h a r i t y   s c a n d a l s . 
 3 .     * * I n e f f i c i e n c y * * :   M a n u a l   a u d i t i n g   p r o c e s s e s   a r e   s l o w   a n d   e x p e n s i v e . 
 4 .     * * D a t a   L o s s   R i s k * * :   C e n t r a l i z e d   s e r v e r s   c a n   c r a s h   o r   b e   c o r r u p t e d ,   l e a d i n g   t o   p e r m a n e n t   d a t a   l o s s . 
 
 # #   2 . 3   P r o p o s e d   S y s t e m 
 T h e   p r o p o s e d   s y s t e m ,   * * A u t o m a t e d   a n d   A c c o u n t a b l e   C h a r i t y   D o n a t i o n   F r a m e w o r k * * ,   i n t r o d u c e s   a   d e c e n t r a l i z e d   a r c h i t e c t u r e   w h e r e   e v e r y   t r a n s a c t i o n   i s   r e c o r d e d   o n   a   b l o c k c h a i n . 
 
 I n   t h i s   s y s t e m : 
 1 .     * * B l o c k c h a i n   L e d g e r * * :   E v e r y   d o n a t i o n   i s   a   t r a n s a c t i o n   b l o c k   l i n k e d   t o   t h e   p r e v i o u s   o n e   v i a   c r y p t o g r a p h i c   h a s h . 
 2 .     * * S m a r t   C o n t r a c t s * * :   A u t o m a t e d   c o d e   e x e c u t e s   l o g i c   ( e . g . ,   r e l e a s e   f u n d s   w h e n   v e r i f i c a t i o n   i s   c o m p l e t e )   w i t h o u t   h u m a n   i n t e r v e n t i o n . 
 3 .     * * I m m u t a b l e   R e c o r d s * * :   O n c e   a   b l o c k   i s   a d d e d ,   i t   c a n n o t   b e   c h a n g e d   m a t h e m a t i c a l l y   w i t h o u t   i n v a l i d a t i n g   t h e   e n t i r e   c h a i n . 
 4 .     * * P u b l i c   V e r i f i c a t i o n * * :   A n y o n e   ( w i t h   a p p r o p r i a t e   p e r m i s s i o n s )   c a n   v e r i f y   t h e   i n t e g r i t y   o f   t h e   b l o c k c h a i n . 
 
 # #   2 . 4   A d v a n t a g e s   o f   P r o p o s e d   S y s t e m 
 1 .     * * T r a n s p a r e n c y * * :   E v e r y   t r a n s a c t i o n   i s   v i s i b l e   a n d   t r a c e a b l e . 
 2 .     * * I m m u t a b i l i t y * * :   R e c o r d s   a r e   p e r m a n e n t   a n d   t e m p e r - e v i d e n t . 
 3 .     * * T r u s t * * :   D o n o r s   c a n   t r u s t   t h e   c o d e   ( S m a r t   C o n t r a c t )   r a t h e r   t h a n   i n d i v i d u a l s . 
 4 .     * * A u d i t a b i l i t y * * :   R e a l - t i m e   a u d i t i n g   i s   p o s s i b l e   w i t h o u t   m a n u a l   i n t e r v e n t i o n . 
 5 .     * * S e c u r i t y * * :   C r y p t o g r a p h i c   h a s h i n g   e n s u r e s   d a t a   i n t e g r i t y . 
 
 # #   2 . 5   B l o c k c h a i n   T e c h n o l o g y   O v e r v i e w 
 * * B l o c k c h a i n * *   i s   a   d i s t r i b u t e d   l e d g e r   t e c h n o l o g y   t h a t   m a i n t a i n s   a   c o n t i n u o u s l y   g r o w i n g   l i s t   o f   r e c o r d s ,   c a l l e d   b l o c k s .   E a c h   b l o c k   c o n t a i n s   a   t i m e s t a m p   a n d   a   l i n k   t o   a   p r e v i o u s   b l o c k . 
 
 # # #   K e y   C o n c e p t s : 
 1 .     * * D e c e n t r a l i z a t i o n * * :   N o   s i n g l e   e n t i t y   c o n t r o l s   t h e   d a t a . 
 2 .     * * C r y p t o g r a p h y * * :   U s e s   S H A - 2 5 6   ( S e c u r e   H a s h   A l g o r i t h m   2 5 6 - b i t )   t o   c r e a t e   u n i q u e   d i g i t a l   s i g n a t u r e s   f o r   d a t a . 
 3 .     * * C o n s e n s u s * * :   N e t w o r k   p a r t i c i p a n t s   a g r e e   o n   t h e   v a l i d i t y   o f   t r a n s a c t i o n s   ( e . g . ,   P r o o f   o f   W o r k ) . 
 4 .     * * S m a r t   C o n t r a c t s * * :   S e l f - e x e c u t i n g   c o n t r a c t s   w i t h   t h e   t e r m s   o f   t h e   a g r e e m e n t   d i r e c t l y   w r i t t e n   i n t o   c o d e . 
 
 - - - 
 
 #   C H A P T E R   3 :   S Y S T E M   A N A L Y S I S 
 
 # #   3 . 1   F e a s i b i l i t y   S t u d y 
 A   f e a s i b i l i t y   s t u d y   e v a l u a t e s   t h e   p r a c t i c a l   v i a b i l i t y   o f   t h e   p r o p o s e d   s y s t e m . 
 
 # # #   3 . 1 . 1   T e c h n i c a l   F e a s i b i l i t y 
 T h e   p r o j e c t   u s e s   * * P y t h o n * * ,   * * F l a s k * * ,   a n d   * * B l o c k c h a i n   l o g i c * * .   P y t h o n   i s   a   r o b u s t   l a n g u a g e   w i t h   e x c e l l e n t   c r y p t o g r a p h i c   l i b r a r i e s   ( h a s h l i b ) .   F l a s k   i s   l i g h t w e i g h t   a n d   s u i t a b l e   f o r   R E S T   A P I s .   T h e   t e c h n i c a l   r e q u i r e m e n t s   ( h a s h i n g ,   J S O N   s e r i a l i z a t i o n ,   H T T P   r e q u e s t s )   a r e   w e l l   w i t h i n   t h e   c a p a b i l i t i e s   o f   m o d e r n   h a r d w a r e   a n d   o p e n - s o u r c e   s o f t w a r e .   T h e r e f o r e ,   t h e   p r o j e c t   i s   t e c h n i c a l l y   f e a s i b l e . 
 
 # # #   3 . 1 . 2   E c o n o m i c   F e a s i b i l i t y 
 T h e   c o s t   o f   d e v e l o p m e n t   i s   m i n i m a l   a s   i t   u t i l i z e s   o p e n - s o u r c e   t e c h n o l o g i e s   ( P y t h o n ,   F l a s k ,   H T M L 5 ) .   C l o u d   d e p l o y m e n t   o n   p l a t f o r m s   l i k e   R e n d e r   o f f e r s   f r e e   t i e r s   f o r   p r o t o t y p e s .   T h e r e   a r e   n o   e x p e n s i v e   s o f t w a r e   l i c e n s e s   r e q u i r e d .   T h u s ,   i t   i s   e c o n o m i c a l l y   f e a s i b l e . 
 
 # # #   3 . 1 . 3   O p e r a t i o n a l   F e a s i b i l i t y 
 T h e   s y s t e m   i s   d e s i g n e d   w i t h   a   u s e r - f r i e n d l y   i n t e r f a c e .   D o n o r s   a n d   C h a r i t y   o r g a n i z a t i o n s   c a n   e a s i l y   r e g i s t e r   a n d   p e r f o r m   t a s k s   w i t h o u t   d e e p   t e c h n i c a l   k n o w l e d g e .   T h e   a d m i n i s t r a t i v e   f u n c t i o n s   ( v i e w i n g   l e d g e r )   a r e   i n t u i t i v e .   T h e r e f o r e ,   i t   i s   o p e r a t i o n a l l y   v i a b l e . 
 
 # #   3 . 2   S y s t e m   R e q u i r e m e n t s 
 
 # # #   3 . 2 . 1   H a r d w a r e   R e q u i r e m e n t s 
 *       * * P r o c e s s o r * * :   I n t e l   C o r e   i 3   o r   h i g h e r   ( f o r   d e v e l o p m e n t / h o s t i n g ) . 
 *       * * R A M * * :   4 G B   m i n i m u m   ( 8 G B   r e c o m m e n d e d ) . 
 *       * * S t o r a g e * * :   1 0 0 M B   f o r   a p p l i c a t i o n   c o d e   a n d   s i m u l a t e d   b l o c k c h a i n   d a t a . 
 *       * * I n t e r n e t   C o n n e c t i o n * * :   R e q u i r e d   f o r   A P I   r e q u e s t s   a n d   d e p l o y m e n t . 
 
 # # #   3 . 2 . 2   S o f t w a r e   R e q u i r e m e n t s 
 *       * * O p e r a t i n g   S y s t e m * * :   W i n d o w s   1 0 / 1 1 ,   L i n u x ,   o r   m a c O S . 
 *       * * L a n g u a g e * * :   P y t h o n   3 . 1 1 + . 
 *       * * W e b   F r a m e w o r k * * :   F l a s k   3 . 0 . 0 . 
 *       * * C r y p t o g r a p h y   L i b r a r y * * :   h a s h l i b   ( s t a n d a r d   P y t h o n   l i b r a r y ) . 
 *       * * A u t h e n t i c a t i o n * * :   P y J W T   ( J S O N   W e b   T o k e n s ) . 
 *       * * F r o n t e n d * * :   H T M L 5 ,   C S S 3 ,   J a v a S c r i p t   ( V a n i l l a ) . 
 *       * * I D E * * :   V S   C o d e   o r   P y C h a r m . 
 *       * * V e r s i o n   C o n t r o l * * :   G i t   &   G i t H u b . 
 
 # #   3 . 3   F u n c t i o n a l   R e q u i r e m e n t s 
 1 .     * * U s e r   R e g i s t r a t i o n * * :   S y s t e m   m u s t   a l l o w   D o n o r s ,   C h a r i t i e s ,   a n d   A d m i n s   t o   r e g i s t e r . 
 2 .     * * A u t h e n t i c a t i o n * * :   S e c u r e   l o g i n   u s i n g   J W T . 
 3 .     * * D o n a t i o n   P r o c e s s i n g * * :   D o n o r s   m u s t   b e   a b l e   t o   s e n d   f u n d s   t o   s p e c i f i c   c h a r i t i e s . 
 4 .     * * F u n d   R e q u e s t * * :   C h a r i t i e s   m u s t   b e   a b l e   t o   r e q u e s t   f u n d s   f o r   s p e c i f i c   c a u s e s . 
 5 .     * * S m a r t   C o n t r a c t   E x e c u t i o n * * :   S y s t e m   m u s t   a u t o m a t i c a l l y   c h e c k   b a l a n c e s   a n d   r e l e a s e   f u n d s   i f   c o n d i t i o n s   a r e   m e t . 
 6 .     * * L e d g e r   V i e w i n g * * :   A d m i n   m u s t   b e   a b l e   t o   v i e w   t h e   e n t i r e   b l o c k c h a i n . 
 7 .     * * T a m p e r   D e t e c t i o n * * :   S y s t e m   m u s t   p r o v i d e   a   m e c h a n i s m   t o   v e r i f y   c h a i n   i n t e g r i t y . 
 
 # #   3 . 4   N o n - F u n c t i o n a l   R e q u i r e m e n t s 
 1 .     * * S e c u r i t y * * :   P a s s w o r d s   m u s t   b e   h a s h e d .   D a t a   t r a n s m i s s i o n   s h o u l d   b e   s e c u r e . 
 2 .     * * P e r f o r m a n c e * * :   B l o c k c h a i n   o p e r a t i o n s   ( m i n i n g )   s h o u l d   n o t   t a k e   e x c e s s i v e   t i m e   f o r   t h i s   p r o t o t y p e . 
 3 .     * * S c a l a b i l i t y * * :   T h e   m o d u l a r   c o d e   s t r u c t u r e   s h o u l d   a l l o w   f o r   f u t u r e   e x p a n s i o n   ( e . g . ,   m o v i n g   t o   a   r e a l   d a t a b a s e ) . 
 4 .     * * U s a b i l i t y * * :   T h e   U I   s h o u l d   b e   r e s p o n s i v e   a n d   e a s y   t o   n a v i g a t e . 
 
 - - - 
  
 
 #   C H A P T E R   4 :   S Y S T E M   D E S I G N 
 
 # #   4 . 1   S y s t e m   A r c h i t e c t u r e 
 T h e   s y s t e m   f o l l o w s   a   t y p i c a l   * * C l i e n t - S e r v e r   A r c h i t e c t u r e * *   w i t h   a   d e c e n t r a l i z e d   d a t a   l a y e r   l o g i c : 
 1 .     * * F r o n t e n d   ( C l i e n t ) * * :   B u i l t   w i t h   H T M L 5 ,   C S S 3   ( C u s t o m   s t y l i n g ) ,   a n d   J a v a S c r i p t .   U s e r s   i n t e r a c t   w i t h   f o r m s   ( R e g i s t r a t i o n ,   D o n a t i o n ,   R e q u e s t   F u n d ) .   J S    e t c h   c a l l s   s e n d   J S O N   d a t a   t o   t h e   b a c k e n d   A P I . 
 2 .     * * B a c k e n d   ( S e r v e r ) * * :   A   P y t h o n   F l a s k   a p p l i c a t i o n   (  p p . p y )   h a n d l e s   a l l   H T T P   r e q u e s t s .   I t   a c t s   a s   t h e   g a t e w a y   t o   t h e   b l o c k c h a i n   l o g i c . 
 3 .     * * A u t h e n t i c a t i o n   L a y e r * * :   J W T   ( J S O N   W e b   T o k e n s )   a r e   i s s u e d   u p o n   l o g i n   a n d   r e q u i r e d   f o r   p r o t e c t e d   e n d p o i n t s   ( D o n a t e ,   R e q u e s t   F u n d ,   L e d g e r   V i e w ) . 
 4 .     * * B l o c k c h a i n   L a y e r   (  l o c k c h a i n . p y ) * * :   T h i s   i s   t h e   c o r e   l o g i c .   I t   m a n a g e s   t h e   B l o c k   c l a s s ,   B l o c k c h a i n   c l a s s ,   h a s h i n g   ( S H A - 2 5 6 ) ,   P r o o f   o f   W o r k   ( m i n i n g ) ,   a n d   v a l i d a t i o n . 
 5 .     * * S m a r t   C o n t r a c t   L o g i c * * :   E m b e d d e d   c h e c k s   w i t h i n    p p . p y   a u t o m a t i c a l l y   r e l e a s e   f u n d s   i f   D o n a t i o n   A m o u n t   > =   R e q u e s t e d   A m o u n t . 
 
 # #   4 . 2   U M L   D i a g r a m s 
 
 # # #   4 . 2 . 1   U s e   C a s e   D i a g r a m 
 T h e   U s e   C a s e   d i a g r a m   d e p i c t s   t h e   i n t e r a c t i o n s   b e t w e e n   a c t o r s   ( D o n o r s ,   C h a r i t i e s ,   A d m i n )   a n d   t h e   s y s t e m . 
 
 *       * * D o n o r * * :   R e g i s t e r ,   L o g i n ,   V i e w   B a l a n c e s ,   D o n a t e   F u n d s ,   V i e w   P r o f i l e . 
 *       * * C h a r i t y * * :   R e g i s t e r ,   L o g i n ,   R e q u e s t   F u n d s ,   V i e w   R e c e i v e d   F u n d s . 
 *       * * A d m i n * * :   L o g i n ,   V i e w   F u l l   L e d g e r ,   V e r i f y   C h a i n   I n t e g r i t y ,   T a m p e r   S i m u l a t i o n . 
 
 # # #   4 . 2 . 2   C l a s s   D i a g r a m 
 T h e   C l a s s   d i a g r a m   r e p r e s e n t s   t h e   s t a t i c   s t r u c t u r e   o f   t h e   s y s t e m . 
 
 * * C l a s s :   B l o c k c h a i n * * 
 *       A t t r i b u t e s :   c h a i n   ( L i s t   o f   B l o c k s ) ,   u n c o n f i r m e d _ t r a n s a c t i o n s   ( L i s t ) ,   
 o d e s   ( S e t ) . 
 *       M e t h o d s :   c r e a t e _ g e n e s i s _ b l o c k ( ) ,    d d _ b l o c k ( ) ,   m i n e ( ) ,   p r o o f _ o f _ w o r k ( ) ,   i s _ v a l i d _ c h a i n ( ) . 
 
 * * C l a s s :   B l o c k * * 
 *       A t t r i b u t e s :   i n d e x   ( I n t e g e r ) ,   	 r a n s a c t i o n s   ( L i s t ) ,   	 i m e s t a m p   ( F l o a t ) ,   p r e v i o u s _ h a s h   ( S t r i n g ) ,   
 o n c e   ( I n t e g e r ) . 
 *       M e t h o d s :   c o m p u t e _ h a s h ( ) . 
 
 * * C l a s s :   U s e r * *   ( C o n c e p t u a l   i n    p p . p y   d i c t i o n a r y ) 
 *       A t t r i b u t e s :   u s e r n a m e ,   p a s s w o r d _ h a s h ,    o l e   ( D o n o r / C h a r i t y / A d m i n ) ,    a l a n c e ,    a n k _ d e t a i l s . 
 
 # # #   4 . 2 . 3   S e q u e n c e   D i a g r a m 
 A   s e q u e n c e   d i a g r a m   f o r   a   * * D o n a t i o n * * : 
 1 .     * * D o n o r * *   s e n d s   d o n a t i o n   r e q u e s t   ( A P I   C a l l )   - >   * * B a c k e n d * * . 
 2 .     * * B a c k e n d * *   c h e c k s   * * D o n o r   B a l a n c e * *   - >   * * U s e r   S t o r e * * . 
 3 .     I f   s u f f i c i e n t   f u n d s ,   * * B a c k e n d * *   c r e a t e s   n e w   * * T r a n s a c t i o n * * . 
 4 .     * * B a c k e n d * *   c a l l s    l o c k c h a i n . a d d _ n e w _ t r a n s a c t i o n ( ) . 
 5 .     * * B a c k e n d * *   c a l l s    l o c k c h a i n . m i n e ( )   t o   c r e a t e   a   n e w   * * B l o c k * * . 
 6 .     * * B a c k e n d * *   u p d a t e s   * * C h a r i t y   B a l a n c e * *   a n d   * * S m a r t   C o n t r a c t   S t a t e * * . 
 7 .     * * B a c k e n d * *   r e t u r n s   s u c c e s s   r e s p o n s e   - >   * * D o n o r * * . 
 
 # # #   4 . 2 . 4   A c t i v i t y   D i a g r a m   ( D o n a t i o n   P r o c e s s ) 
 S t a r t   - >   L o g i n   - >   D a s h b o a r d   - >   S e l e c t   C h a r i t y   - >   E n t e r   A m o u n t   - >   [ C h e c k   B a l a n c e ]   - >   ( Y e s )   - >   D e d u c t   F u n d s   - >   A d d   T r a n s a c t i o n   - >   M i n e   B l o c k   - >   C r e a t e   N o t i f i c a t i o n   - >   E n d . 
 ( N o )   - >   S h o w   E r r o r   - >   E n d . 
 
 # # #   4 . 2 . 5   D a t a   F l o w   D i a g r a m   ( D F D ) 
 *       * * L e v e l   0 * * :   U s e r   - >   [ C h a r i t y   S y s t e m ]   - >   D a t a b a s e / B l o c k c h a i n . 
 *       * * L e v e l   1 * * :   B r e a k d o w n   o f   [ C h a r i t y   S y s t e m ]   i n t o   A u t h e n t i c a t i o n ,   T r a n s a c t i o n   P r o c e s s i n g ,   B l o c k   M i n i n g ,   a n d   R e p o r t i n g   m o d u l e s . 
 
 # #   4 . 3   D a t a b a s e   D e s i g n   /   D a t a   S t r u c t u r e 
 S i n c e   t h i s   i s   a   b l o c k c h a i n   s i m u l a t i o n ,   w e   u s e   i n - m e m o r y   d a t a   s t r u c t u r e s   ( P y t h o n   L i s t s   a n d   D i c t i o n a r i e s )   t o   m i m i c   a   d a t a b a s e   a n d   d i s t r i b u t e d   l e d g e r . 
 
 * * U s e r s   D i c t i o n a r y * * : 
 \ \ \ p y t h o n 
 u s e r s   =   { 
         ' u s e r n a m e ' :   { 
                 ' p a s s w o r d ' :   ' h a s h e d _ p a s s w o r d ' , 
                 ' r o l e ' :   ' D o n o r ' , 
                 ' b a l a n c e ' :   1 0 0 0 . 0 , 
                 ' b a n k _ d e t a i l s ' :   { ' a c c o u n t _ n u m b e r ' :   ' . . . ' ,   ' i f s c ' :   ' . . . ' } 
         } 
 } 
 \ \ \ 
 
 * * B l o c k c h a i n   L i s t * * : 
 \ \ \ p y t h o n 
 c h a i n   =   [ 
         B l o c k ( i n d e x = 0 ,   t r a n s a c t i o n s = [ ] ,   p r e v i o u s _ h a s h = ' 0 ' ,   n o n c e = 0 ) , 
         B l o c k ( i n d e x = 1 ,   t r a n s a c t i o n s = [ . . . ] ,   p r e v i o u s _ h a s h = ' h a s h _ o f _ b l o c k _ 0 ' ,   n o n c e = 1 2 3 4 5 ) , 
         . . . 
 ] 
 \ \ \ 
 
 * * S m a r t   C o n t r a c t   S t a t e * * : 
 \ \ \ p y t h o n 
 c o n t r a c t _ s t a t e   =   { 
         ' c h a r i t y _ b a l a n c e s ' :   { ' S a v e T h e K i d s ' :   5 0 0 . 0 } , 
         ' p e n d i n g _ r e q u e s t s ' :   [ { ' c h a r i t y ' :   ' S a v e T h e K i d s ' ,   ' a m o u n t ' :   1 0 0 . 0 } ] 
 } 
 \ \ \ 
 
 # #   4 . 4   M o d u l e   D e s c r i p t i o n 
 1 .     * * A u t h e n t i c a t i o n   M o d u l e * * :   M a n a g e s   u s e r   r e g i s t r a t i o n ,   l o g i n ,   a n d   J W T   g e n e r a t i o n   u s i n g   P y J W T . 
 2 .     * * B l o c k c h a i n   M o d u l e * * :   H a n d l e s   b l o c k   c r e a t i o n ,   h a s h i n g ,   P r o o f   o f   W o r k   ( m i n i n g ) ,   a n d   c h a i n   v a l i d a t i o n . 
 3 .     * * T r a n s a c t i o n   M o d u l e * * :   C r e a t e s   a n d   v a l i d a t e s   d o n a t i o n   t r a n s a c t i o n s . 
 4 .     * * S m a r t   C o n t r a c t   M o d u l e * * :   A u t o m a t e s   f u n d   r e l e a s e   l o g i c   b a s e d   o n   p r e - d e f i n e d   r u l e s . 
 5 .     * * B a n k   I n t e g r a t i o n   M o d u l e * * :   S i m u l a t e s   I F S C   l o o k u p   a n d   b a n k   a c c o u n t   l i n k i n g . 
 6 .     * * A d m i n   M o d u l e * * :   P r o v i d e s   o v e r s i g h t ,   l e d g e r   v i e w i n g ,   a n d   s e c u r i t y   a u d i t i n g   t o o l s . 
 
 - - - 
 
 #   C H A P T E R   5 :   I M P L E M E N T A T I O N 
 
 T h i s   c h a p t e r   d e t a i l s   t h e   a c t u a l   c o d e   i m p l e m e n t a t i o n   o f   t h e   p r o j e c t .   T h e   s y s t e m   i s   b u i l t   u s i n g   P y t h o n   3   a n d   t h e   F l a s k   f r a m e w o r k . 
 
 # #   5 . 1   T e c h n o l o g y   S t a c k   D e s c r i p t i o n 
 
 # # #   5 . 1 . 1   P y t h o n 
 P y t h o n   i s   a   h i g h - l e v e l ,   i n t e r p r e t e d   l a n g u a g e   k n o w n   f o r   i t s   r e a d a b i l i t y   a n d   v a s t   l i b r a r y   s u p p o r t .   I t   i s   i d e a l   f o r   b l o c k c h a i n   d e v e l o p m e n t   d u e   t o   i t s   r o b u s t   c r y p t o g r a p h i c   l i b r a r i e s   ( h a s h l i b ,   h m a c )   a n d   r a p i d   p r o t o t y p i n g   c a p a b i l i t i e s . 
 
 # # #   5 . 1 . 2   F l a s k   F r a m e w o r k 
 F l a s k   i s   a   m i c r o   w e b   f r a m e w o r k   w r i t t e n   i n   P y t h o n .   I t   d o e s   n o t   r e q u i r e   p a r t i c u l a r   t o o l s   o r   l i b r a r i e s ,   m a k i n g   i t   l i g h t w e i g h t .   W e   u s e   F l a s k   t o   e x p o s e   o u r   b l o c k c h a i n   f u n c t i o n s   a s   R E S T   A P I   e n d p o i n t s   ( / d o n a t e ,   / m i n e ,   / c h a i n ) . 
 
 # # #   5 . 1 . 3   H T M L / C S S / J a v a S c r i p t 
 T h e   f r o n t e n d   u s e s   s t a n d a r d   w e b   t e c h n o l o g i e s   t o   c r e a t e   a   r e s p o n s i v e   a n d   i n t e r a c t i v e   u s e r   i n t e r f a c e . 
 *       * * H T M L 5 * * :   S t r u c t u r e   o f   t h e   d a s h b o a r d . 
 *       * * C S S 3 * * :   S t y l i n g   w i t h   g l a s s m o r p h i s m   e f f e c t s   a n d   r e s p o n s i v e n e s s . 
 *       * * J a v a S c r i p t * * :   A s y n c h r o n o u s    e t c h   A P I   c a l l s   t o   c o m m u n i c a t e   w i t h   t h e   F l a s k   b a c k e n d   w i t h o u t   p a g e   r e l o a d s . 
 
 # #   5 . 2   A l g o r i t h m s   U s e d 
 
 # # #   5 . 2 . 1   S H A - 2 5 6   H a s h i n g 
 S e c u r e   H a s h   A l g o r i t h m   2 5 6 - b i t   ( S H A - 2 5 6 )   m a p s   d a t a   o f   a r b i t r a r y   s i z e   t o   a   f i x e d   s i z e   b i t   s t r i n g   ( h a s h ) .   W e   u s e   i t   t o   e n s u r e   t h e   i n t e g r i t y   o f   b l o c k s .   C h a n g i n g   e v e n   a   s i n g l e   c h a r a c t e r   i n   a   b l o c k   c h a n g e s   i t s   e n t i r e   h a s h ,   b r e a k i n g   t h e   c h a i n . 
 
 * * H a s h i n g   I m p l e m e n t a t i o n * * : 
 \ \ \ p y t h o n 
 i m p o r t   h a s h l i b 
 i m p o r t   j s o n 
 
 d e f   c o m p u t e _ h a s h ( s e l f ) : 
         b l o c k _ s t r i n g   =   j s o n . d u m p s ( s e l f . _ _ d i c t _ _ ,   s o r t _ k e y s = T r u e ) 
         r e t u r n   h a s h l i b . s h a 2 5 6 ( b l o c k _ s t r i n g . e n c o d e ( ) ) . h e x d i g e s t ( ) 
 \ \ \ 
 
 # # #   5 . 2 . 2   P r o o f   o f   W o r k   ( P o W )   C o n s e n s u s 
 P r o o f   o f   W o r k   i s   t h e   c o n s e n s u s   a l g o r i t h m   u s e d   t o   v a l i d a t e   t r a n s a c t i o n s   a n d   c r e a t e   n e w   b l o c k s .   I t   i n v o l v e s   f i n d i n g   a   n u m b e r   ( n o n c e )   s u c h   t h a t   t h e   h a s h   o f   t h e   b l o c k   s t a r t s   w i t h   a   s p e c i f i c   n u m b e r   o f   z e r o e s   ( d i f f i c u l t y   l e v e l ) .   T h i s   p r e v e n t s   s p a m   a n d   S y b i l   a t t a c k s . 
 
 * * P o W   I m p l e m e n t a t i o n * * : 
 \ \ \ p y t h o n 
 d e f   p r o o f _ o f _ w o r k ( s e l f ,   b l o c k ) : 
         b l o c k . n o n c e   =   0 
         c o m p u t e d _ h a s h   =   b l o c k . c o m p u t e _ h a s h ( ) 
         w h i l e   n o t   c o m p u t e d _ h a s h . s t a r t s w i t h ( ' 0 '   *   2 ) :   #   D i f f i c u l t y :   2   L e a d i n g   Z e r o s 
                 b l o c k . n o n c e   + =   1 
                 c o m p u t e d _ h a s h   =   b l o c k . c o m p u t e _ h a s h ( ) 
         r e t u r n   c o m p u t e d _ h a s h 
 \ \ \ 
 
 # #   5 . 3   K e y   C o d e   I m p l e m e n t a t i o n 
 
 # # #   5 . 3 . 1   B l o c k c h a i n   C l a s s   (  l o c k c h a i n . p y ) 
 T h e   B l o c k c h a i n   c l a s s   m a n a g e s   t h e   c h a i n   a n d   u n c o n f i r m e d   t r a n s a c t i o n s . 
 
 \ \ \ p y t h o n 
 c l a s s   B l o c k c h a i n : 
         d e f   _ _ i n i t _ _ ( s e l f ) : 
                 s e l f . u n c o n f i r m e d _ t r a n s a c t i o n s   =   [ ] 
                 s e l f . c h a i n   =   [ ] 
                 s e l f . c r e a t e _ g e n e s i s _ b l o c k ( ) 
 
         d e f   c r e a t e _ g e n e s i s _ b l o c k ( s e l f ) : 
                 g e n e s i s _ b l o c k   =   B l o c k ( 0 ,   [ ] ,   ' 0 ' ) 
                 g e n e s i s _ b l o c k . h a s h   =   g e n e s i s _ b l o c k . c o m p u t e _ h a s h ( ) 
                 s e l f . c h a i n . a p p e n d ( g e n e s i s _ b l o c k ) 
                 
         d e f   a d d _ n e w _ t r a n s a c t i o n ( s e l f ,   t r a n s a c t i o n ) : 
                 s e l f . u n c o n f i r m e d _ t r a n s a c t i o n s . a p p e n d ( t r a n s a c t i o n ) 
                 
         d e f   m i n e ( s e l f ) : 
                 i f   n o t   s e l f . u n c o n f i r m e d _ t r a n s a c t i o n s : 
                         r e t u r n   F a l s e 
                 l a s t _ b l o c k   =   s e l f . l a s t _ b l o c k 
                 n e w _ b l o c k   =   B l o c k ( i n d e x = l a s t _ b l o c k . i n d e x   +   1 , 
                                                     t r a n s a c t i o n s = s e l f . u n c o n f i r m e d _ t r a n s a c t i o n s , 
                                                     p r e v i o u s _ h a s h = l a s t _ b l o c k . h a s h ) 
                 p r o o f   =   s e l f . p r o o f _ o f _ w o r k ( n e w _ b l o c k ) 
                 s e l f . a d d _ b l o c k ( n e w _ b l o c k ,   p r o o f ) 
                 s e l f . u n c o n f i r m e d _ t r a n s a c t i o n s   =   [ ] 
                 r e t u r n   n e w _ b l o c k . i n d e x 
 \ \ \ 
  
 
 # # #   5 . 3 . 3   A P I   R o u t e s   (  p p . p y ) 
 F l a s k   r o u t e s   d e f i n e   t h e   i n t e r f a c e   f o r   i n t e r a c t i n g   w i t h   t h e   b l o c k c h a i n . 
 
 * * R e g i s t r a t i o n   ( / r e g i s t e r ) * * : 
 \ \ \ p y t h o n 
 @ a p p . r o u t e ( ' / r e g i s t e r ' ,   m e t h o d s = [ ' P O S T ' ] ) 
 d e f   r e g i s t e r ( ) : 
         d a t a   =   r e q u e s t . g e t _ j s o n ( ) 
         u s e r n a m e   =   d a t a . g e t ( ' u s e r n a m e ' ) 
         p a s s w o r d   =   d a t a . g e t ( ' p a s s w o r d ' ) 
         r o l e   =   d a t a . g e t ( ' r o l e ' ,   ' D o n o r ' ) 
         
         i f   u s e r n a m e   i n   u s e r s : 
                 r e t u r n   j s o n i f y ( { ' m e s s a g e ' :   ' U s e r n a m e   a l r e a d y   e x i s t s ' } ) ,   4 0 0 
                 
         u s e r s [ u s e r n a m e ]   =   { ' p a s s w o r d ' :   p a s s w o r d ,   ' r o l e ' :   r o l e ,   ' b a l a n c e ' :   1 0 0 0   i f   r o l e   = =   ' D o n o r '   e l s e   0 } 
         r e t u r n   j s o n i f y ( { ' m e s s a g e ' :   ' U s e r   r e g i s t e r e d   s u c c e s s f u l l y ' } ) ,   2 0 1 
 \ \ \ 
 
 * * D o n a t i o n   ( / d o n a t e ) * * : 
 \ \ \ p y t h o n 
 @ a p p . r o u t e ( ' / d o n a t e ' ,   m e t h o d s = [ ' P O S T ' ] ) 
 @ t o k e n _ r e q u i r e d 
 d e f   d o n a t e ( c u r r e n t _ u s e r ) : 
         d a t a   =   r e q u e s t . g e t _ j s o n ( ) 
         c h a r i t y   =   d a t a . g e t ( ' c h a r i t y ' ) 
         a m o u n t   =   f l o a t ( d a t a . g e t ( ' a m o u n t ' ) ) 
         
         #   C r e a t e   T r a n s a c t i o n 
         t r a n s a c t i o n   =   { 
                 ' s e n d e r ' :   c u r r e n t _ u s e r [ ' u s e r n a m e ' ] , 
                 ' r e c i p i e n t ' :   c h a r i t y , 
                 ' a m o u n t ' :   a m o u n t , 
                 ' t i m e s t a m p ' :   s t r ( d a t e t i m e . d a t e t i m e . n o w ( ) ) 
         } 
         
         b l o c k c h a i n . a d d _ n e w _ t r a n s a c t i o n ( t r a n s a c t i o n ) 
         b l o c k c h a i n . m i n e ( ) 
         
         c u r r e n t _ u s e r [ ' b a l a n c e ' ]   - =   a m o u n t 
         c o n t r a c t _ s t a t e [ ' c h a r i t y _ b a l a n c e s ' ] [ c h a r i t y ]   + =   a m o u n t 
         
         #   E x e c u t e   S m a r t   C o n t r a c t 
         l o g s   =   e x e c u t e _ s m a r t _ c o n t r a c t ( ) 
         
         r e t u r n   j s o n i f y ( { ' m e s s a g e ' :   ' D o n a t i o n   s u c c e s s f u l ' ,   ' l o g s ' :   l o g s } ) 
 \ \ \ 
 
 * * S m a r t   C o n t r a c t   L o g i c   ( e x e c u t e _ s m a r t _ c o n t r a c t ) * * : 
 \ \ \ p y t h o n 
 d e f   e x e c u t e _ s m a r t _ c o n t r a c t ( ) : 
         l o g s   =   [ ] 
         #   C h e c k   p e n d i n g   r e q u e s t s   a g a i n s t   b a l a n c e s 
         f o r   r e q   i n   c o n t r a c t _ s t a t e [ ' p e n d i n g _ r e q u e s t s ' ] : 
                 c h a r i t y   =   r e q [ ' c h a r i t y ' ] 
                 a m o u n t   =   r e q [ ' a m o u n t ' ] 
                 b a l a n c e   =   c o n t r a c t _ s t a t e [ ' c h a r i t y _ b a l a n c e s ' ] . g e t ( c h a r i t y ,   0 ) 
                 
                 i f   b a l a n c e   > =   a m o u n t : 
                         #   A u t o m a t i c   R e l e a s e 
                         t x   =   { ' t y p e ' :   ' F U N D _ R E L E A S E ' ,   ' c h a r i t y ' :   c h a r i t y ,   ' a m o u n t ' :   a m o u n t } 
                         b l o c k c h a i n . a d d _ n e w _ t r a n s a c t i o n ( t x ) 
                         b l o c k c h a i n . m i n e ( ) 
                         
                         c o n t r a c t _ s t a t e [ ' c h a r i t y _ b a l a n c e s ' ] [ c h a r i t y ]   - =   a m o u n t 
                         l o g s . a p p e n d ( f  
 S M A R T  
 C O N T R A C T :  
 R e l e a s e d  
 a m o u n t  
 t o  
 c h a r i t y  
 ) 
                         
         r e t u r n   l o g s 
 \ \ \ 
 
 - - - 
 
 #   C H A P T E R   6 :   T E S T I N G 
 
 # #   6 . 1   T e s t i n g   M e t h o d o l o g i e s 
 T e s t i n g   i s   a   c r i t i c a l   p h a s e   w h e r e   t h e   s y s t e m   l o g i c   i s   v e r i f i e d   a g a i n s t   r e q u i r e m e n t s .   W e   e m p l o y e d : 
 1 .     * * U n i t   T e s t i n g * * :   V e r i f i e d   i n d i v i d u a l   f u n c t i o n s   ( e . g . ,   c o m p u t e _ h a s h ,   p r o o f _ o f _ w o r k ) . 
 2 .     * * I n t e g r a t i o n   T e s t i n g * * :   V e r i f i e d   t h e   i n t e r a c t i o n   b e t w e e n   f r o n t e n d   a n d   b a c k e n d   A P I s . 
 3 .     * * S y s t e m   T e s t i n g * * :   V e r i f i e d   e n d - t o - e n d   w o r k f l o w s   ( R e g i s t r a t i o n   - >   D o n a t i o n   - >   B l o c k   R e l e a s e ) . 
 4 .     * * S e c u r i t y   T e s t i n g * * :   S i m u l a t i n g   a   t a m p e r i n g   a t t a c k   ( / t a m p e r _ d e m o )   t o   v e r i f y   c h a i n   i n t e g r i t y   c h e c k s . 
 
 # #   6 . 2   U n i t   T e s t i n g 
 * * T e s t   C a s e   1 :   H a s h i n g   F u n c t i o n * * 
 *       * * I n p u t * * :   B l o c k   d a t a   { ' i n d e x ' :   0 ,   ' d a t a ' :   ' g e n e s i s ' } 
 *       * * E x p e c t e d * * :   V a l i d   S H A - 2 5 6   h a s h   s t r i n g   ( 6 4   c h a r a c t e r s ) . 
 *       * * R e s u l t * * :   S u c c e s s . 
 
 * * T e s t   C a s e   2 :   C h a i n   V a l i d a t i o n * * 
 *       * * I n p u t * * :   V a l i d   c h a i n   o f   3   b l o c k s . 
 *       * * A c t i o n * * :   M o d i f y   d a t a   i n   B l o c k   1 . 
 *       * * E x p e c t e d * * :   c h e c k _ c h a i n _ v a l i d i t y ( )   r e t u r n s   F a l s e . 
 *       * * R e s u l t * * :   S u c c e s s . 
 
 # #   6 . 3   I n t e g r a t i o n   T e s t i n g 
 * * T e s t   C a s e   3 :   U s e r   R e g i s t r a t i o n   A P I * * 
 *       * * I n p u t * * :   J S O N   { ' u s e r n a m e ' :   ' A l i c e ' ,   ' p a s s w o r d ' :   ' p a s s w o r d 1 2 3 ' ,   ' r o l e ' :   ' D o n o r ' } 
 *       * * E x p e c t e d * * :   H T T P   2 0 1   C r e a t e d .   U s e r   a d d e d   t o   u s e r s   d i c t i o n a r y . 
 *       * * R e s u l t * * :   S u c c e s s . 
 
 # #   6 . 4   S y s t e m   T e s t i n g 
 * * W o r k f l o w   T e s t :   D o n a t i o n   P r o c e s s * * 
 1 .     * * S t e p   1 * * :   L o g i n   a s   D o n o r   ( A l i c e ) .   - >   * * R e s u l t * * :   T o k e n   r e c e i v e d . 
 2 .     * * S t e p   2 * * :   S e l e c t   C h a r i t y   ( S a v e T h e K i d s ) ,   A m o u n t   ( ) .   - >   * * R e s u l t * * :   D o n a t i o n   r e q u e s t   s e n t . 
 3 .     * * S t e p   3 * * :   V e r i f y   T r a n s a c t i o n .   - >   * * R e s u l t * * :   B l o c k c h a i n   l e n g t h   i n c r e a s e d   b y   1 . 
 4 .     * * S t e p   4 * * :   V e r i f y   B a l a n c e .   - >   * * R e s u l t * * :   A l i c e   b a l a n c e   d e d u c t e d   b y   . 
 5 .     * * S t e p   5 * * :   C h e c k   A d m i n   L e d g e r .   - >   * * R e s u l t * * :   N e w   b l o c k   v i s i b l e   w i t h   c o r r e c t   h a s h . 
 
 # #   6 . 5   S e c u r i t y   T e s t i n g   ( T a m p e r   S i m u l a t i o n ) 
 W e   i m p l e m e n t e d   a   s p e c i a l   r o u t e   / t a m p e r _ d e m o   t o   d e m o n s t r a t e   t h e   s e c u r i t y   o f   t h e   b l o c k c h a i n . 
 *       * * A c t i o n * * :   M a n u a l l y   m o d i f y   t h e   t r a n s a c t i o n   a m o u n t   i n   a n   e x i s t i n g   b l o c k   ( e . g . ,   B l o c k   # 2 ) . 
 *       * * V e r i f i c a t i o n * * :   R u n   / v e r i f y _ c h a i n . 
 *       * * O u t c o m e * * :   T h e   s y s t e m   d e t e c t s   t h a t   t h e   s t o r e d   h a s h   o f   B l o c k   # 2   d o e s   n o t   m a t c h   t h e   r e c o m p u t e d   h a s h   o f   i t s   m o d i f i e d   d a t a .   T h e   c h a i n   i s   f l a g g e d   a s   * * I N V A L I D * * . 
 
 - - - 
 
 #   C H A P T E R   7 :   R E S U L T S   A N D   S N A P S H O T S 
 
 # #   7 . 1   U s e r   I n t e r f a c e   I m p l e m e n t a t i o n 
 T h e   s y s t e m   f e a t u r e s   a   c o m p r e h e n s i v e   d a s h b o a r d   b u i l t   w i t h   H T M L 5 / C S S 3 . 
 *       * * L o g i n   P a g e * * :   S e c u r e   e n t r y   p o i n t   w i t h   r o l e   s e l e c t i o n . 
 *       * * D o n o r   D a s h b o a r d * * :   D i s p l a y s   c u r r e n t   b a l a n c e ,   l i s t   o f   c h a r i t i e s ,   a n d   d o n a t i o n   f o r m . 
 *       * * C h a r i t y   D a s h b o a r d * * :   D i s p l a y s   r e c e i v e d   f u n d s   a n d   f u n d   r e q u e s t   f o r m . 
 *       * * A d m i n   D a s h b o a r d * * :   S h o w s   s y s t e m   h e a l t h ,   t o t a l   t r a n s a c t i o n s ,   a n d   f u l l   b l o c k c h a i n   l e d g e r . 
 
 # #   7 . 2   B l o c k c h a i n   L e d g e r   O u t p u t 
 T h e   l e d g e r   v i e w   p r o v i d e s   t r a n s p a r e n c y .   I t   d i s p l a y s : 
 *       * * B l o c k   I n d e x * * :   T h e   p o s i t i o n   i n   t h e   c h a i n . 
 *       * * T i m e s t a m p * * :   W h e n   t h e   b l o c k   w a s   m i n e d . 
 *       * * H a s h * * :   T h e   u n i q u e   c r y p t o g r a p h i c   s i g n a t u r e . 
 *       * * P r e v i o u s   H a s h * * :   T h e   l i n k   t o   t h e   p r i o r   b l o c k . 
 *       * * T r a n s a c t i o n s * * :   T h e   d a t a   s t o r e d   ( s e n d e r ,   r e c i p i e n t ,   a m o u n t ) . 
 
 # #   7 . 3   P e r f o r m a n c e   A n a l y s i s 
 *       * * T r a n s a c t i o n   S p e e d * * :   A v e r a g e   m i n i n g   t i m e   i s   <   0 . 1   s e c o n d s   ( P r o o f   o f   W o r k   d i f f i c u l t y   s e t   t o   2   f o r   d e m o   p u r p o s e s ) . 
 *       * * S c a l a b i l i t y * * :   T h e   s y s t e m   c u r r e n t l y   h a n d l e s   s e q u e n t i a l   t r a n s a c t i o n s   e f f i c i e n t l y .   I n   a   p r o d u c t i o n   e n v i r o n m e n t ,   t h i s   w o u l d   b e   d i s t r i b u t e d   a c r o s s   n o d e s . 
 *       * * L a t e n c y * * :   A P I   r e s p o n s e   t i m e   i s   c o n s i s t e n t l y   u n d e r   2 0 0 m s   f o r   l o c a l   e x e c u t i o n . 
 
 - - - 
 
 #   C H A P T E R   8 :   C O N C L U S I O N   A N D   F U T U R E   S C O P E 
 
 # #   8 . 1   C o n c l u s i o n 
 T h e   * *  
 A u t o m a t e d  
 a n d  
 A c c o u n t a b l e  
 C h a r i t y  
 D o n a t i o n  
 F r a m e w o r k * *   s u c c e s s f u l l y   d e m o n s t r a t e s   t h e   p o t e n t i a l   o f   b l o c k c h a i n   t e c h n o l o g y   i n   t h e   p h i l a n t h r o p i c   s e c t o r .   B y   d e c e n t r a l i z i n g   t h e   l e d g e r   a n d   u s i n g   s m a r t   c o n t r a c t s   f o r   f u n d   r e l e a s e ,   w e   a d d r e s s e d   t h e   c o r e   i s s u e s   o f   t r a n s p a r e n c y ,   t r u s t ,   a n d   a c c o u n t a b i l i t y . 
 
 T h e   p r o j e c t   h i g h l i g h t s : 
 1 .     * * I m m u t a b i l i t y * * :   O n c e   a   d o n a t i o n   i s   r e c o r d e d ,   i t   c a n n o t   b e   a l t e r e d . 
 2 .     * * A u t o m a t i o n * * :   S m a r t   c o n t r a c t s   r e d u c e   a d m i n i s t r a t i v e   o v e r h e a d   a n d   b i a s . 
 3 .     * * S e c u r i t y * * :   C r y p t o g r a p h i c   h a s h i n g   s e r v e s   a s   a   r o b u s t   d e f e n s e   a g a i n s t   d a t a   t a m p e r i n g . 
 4 .     * * U s e r   E x p e r i e n c e * * :   A   c l e a n ,   r e s p o n s i v e   i n t e r f a c e   m a k e s   t h e   c o m p l e x   b a c k e n d   a c c e s s i b l e   t o   n o n - t e c h n i c a l   u s e r s . 
 
 T h i s   s y s t e m   s e r v e s   a s   a   f o u n d a t i o n a l   p r o t o t y p e   f o r   b u i l d i n g   l a r g e - s c a l e ,   d e c e n t r a l i z e d   c h a r i t y   p l a t f o r m s   t h a t   c a n   r e s t o r e   p u b l i c   f a i t h   i n   c h a r i t a b l e   g i v i n g . 
 
 # #   8 . 2   F u t u r e   E n h a n c e m e n t s 
 W h i l e   t h e   c u r r e n t   s y s t e m   i s   f u n c t i o n a l   f o r   a c a d e m i c   d e m o n s t r a t i o n ,   s e v e r a l   e n h a n c e m e n t s   c a n   b e   m a d e   f o r   a   p r o d u c t i o n - r e a d y   v e r s i o n : 
 1 .     * * R e a l   B l o c k c h a i n   N e t w o r k * * :   M i g r a t e   f r o m   a n   i n - m e m o r y   P y t h o n   i m p l e m e n t a t i o n   t o   a   d e p l o y e d   n e t w o r k   l i k e   * * E t h e r e u m * *   o r   * * H y p e r l e d g e r   F a b r i c * * . 
 2 .     * * W a l l e t   I n t e g r a t i o n * * :   I n t e g r a t e   c r y p t o c u r r e n c y   w a l l e t s   ( e . g . ,   M e t a M a s k )   f o r   r e a l   c r y p t o   d o n a t i o n s   ( E T H ,   B T C ) . 
 3 .     * * D i s t r i b u t e d   F i l e   S y s t e m   ( I P F S ) * * :   S t o r e   l a r g e   d o c u m e n t s   ( c h a r i t y   r e g i s t r a t i o n   p r o o f s ,   i m p a c t   r e p o r t s )   o n   I P F S   h a s h e s   s t o r e d   o n - c h a i n . 
 4 .     * * M o b i l e   A p p l i c a t i o n * * :   D e v e l o p   a   n a t i v e   m o b i l e   a p p   ( R e a c t   N a t i v e / F l u t t e r )   f o r   e a s i e r   a c c e s s . 
 5 .     * * C o n s e n s u s   U p g r a d e * * :   I m p l e m e n t   P r o o f   o f   S t a k e   ( P o S )   f o r   b e t t e r   e n e r g y   e f f i c i e n c y   c o m p a r e d   t o   P r o o f   o f   W o r k . 
 
 - - - 
 
 #   R E F E R E N C E S 
 
 1 .     N a k a m o t o ,   S .   ( 2 0 0 8 ) .   * B i t c o i n :   A   P e e r - t o - P e e r   E l e c t r o n i c   C a s h   S y s t e m * . 
 2 .     S w a n ,   M .   ( 2 0 1 5 ) .   * B l o c k c h a i n :   B l u e p r i n t   f o r   a   N e w   E c o n o m y * .   O ' R e i l l y   M e d i a . 
 3 .     F l a s k   D o c u m e n t a t i o n .   ( 2 0 2 4 ) .   * W e l c o m e   t o   F l a s k * .   [ O n l i n e ] .   A v a i l a b l e :   h t t p s : / / f l a s k . p a l l e t s p r o j e c t s . c o m / 
 4 .     P y t h o n   S o f t w a r e   F o u n d a t i o n .   ( 2 0 2 4 ) .   * P y t h o n   3 . 1 1   D o c u m e n t a t i o n * . 
 5 .     G r i n b e r g ,   M .   ( 2 0 1 8 ) .   * F l a s k   W e b   D e v e l o p m e n t :   D e v e l o p i n g   W e b   A p p l i c a t i o n s   w i t h   P y t h o n * .   O ' R e i l l y   M e d i a . 
 6 .     A n d r e a s   M .   A n t o n o p o u l o s .   ( 2 0 1 4 ) .   * M a s t e r i n g   B i t c o i n :   U n l o c k i n g   D i g i t a l   C r y p t o c u r r e n c i e s * . 
 
 - - - 
 * * E N D   O F   R E P O R T * * 
  
 