# Stress-Test-Portofolio
Yeaaaah, this is one step forward to become QE.

# Stress Test Portfolio - JMeter

## 📌 Overview
This project demonstrates stress testing implementation using Apache JMeter to analyze system behavior under extreme load conditions.

## 🛠 Tools Used
- Apache JMeter
- Java JDK
- CSV Data Config
- GitHub

## 🎯 Objectives
- Identify system limit under heavy traffic
- Measure response time & throughput
- Observe server failure point
- Evaluate system stability
- 
## Test Scenarios
  I have 2 test scenarios :
- Total Requests: 1,000
- Target: PetStore Swagger API
- Goal: Push the system beyond normal load

===========================================
- Total Requests: 5,000
- Target: PetStore Swagger API
- Goal: Push the system beyond normal load

===========================================
From 2 test scenarios I did before, I was still not stisfied because the system was still safe and tried to do 1 more scenario until the system crashed.

- Total Requests: 23,000
- Target: PetStore Swagger API
- Goal: Push the system beyond normal load



## Result Summary

- [Result Summary)(https://github.com/Kanekoo00/Stress-Test-Portofolio/tree/main/reports)

## Conclusion
 - Based on 2 Scenarios with 1000 and 5000 samples
   The system remains functionally stable, but experiences significant performance degradation.     Response times exceed acceptable limits, even though no failures.
   
 - However, an additional test scenario with a higher number of requests in the system reaching     maximum limit. The result of this scenario got an error rate of 12% and a performance            collapse taht reached a maximum value of 23 minutes. This sccenario could be considered a        partial failure.

 - Overall, the stress testing confirmed that the application is able to handle load functionally up to a certain threshold, but fails to maintin performance under extreme conditions. This testing successfully indentified **breaking point** and **performance degredation pattern** of the system, this is can be used as reference for capacity planning and optimization.

