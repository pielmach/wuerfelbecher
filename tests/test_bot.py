import asyncio
import os
import tempfile
import unittest
from unittest import mock

from wuerfelbecher import bot


class TestBot(unittest.TestCase):
    def setUp(self):
        self.test_bot = bot.setup_bot()
        os.environ["TEST_ENV"] = "test_secret_env"
        self.test_file = tempfile.NamedTemporaryFile(mode="w")
        self.test_file.writelines("test_secret_file")
        self.test_file.flush()

    def tearDown(self):
        self.test_file.close()
        os.environ.pop("TEST_ENV")
        self.test_bot = None

    def test_get_bot_token(self):
        self.assertEqual(bot.get_bot_token(self.test_file.name, "RANDOM_NOT_EXISTING_ENV"), "test_secret_file")
        self.assertEqual(bot.get_bot_token("/tmp/random_not_existing_path", "TEST_ENV"), "test_secret_env")
        self.assertEqual(bot.get_bot_token(self.test_file.name, "TEST_ENV"), "test_secret_file")

        with self.assertRaises(RuntimeError):
            bot.get_bot_token("/tmp/random_not_existing_path", "RANDOM_NOT_EXISTING_ENV")

    def test_commands(self):
        # validate that each of the commands is actually defined in the bot
        mock_ctx = mock.AsyncMock()
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.test_bot.all_commands["stats"](mock_ctx))
        loop.run_until_complete(self.test_bot.all_commands["roll"](mock_ctx))
        loop.run_until_complete(self.test_bot.all_commands["r"](mock_ctx))
        loop.run_until_complete(self.test_bot.on_ready())
        loop.close()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
