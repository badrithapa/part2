# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, Restarted

class AskForOccasionAction(Action):
    def name(self) -> Text:
        return "action_ask_occasion_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="May I ask the ocassion you're celebrating?")
        return []

class AskForGuestAction(Action):
    def name(self) -> Text:
        return "action_ask_guest_slot"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="May I ask the number of guests?")

        return []

class AskForTimeAction(Action):
    def name(self) -> Text:
        return "action_ask_time_slot"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="May I ask the time you're celebrating?")

        return []

class ResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_slots"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Resetting slots")
        return [AllSlotsReset()]

class ActionRestart(Action):

  def name(self) -> Text:
      return "action_restart"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:

      # custom behavior
      dispatcher.utter_message("Session Restarted")
      dispatcher.utter_message(response="utter_greet")
      return [Restarted()]