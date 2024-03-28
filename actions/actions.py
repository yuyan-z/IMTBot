# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import pandas as pd

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


# This is a simple example for a custom action which utters "Hello World!"
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

def get_campus_info(campus_entity):
    df = pd.read_csv('./data/campus.csv')
    for campus in df['campus']:
        if campus_entity in campus:
            info = df[df['campus'] == campus]
            overview = info['overview'].values[0]
            campus = info['campus'].values[0]
            return campus, overview

    return None, None


class GetCampusInfo(Action):

    def name(self) -> Text:
        return "action_campus_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        campus = next(tracker.get_latest_entity_values('campus'), None)

        if campus is None:
            dispatcher.utter_message("Sorry, I couldn't detect the campus")
        else:
            campus_found, overview = get_campus_info(campus)
            if not campus_found:
                dispatcher.utter_message(f"Sorry, I couldn't find information about {campus_found}.")
            else:
                dispatcher.utter_message(f"{campus_found.upper()} Campus: {overview}")

        return []


def get_teacher_info(teacher_entity):
    df = pd.read_csv('./data/teacher_info.csv')
    matches = df[(df['name'].str.lower().str.contains(teacher_entity.lower()))]
    return matches[['name', 'campus', 'designation', 'telephone', 'email']]


class GetTeacherInfo(Action):

    def name(self) -> Text:
        return "action_teacher_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        teacher_name = next(tracker.get_latest_entity_values('PERSON'), None)

        if teacher_name is None:
            dispatcher.utter_message("Sorry, I couldn't detect the name")
        else:
            matches = get_teacher_info(teacher_name)
            if len(matches) == 0:
                dispatcher.utter_message(f"Sorry, I couldn't find information about {teacher_name}.")
            else:
                matches_str = matches.to_string(index=False, header=False)
                dispatcher.utter_message("Here's the faculty members found :\n" + matches_str)

        return []


def get_major(domain_entity, campus_entity):
    df = pd.read_csv('./data/major.csv')
    matches = df[(df['domain'].str.lower().str.contains(domain_entity.lower())) &
                 (df['campus'].str.lower().str.contains(campus_entity.lower()))]
    return matches


class MajorFormAction(Action):
    def name(self) -> Text:
        return "action_major_form_submit"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        domain = tracker.get_slot("domain")
        campus = tracker.get_slot("campus")

        if domain is None or campus is None:
            dispatcher.utter_message("Sorry, I couldn't detect the name")
        else:
            matches = get_major(domain, campus)
            if len(matches) == 0:
                dispatcher.utter_message(f"Sorry, I couldn't find information about {domain} at the {campus} campus.")
            else:
                matches_str = matches.to_string(index=False)
                dispatcher.utter_message("You can choose the following majors :\n" + matches_str)

        return [SlotSet("domain", None), SlotSet("campus", None)]


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_contact_me"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = next(tracker.get_latest_entity_values('phone'), None)
        email = next(tracker.get_latest_entity_values('email'), None)

        if phone is None and email is None:
            dispatcher.utter_message("Sorry, I couldn't detect the contact information.")
        elif phone is None:
            dispatcher.utter_message(f"We'll contact you at {email} very soon")
        elif email is None:
            dispatcher.utter_message(f"We'll contact you at {phone} very soon")
        else:
            dispatcher.utter_message(f"We'll contact you at {phone} and {email} very soon")

        return []
