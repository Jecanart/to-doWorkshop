#languaje: en

Feature: todo list 

    Scenario: Add a single task to the list
        Given the to-do list is empty
        When the user adds a task "buy groceries"
        Then the list should contain "buy groceries"

    Scenario: Add multiple task to the to-do list
        Given the to-do list is empty
        When the user adds multiple task "buy groceries, wash the car, mown the lawn"
        Then the list should contain "buy groceries"
        And the list should contain "wash the car"
        And the list should contain "mown the lawn"
    
    Scenario: List all the task in the to-do list
        Given the to-do list contains tasks
            | task             |
            | buy groceries    |
            | wash the car     |
        When the user lists all tasks
        Then the output should contain
            | task             |
            | buy groceries    |
            | wash the car     |

    Scenario: Mask a task as completed
        Given The to-do list contain tasks
            | task             |
            | buy groceries    |
        When The user marks task "buy groceries" as completed
        Then The to-do list should show "buy groceries" as completed
    
    Scenario: Clear the to-do list
        Given The to-do list contains tasks
            | task             |
            | buy groceries    |
            | wash the car     |
        When The user clears the to-do list
        Then The to-do list should be empty