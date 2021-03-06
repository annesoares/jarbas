from unittest.mock import patch

from django.test import TestCase

from jarbas.core.management.commands.searchvector import Command
from jarbas.core.models import Reimbursement


class TestCommandHandler(TestCase):

    @patch.object(Reimbursement.objects, 'update')
    @patch('jarbas.core.management.commands.searchvector.print')
    def test_handler(self, print_, update):
        command = Command()
        command.handle()
        self.assertEqual(2, print_.call_count)
        self.assertEqual(1, update.call_count)
