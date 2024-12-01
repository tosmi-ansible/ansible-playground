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

        inventory.add_group('example-group')
        inventory.add_child('example-group', 'example-host1')
        inventory.add_child('example-group','example-host2')


