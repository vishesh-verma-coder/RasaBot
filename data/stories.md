##chitchat
#* chitchat
 #   - respond_chitchat
    
##ask_question_name
* ask_question
 - utter_name

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## Chatbot web socket get_started
* get_started
 - utter_getstarted1
 - utter_getstarted2
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

## Failed to Cheer-1
* greet
    - utter_greet
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* deny
    - utter_sorry

## Failed to cheer-2
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* deny
    - utter_sorry
 
##Response to how can you help
* how_can_you_help
 - utter_greet

## Response to button clicks
* ask_about_esc_cybersoc_button
 - utter_ask_about_cybersoc_button
* ask_about_netsec_button
 - utter_ask_about_netsec_button
* ask_about_ppm_button
 - utter_ask_about_ppm_button
* ask_about_sdn_button
 - utter_ask_about_sdn_button
* ask_about_pdl_button
 - utter_ask_about_pdl_button
* ask_about_ucc_button
 - utter_ask_about_ucc_button
 
##ask_about_esc
* ask_about_esc
 - utter_ask_about_esc
 
 
##ask_about_esc_offerings_services
* ask_about_esc_domains_offerings_services
 - utter_incomplete_question

* ask_about_esc_domains_offerings_services{"services_esc": "ESC"}
 - ask_about_esc_offerings_action
* ask_about_esc_domains_offerings_services{"services_pdl": "PDL"}
 - ask_about_esc_pdl_services_support_action
* ask_about_esc_domains_offerings_services{"services_cyber": "CyberSOC"}
 - ask_about_esc_cybersoc_services_action
* ask_about_esc_domains_offerings_services{"services_netsec": "Netsec"}
 - ask_about_esc_networksoc_services_action
* ask_about_esc_domains_offerings_services{"services_sdn": "SDN"}
 - ask_about_esc_sdn_services_action
* ask_about_esc_domains_offerings_services{"services_ppm": "PPM"}
 - ask_about_esc_ppm_services_action 
* ask_about_esc_domains_offerings_services{"services_contactcenter": "Contact Center"}
 - utter_ask_about_esc_contactcenter_services_action 
 
## Response about ESC Managers (Entity not provided)
* ask_about_esc_manager
 - utter_default
## Response about ESC Managers
* ask_about_esc_manager{"department_cyber": "CyberSOC"}
  - utter_ask_about_esc_manager_cybersoc
* ask_about_esc_manager{"department_netsec": "NetworkSOC"}
  - utter_ask_about_esc_manager_networksecurity
* ask_about_esc_manager{"department_incubation": "IncubationCenter"}
  - utter_ask_about_esc_manager_incubationcenter
* ask_about_esc_manager{"department_esc": "ESC"}
  - utter_ask_about_esc_manager_esc
  
## Response to Abbreviations(Entity not provided)
* ask_about_esc_abbreviations
 - utter_default
 
## Response to Abbreviations
* ask_about_esc_abbreviations{"abb_pdl": "PDL"}
 - utter_ask_about_esc_pdl_abbreviation
* ask_about_esc_abbreviations{"abb_slm": "SLM"}
 - utter_ask_about_esc_slm_abbreviation
* ask_about_esc_abbreviations{"abb_esc": "ESC"}
 - utter_ask_about_esc_abbreviation
* ask_about_esc_abbreviations{"abb_sdn": "SDN"}
 - utter_ask_about_esc_sdn_abbreviation
* ask_about_esc_abbreviations{"abb_ppm": "PPM"}
 - utter_ask_about_esc_ppm_abbreviation
* ask_about_esc_abbreviations{"abb_ucc": "UCC"}
 - utter_ask_about_esc_ucc_abbreviation
 
## Response about ongoing automation projects
* ask_about_esc_ongoing_automation_projects
 - ask_about_esc_ongoing_automation_projects_action

## Response about ongoing trainings
* ask_about_esc_ongoing_training
 - utter_ask_about_esc_ongoing_training
 
## Response about SLM activities
* ask_about_esc_slm_activities
 - ask_about_esc_slm_activities_action

## Response about SLM objectives
* ask_about_esc_slm_objectives
 - utter_ask_about_esc_slm_objectives
 
## Response to details of any domain (Entity Not provided)
* ask_about_esc_details_of_domains
 - utter_default
##Response to details of any domain (Entity provided)
## Response to details of PDL
* ask_about_esc_details_of_domains{"details_pdl": "PDL"}
 - utter_ask_about_esc_details_of_domains_pdl1
 - ask_about_esc_slm_activities_action
 - ask_about_esc_pdl_services_support_action
## Response to details of UCC
* ask_about_esc_details_of_domains{"details_ucc": "UCC"}
 - utter_ask_about_esc_details_of_domains_ucc
 - ask_about_esc_details_of_domains_ucc
## Response to details of PPM
* ask_about_esc_details_of_domains{"details_pmm": "PPM"}
 - ask_about_esc_details_of_domains_ppm
 - ask_about_esc_ppm_services_action
## Response to details of CyberSOC
* ask_about_esc_details_of_domains{"details_cybersoc": "CyberSOC"}
 - ask_about_esc_details_of_domains_cybersoc
 - ask_about_esc_cybersoc_services_action
 - utter_ask_about_esc_manager_cybersoc
## Response to details of NetSEC
* ask_about_esc_details_of_domains{"details_netsec": "NetSec"}
 - about_esc_details_of_domains_netsec
 - utter_ask_about_esc_manager_cybersoc
 - ask_about_esc_networksoc_services_action
## Response to details of SDN
* ask_about_esc_details_of_domains{"details_sdn": "SDN"}
 - ask_about_esc_details_of_domains_sdn
 - ask_about_esc_sdn_services_action
## Response to details of ESC
* ask_about_esc_details_of_domains{"details_esc": "ESC"}
 - utter_ask_about_esc_abbreviation
 - utter_ask_about_esc_manager_esc
 - ask_about_esc_offerings_action

##Response to shift timings
* ask_about_esc_shift_times
 - ask_about_esc_shift_timings_action
 
## Response to ESC Portal page
* ask_about_esc_plazza_and_esc_portalpage
 - ask_about_esc_plazza_and_esc_portalpage_action
 
 