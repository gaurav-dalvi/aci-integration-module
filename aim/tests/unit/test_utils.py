# Copyright (c) 2016 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
test_utils
----------------------------------

Tests for `utils` module.
"""

from aim.tests import base
from aim import utils


class TestUtils(base.TestAimDBBase):

    def test_sanitize_display_name(self):
        self.assertEqual(
            'some name',
            utils.sanitize_display_name('some name'))

        self.assertEqual(
            'some' * 14 + 'som',
            utils.sanitize_display_name('some' * 15))
