from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

print('cms.menu: cms_menu en Capture')

class TestMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('Plan'), "/", 5)
        n2 = NavigationNode(_('Travel'), "/capture/", 6)
        n3 = NavigationNode(_('Remember'), "/hello/", 3)
        n4 = NavigationNode(_('Memories'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenu)



from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu2(CMSAttachMenu):

    name = _("test2 menu")

    def get_nodes(self, request):
        nodes2 = []
        xn = NavigationNode(_('sample root page'), "/", 1)
        xn2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        xn3 = NavigationNode(_('sample account page'), "/hello/", 3)
        xn4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        nodes2.append(xn)
        nodes2.append(xn2)
        nodes2.append(xn3)
        nodes2.append(xn4)
        return nodes2

menu_pool.register_menu(TestMenu2)


