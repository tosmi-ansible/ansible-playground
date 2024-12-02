from ansible.plugins.inventory import BaseInventoryPlugin

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


class InventoryModule(BaseInventoryPlugin):
    NAME = 'example'

    def verify_file(self, path):
        return path.endswith(('example.yml', 'example.yaml'))

    def parse(self, inventory, loader, path, cache=True):
        inventory.add_host('example-host1')
        inventory.add_host('example-host2')
        inventory.add_host('example-host3')

        inventory.add_group('Group_1')
        inventory.add_group('Group_2')
        inventory.add_group('Group_3')

        inventory.add_child('Group_1', 'example-host1')
        inventory.add_child('Group_2', 'example-host2')
        inventory.add_child('Group_3', 'example-host3')

