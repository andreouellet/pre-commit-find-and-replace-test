# -*- coding: utf-8 -*-
# import unittest
# import os
# import tempfile
# import json
# from unittest.mock import patch
# import argparse
# from find_and_replace.main import replace_in_file, main



# class TestReplaceInFile(unittest.TestCase):
#     def setUp(self):
#         self.temp_file = tempfile.NamedTemporaryFile(delete=False)
#         self.temp_file.write(b'Test line 1\nTest line 2\nTest line 3\n')
#         self.temp_file.close()

#     def tearDown(self):
#         os.unlink(self.temp_file.name)

#     def test_replace_in_file(self):
#         replace_in_file(self.temp_file.name, 'Test', 'Replaced')
#         with open(self.temp_file.name, 'r') as f:
#             lines = f.readlines()
#         self.assertEqual(lines, ['Replaced line 1\n', 'Replaced line 2\n', 'Replaced line 3\n'])

# class TestMain(unittest.TestCase):
#     def setUp(self):
#         self.temp_file = tempfile.NamedTemporaryFile(delete=False)
#         self.temp_file.write(b'Test line 1\nTest line 2\nTest line 3\n')
#         self.temp_file.close()

#     def tearDown(self):
#         os.unlink(self.temp_file.name)
#     @patch('argparse.ArgumentParser.parse_args')
#     def test_main_with_direct_mode(self, mock_args):
#         mock_args.return_value = argparse.Namespace(files=[self.temp_file.name], search='Test', replacement='Replaced', read_from_file=False, replacements_file='')
#         main()
#         with open(self.temp_file.name, 'r') as f:
#             lines = f.readlines()
#         self.assertEqual(lines, ['Replaced line 1\n', 'Replaced line 2\n', 'Replaced line 3\n'])

#     @patch('argparse.ArgumentParser.parse_args')
#     def test_main_with_file_mode(self, mock_args):
#         replacements_file = tempfile.NamedTemporaryFile(delete=False)
#         replacements_file.write(b'[{"search": "Test", "replacement": "Replaced"}]')
#         replacements_file.close()

#         mock_args.return_value = argparse.Namespace(files=[self.temp_file.name], search='', replacement='', read_from_file=True, replacements_file=replacements_file.name)
#         main()
#         with open(self.temp_file.name, 'r') as f:
#             lines = f.readlines()
#         self.assertEqual(lines, ['Replaced line 1\n', 'Replaced line 2\n', 'Replaced line 3\n'])

#         os.unlink(replacements_file.name)

#     @patch('argparse.ArgumentParser.parse_args')
#     def test_main_with_invalid_replacements_file(self, mock_args):
#         mock_args.return_value = argparse.Namespace(files=[self.temp_file.name], search='', replacement='', read_from_file=True, replacements_file='invalid.json')
#         with self.assertRaises(SystemExit) as cm:
#             main()
#         self.assertEqual(cm.exception.code, 1)

#     @patch('argparse.ArgumentParser.parse_args')
#     def test_main_with_invalid_json(self, mock_args):
#         replacements_file = tempfile.NamedTemporaryFile(delete=False)
#         replacements_file.write(b'invalid json')
#         replacements_file.close()

#         mock_args.return_value = argparse.Namespace(files=[self.temp_file.name], search='', replacement='', read_from_file=True, replacements_file=replacements_file.name)
#         with self.assertRaises(SystemExit) as cm:
#             main()
#         self.assertEqual(cm.exception.code, 1)

#         os.unlink(replacements_file.name)

# if __name__ == '__main__':
#     unittest.main()
