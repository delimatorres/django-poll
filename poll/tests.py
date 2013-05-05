from django.test import TestCase
from poll.models import Poll, Queue, Vote
from django.utils.datetime_safe import datetime
from django.test.client import Client
from django.core.urlresolvers import reverse


class PollTest(TestCase):
    def setUp(self):
        self.queue = Queue(title='TestQueue',
                           auth=False)
        self.queue.save()
        self.poll = Poll(title='TestPoll',
                         queue=self.queue,
                         polltype=0,
                         startdate=datetime.now())
        self.poll.save()
        self.item = self.poll.item_set.create(userbox=False,
                                              value='One',
                                              index=0)
        self.client = Client()
    
    def test_voting(self):
        request = self.client.post(
                    reverse('poll_ajax_vote',
                            args=(self.poll.pk,)),
                            {'chosen_items': '{"%s": "radio"}'\
                                                    % (self.item.id,)},
                            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(Vote.objects.count(), 1)