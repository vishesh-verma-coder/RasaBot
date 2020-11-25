from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import time
class ask_about_esc_offerings_action(Action):
   def name(self):
      return "ask_about_esc_offerings_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message=" [ESC Team in India supports]"\
              "  <br> 1. UCC"\
              "  <br> 2. Voice Operations"\
              "  <br> 3. Video Operations"\
              "  <br> 4. Contact Center"\
              "  <br> 5. Network and Cyber Security Operations"\
              "  <br> 6. Product and Process Development"\
              "  <br> 7. SDN\SD-WAN"

      dispatcher.utter_message(message)

class ask_about_esc_ongoing_automation_projects_action(Action):
   def name(self):
      return "ask_about_esc_ongoing_automation_projects_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message=" [ESC Team has following ongoing Automation projects]" \
              "  <br> 1. Robotic Process Automation"\
              "  <br> 2. Open Source Chatbot"\
              "  <br> 3. Machine Learning and AI"

      dispatcher.utter_message(message)

class ask_about_esc_slm_activities_action(Action):
   def name(self):
      return "ask_about_esc_slm_activities_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[Main activities of the Service LifeCycle Manager are:-]" \
              "  <br> 1> SIP management (Service Improvement Plans) " \
              "  <br> 2> Process & IT optimization for operational teams" \
              "  <br> 3> Operational product documentation maintenance " \
              "  <br> 4> Service Performance analysis"\
              "  <br> 5> Contribution to T5 and T6 presentations in TTM Product Boards"\
              "  <br> 6> Service change initiation, specification and Management"\
              "  <br> 7> Internal & External Audit for service"

      dispatcher.utter_message(message)

class ask_about_esc_pdl_services_support_action(Action):
   def name(self):
      return "ask_about_esc_pdl_services_support_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[Services Supported by ESC PDL India Team along with Experts are :]" \
              "  <br> 1. B2G Cisco & Avaya | Harish Yadav(SLM and SIE)" \
              "  <br> 2. B2G Microsoft | Jayant Mandal(SLM)" \
              "  <br> 3. B2GaaS | Alpana Sinha(Sr.SLM)" \
              "  <br> 4. FCC (Flexible Contact Center)| Kamal Verma(SLM)"\
              "  <br> 5. MCC Cisco | Kamal Verma (SLM)"\
              "  <br> 6. MCCP (Managed Contact Center Premium) | Harish Yadav (SLM)" \
              "  <br> 7. MVP (Managed Voice Portal) | Saba Khalid (SIE)"\
              "  <br> 8. OVP | Ankita Saxena (SLM)"

      dispatcher.utter_message(message)


class ask_about_esc_cybersoc_services_action(Action):


   def name(self):
      return "ask_about_esc_cybersoc_services_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[Services Supported by CyberSOC India Team are :-]" \
              " <br> 1> SIEM " \
              " <br> 2> DDOS Protection" \
              " <br> 3> IAM" \
              " <br> 4> Vulnerability Management"\
              " <br> 5> AntiSpam/AntiPhishing"\
              " <br> 6> Malware Analysis"\
              " <br> 7> Network Intrusion Prevention and Detection" \
              " <br> 8> Advaned Datalake\Threat Intelligence solution"\
              " <br> 9> Real Time Threat Prevention"
      dispatcher.utter_message(message)

class ask_about_esc_networksoc_services_action(Action):
   def name(self):
      return "ask_about_esc_networksoc_services_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[Services Supported by Network Security India Team are :-]" \
              "  <br> 1> Perimeter Security Firewalls " \
              "  <br> 2> Network IPS/IDS Solution" \
              "  <br> 3> Cloud Proxy Services" \
              "  <br> 4> Load Balancers"\
              "  <br> 5> Web Application Firewalls"\
              "  <br> 6> Remote SSL VPN Solutions"\
              "  <br> 7> Build Operations/Implementation" \
              "  <br> 8> On Premise Proxy Solutions"

      dispatcher.utter_message(message)

class ask_about_esc_sdn_services_action(Action):
   def name(self):
      return "ask_about_esc_sdn_services_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="Services Supported by SDN/SD-WAN Team are :-" \
              "  <br> 1> SDN easy Go OTT " \
              "  <br> 2> Cisco- uCPE" \
              "  <br> 3> Cisco-Viptela-SD-WAN" \
              "  <br> 4> Riverbed SD-WAN"\
              "  <br> 5> IOT"

      dispatcher.utter_message(message)

class ask_about_esc_ppm_services_action(Action):
   def name(self):
      return "ask_about_esc_ppm_services_action"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[Services Supported in PPM are :]" \
              "  <br> 1> B2gaas " \
              "  <br> 2> BTG" \
              "  <br>3> CCA" \
              "  <br> 4> NIVR"\
              "  <br> 5> LVS" \
              "  <br> 6> Porting Cisco" \
              "  <br> 7> MS Lync" \
              "  <br> 8> Avaya"

      dispatcher.utter_message(message)

class ask_about_esc_details_of_domains_ucc(Action):
   def name(self):
      return "ask_about_esc_details_of_domains_ucc"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="Teams involved in UCC are :-" \
              "  <br> 1. VOC CTS 2 Cisco " \
              "  <br> 2. VOC CTS 3 + PME Cisco" \
              "  <br> 3. VOC CTS2 Lync + Avaya" \
              "  <br> 4. VOC CTS3 Lync + Avaya"\
              "  <br> 5. CTE Cisco" \
              "  <br> 6. CTE Lync" \
              "  <br> 7. BTG CTS2"\
              "  <br> 8. BTG CTS3" \
              "  <br> 9. Voice CPT/VT BTG"

      dispatcher.utter_message(message)

class ask_about_esc_details_of_domains_ppm(Action):
   def name(self):
      return "ask_about_esc_details_of_domains_ppm"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[PPM - Program and Project Management - Offerings of ESC]" \
              "  <br> • PPM Organise the relevant project under the program to drive it as a unit to obtain the customer’s objective" \
              "  <br> • PPM works on establishment, audit and enforcement of technical and established processes"


      dispatcher.utter_message(message)

class ask_about_esc_details_of_domains_cybersoc(Action):
   def name(self):
      return "ask_about_esc_details_of_domains_cybersoc"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="[CyberSOC- Protecting against Cyber Attacks]"\
           "  <br> • CyberSOC team operates from India and France with objective to protect customers from cyber attacks, perform\
      Threat Analysis, Detection, Mitigation"\
           "  <br> • In India CyberSOC has both L1 and L2 support. L3 support is available in France"\
           "  <br> • Click <a href=\"http://10.238.100.73:8080/ESCPortal/#/security/\">ESC CybserSOC!</a> for more details"


      dispatcher.utter_message(message)

class about_esc_details_of_domains_netsec(Action):
   def name(self):
      return "about_esc_details_of_domains_netsec"

   def run(self,
           dispatcher,
           tracker,
           domain):
      message="<u>[NetSec- Providing Infra and Perimeter Security]</u>"\
      " <br> • NetSec team (MSIO India) operates from India/Cairo/Mauritius with objective of handling daily operational issues, business\
      continuity, Perimiter security, Network Intrusuion detection and protection,Web traffic security, Remote SSL solutions etc.."\
      " <br> • India team has L2 support named MSIO India (shared SOC) team with L1 support for a few customers only."\
      " <br> • Click <a href=\"http://10.238.100.73:8080/ESCPortal/#/security/\">ESC NetSec!</a> for more details"

      dispatcher.utter_message(message)
class ask_about_esc_details_of_domains_sdn(Action):
          def name(self):
              return "ask_about_esc_details_of_domains_sdn"

          def run(self,
                  dispatcher,
                  tracker,
                  domain):
              message = " [SDN- Software Defined Network |  SD-WAN -Software Defined Wide Are Network]"\
      "  <br> • SDN goal is to  develop dynamic, flexible, scalable connectivity to support changing demands in the DC (data centers) and on core networks"\
      "  <br> • SD-WAN focuses on providing software defined application routing to the WAN and on connecting an organization’s geographically distributed locations"\
      "  <br> • Click  <a href=\"http://10.238.100.73:8080/ESCPortal/#/sdn/\">SDN Page!</a> for more details"

              dispatcher.utter_message(message)


class ask_about_esc_plazza_and_esc_portalpage_action(Action):
    def name(self):
        return "ask_about_esc_plazza_and_esc_portalpage_action"

    def run(self,
            dispatcher,
            tracker,
            domain):
        message = "• <a href=\"http://10.238.100.73:8080/ESCPortal/\">ESC Portal Page!</a>  " \
                  " <br> • <a href=\"https://plazza.orange.com/groups/esc-india\">ESC Plazza Page!</a>  " \

        dispatcher.utter_message(message)

class ask_about_esc_shift_timings_action(Action):
    def name(self):
        return "ask_about_esc_shift_timings_action"

    def run(self,
            dispatcher,
            tracker,
            domain):
        message = " [Different types of Shifts are]" + "  <br> • A3" +"  <br> • B4" +"  <br> • C5" +"  <br> • D6" + "  <br>• E1" +"  <br> • F2"
        dispatcher.utter_message(message)


class ask_about_esc_meraki_name(Action):
   sample1=" [Fetched below data for Meraki appliances..]"
   sample=""
   def name(self):
      return "ask_about_esc_meraki_name"

   def run(self,
           dispatcher,
           tracker,
           domain):

      #Running API query
      #dispatcher.utter_message(ask_about_esc_cybersoc_services_action.sample)
      header = {"X-Cisco-Meraki-API-Key": "65260a410ebe8a02f187f664dfed3976b5e3e8d4"}
      device_list_response = requests.get('https://api.meraki.com/api/v0/organizations/682858293500054273/devices',
                                          headers=header)
      jsonResponse = device_list_response.json()
      for i in range(0, 5):
          ask_about_esc_meraki_name.sample += "<br>"+str(i+1)+") "+(jsonResponse[i]['name'])

      dispatcher.utter_message(ask_about_esc_meraki_name.sample1 + " " + ask_about_esc_meraki_name.sample)


class ask_about_esc_meraki_lanip(Action):
   sample1="[Fetched below IP info for Meraki appliances..]"
   sample=""
   def name(self):
      return "ask_about_esc_meraki_lanip"

   def run(self,
           dispatcher,
           tracker,
           domain):

      #Running API query
      #dispatcher.utter_message(ask_about_esc_cybersoc_services_action.sample)
      header = {"X-Cisco-Meraki-API-Key": "65260a410ebe8a02f187f664dfed3976b5e3e8d4"}
      device_list_response = requests.get('https://api.meraki.com/api/v0/organizations/682858293500054273/devices',
                                          headers=header)
      jsonResponse = device_list_response.json()
      for i in range(0, 5):
          try:
           ask_about_esc_meraki_lanip.sample += "<br>"+str(i+1)+") "+(jsonResponse[i]['lanIp'])
          except:
              pass

      dispatcher.utter_message(ask_about_esc_meraki_lanip.sample1 + " " + ask_about_esc_meraki_lanip.sample)


##Tesing


class ask_about_video(Action):

   def name(self):
      return "ask_about_video"

   def run(self,
           dispatcher,
           tracker,
           domain):
       msg = {"type": "video", "payload": {"title": "Link name", "src": "https://www.youtube.com/watch?v=pX6zqaEHAdw"}}

       dispatcher.utter_message(text="Check this video", attachment=msg)

class ask_about_chart(Action):

   def name(self):
      return "ask_about_chart"

   def run(self,
           dispatcher,
           tracker,
           domain):
       data = {"title": "Leaves", "labels": ["Sick Leave", "Casual Leave", "Earned Leave", "Flexi Leave"],
               "backgroundColor": ["#36a2eb", "#ffcd56", "#ff6384", "#009688", "#c45850"], "chartsData": [5, 10, 22, 3],
               "chartType": "pie", "displayLegend": "true"}

       message = {"payload": "chart", "data": data}

       dispatcher.utter_message(text="Here are your leave balance details", json_message=message)


class ask_about_location(Action):

   def name(self):
      return "ask_about_location"

   def run(self,
           dispatcher,
           tracker,
           domain):
       data = {"title": "Leaves", "labels": ["Sick Leave", "Casual Leave", "Earned Leave", "Flexi Leave"],
               "backgroundColor": ["#36a2eb", "#ffcd56", "#ff6384", "#009688", "#c45850"], "chartsData": [5, 10, 22, 3],
               "chartType": "pie", "displayLegend": "true"}

       message = {"payload": "location"}

       dispatcher.utter_message("Sure, please allow me to access your location 🧐", json_message=message)


       dispatcher.utter_message(text="Here are your leave balance details", json_message=message)


class ask_about_quick_reply(Action):

   def name(self):
      return "ask_about_quick_reply"

   def run(self,
           dispatcher,
           tracker,
           domain):


     data = [{"title": "chip1", "payload": "chip1_payload"}, {"title": "chip2", "payload": "chip2_payload"},
           {"title": "chip3", "payload": "chip3_payload"}]

     message = {"payload": "quickReplies", "data": data}

     dispatcher.utter_message(text="Please choose a cuisine", json_message=message)


class ask_about_dropdown(Action):

   def name(self):
      return "ask_about_dropdown"

   def run(self,
           dispatcher,
           tracker,
           domain):
       data = [{"label": "option1", "value": "/inform{'slot_name':'option1'}"},
               {"label": "option2", "value": "/inform{'slot_name':'option2'}"},
               {"label": "option3", "value": "/inform{'slot_name':'option3'}"}]

       message = {"payload": "dropDown", "data": data}

       dispatcher.utter_message(text="Please select a option", json_message=message)

class ask_about_cheer_up(Action):

   def name(self):
      return "ask_about_cheer_up"

   def run(self,
           dispatcher,
           tracker,
           domain):
       dispatcher.utter_message(text="Here is something to cheer you up 😉",image="https://i.imgur.com/nGF1K8f.jpg")