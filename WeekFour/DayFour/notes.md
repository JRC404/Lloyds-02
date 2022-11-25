# Testing

* As testers, we want to be involved in as many stages as possible
* Does the software meet the desired requirements?
    * Look back on the requirements stage... does the software do too much?
* Provide stakeholders with information about the quality of the software

* Testers are meant be independent, objective and give thorough view points of the software
* Testers are there to make stakeholders aware of potentials risks

* Testers are meant to identify bugs and defects

## Verification
* Are we building the product right / correctly?

## Validation
* Are we building the right / correct product?

## Stand-up / As a tester
* What did you achieve yesterday?
* What are you working on today? What are your main goals?
* Any stucks / blockers?

## Testing Strategies
* Before testing, we want to identify as many requirements as possible
* Detailed objectives (testing and development objectives)
* Develop a test plan that fits your methodology
* Implement effective test reviews of code and automation tests

## Unit Testing

* Variables, constants, functions, methods, arrays, lists, queues, stacks, loops, conditions, operators etc can all be tested during unit testing

## Regression

* Ensuring that changes to one module doesn't affect or hinder other modules and the way they function

## Integration Testing

* Top-down testing
    * Testing the whole application together first
    * Then slowly breaking down pieces to ensure they still work together

* Bottom-up testing
    * Testing small parts of the application and build up to the complete article

* Module A works with B
* Module A works with C
* Module B works with C

* Module A & B work with C
* Module A & C work with B
* Module B & C work with A

## Performance Testing

* Stress tests
* Volume tests
* Security tests
* Quality tests
* Documentation tests
* Client / Human-Factor tests
* Recovery tests
* Configurations tests (hardware & software)

## Testing Tools

* Simulators
* Monitors - regulate processor load / resourcing
* Analysis - what we've monitored... what are we going to do about it?

## Test Plan

* Document that will have a complete set of test cases
    * What will be done?
    * Who will be doing it?
    * When will it be done?
    * How will it be done?
    * What happened?
    * Comments for other testers, engineers and notes for future reference

### What is in a test case?

* Unique Identifier for the test
* Instructions in the test:
    * Tell the tester what to do?
    * Try and keep instructions in the document
        * Don't send your testers on a wild goose chase around other documents in order to complete your tests
    * Tell / help the tester when a test fails... what should they do when a test does fail?
* Name the tester, name the environment and version numbers, name the date
* What tools do we need?
* Do we need any sample code or data?
    * How do we use it?
    * When can we use it?
    * How long can we use it for?
    * Who can use the test data?
* Expected results
* Actual results
    * Analysis of the results
        * Were the results expected?
        * Did we notice anything strange?
        * Tough day at the office?
* Any comments, corrects... any modification to schedules
* Your approval / sign-off

* Test plan should be quite long

* Completing a test plan can only hapen after the requirements have been confirmed
    * The order of tests depends on many things
    * Tests can be ranked on a probability x impact scale
    * Manual or automated? You decide.

## Test Driven Development

* **Development driven by tests**
* Software requires tests to be written before the code is written that you are going to test

* Writing tests before you've written the code may seem bonkers... but having a clear structure for your code allows you to write clean and precise code, methods, functions etc

* It's a game of fail, pass, fail, pass, fail, pass

* We want working code... by any means necessary!
    * To start with, you don't always get the best solution
    * Getting working software as quickly as you can... then refactoring!