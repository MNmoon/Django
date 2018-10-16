# -*- coding: utf-8 -*-
import datetime
#from django.utils import timezone
from .models import Question
from django.test import TestCase
import timezone

# Create your tests here.

class QuestionModelsTests(TestCase):
    def test_was_publised_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        print time
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
