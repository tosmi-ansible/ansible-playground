import os

from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.utils.display import Display

DOCUMENTATION = r"""
    name: example
    short_description: Example inventory plugin
    description:
        - This is an example of an inventory plugin.
        - It returns a static list of hosts
"""

EXAMPLES = r"""
    # this inventory returns an example group with two hosts
"""

display = Display()

class InventoryModule(BaseInventoryPlugin):
    NAME = 'example'

    def __init__(self):
        super(InventoryModule, self).__init__()
        self.server = None

    def verify_file(self, path):
        return path.endswith(('example.yml', 'example.yaml'))

    def parse(self, inventory, loader, path, cache=True):
        display.warning("Entering parse function")
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        display.warning(path)
        config_data = self._read_config_data(path)

        display.warning("Username from environment: {}".format(os.environ.get('INVENTORY_USERNAME')))
        display.warning("Password from environment: {}".format(os.environ.get('INVENTORY_PASSWORD')))

        display.warning("Server setting from inventory config: {}".format(config_data.get('server')))


        self.inventory.add_host('example-host1')
        self.inventory.add_host('example-host11')
        self.inventory.add_host('example-host12')
        self.inventory.add_host('example-host13')
        self.inventory.add_host('example-host14')
        self.inventory.add_host('example-host2')
        self.inventory.add_host('example-host3')
        self.inventory.add_host('example-host4')

        group = self.inventory.add_group('Group_1')
        self.inventory.set_variable(group, 'ansible_connection', 'local')

        group = self.inventory.add_group('Group_1_nonprod')
        self.inventory.set_variable(group, 'ansible_connection', 'local')

        group = self.inventory.add_group('Group_1_prod')
        self.inventory.set_variable(group, 'ansible_connection', 'local')

        group = self.inventory.add_group('Group_2')
        self.inventory.set_variable(group, 'ansible_connection', 'local')

        group = self.inventory.add_group('Group_3')
        self.inventory.set_variable(group, 'ansible_connection', 'local')

        self.inventory.add_child('Group_1', 'example-host1')


        self.inventory.add_child('Group_1_nonprod', 'example-host11')
        self.inventory.add_child('Group_1_nonprod', 'example-host12')

        self.inventory.add_child('Group_1_prod', 'example-host13')
        self.inventory.add_child('Group_1_prod', 'example-host14')

        self.inventory.add_child('Group_2', 'example-host2')
        self.inventory.add_child('Group_3', 'example-host3')

