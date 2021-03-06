# pylint: disable=invalid-name
"""
Unit testing
"""

import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.test_responses = ['English', 'Spanish', 'Mandarin']


    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.test_responses[1])
        self.assertIn(self.test_responses[1], self.my_survey.responses)
        #print(self.my_survey.show_question())
        #print(self.my_survey.show_results())

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for test_response in self.test_responses:
            self.my_survey.store_response(test_response)
        for test_response in self.test_responses:
            self.assertIn(test_response, self.my_survey.responses)
        #print(self.my_survey.show_question())
        #print(self.my_survey.show_results())


unittest.main()
