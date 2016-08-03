# Copyright 2015 ARM Limited, All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
from module_reset_mbed import HostTestPluginResetMethod_Mbed


class HostTestPluginResetMethodMbedOsx(HostTestPluginResetMethod_Mbed):
    name = 'HostTestPluginResetMethod_MbedOsx'
    type = 'ResetMethod'
    capabilities = ['default_mac']
    required_parameters = ['serial', 'disk']

    def execute(self, capability, *args, **kwargs):
        """! Unmounts mbed Volume on MAC and executes base plugin

        @param capability Capability name
        @param args Additional arguments
        @param kwargs Additional arguments
        @details Each capability e.g. may directly just call some command line program or execute building pythonic function
        @return Capability call return value
        """
        disk = kwargs['serial']
        # unmount disk
        subprocess.call(['diskutil', 'unmount', disk])
        # invoke base class execute
        super(HostTestPluginResetMethodMbedOsx, self).execute(capability, *args, **kwargs)
