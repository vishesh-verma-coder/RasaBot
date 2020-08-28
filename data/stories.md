##ask_question_name
* ask_question
 - utter_name

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

##sad path without greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  
## interactive_story_1
* ask_question
    - utter_name
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* deny
    - utter_goodbye
    
##manager_story_SDWAN_with_NO_domain_provided
*ask_About_SDWAN
 - utter_cannot_understand
 
##manager_story_HP
*ask_About_CyberSOC{"position":"manager","domain":"CyberSOC"}
 - utter_manager_cybersoc
 - slot{"position":"manager"}
 
##manager_story_SDWAN_with_domain_provided
*ask_About_SDWAN{"position":"manager","domain":"SDWAN"}
 - utter_manager_sdwan
 - slot{"position":"manager"}
 
