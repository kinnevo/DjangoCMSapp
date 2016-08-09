
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

print('PPPPPP: cms_toolbar en Capture')
@toolbar_pool.register
class CaptureToolbar(CMSToolbar):

    def populate(self):

        print('KKKKKKKKKKKKKKKKKKKKKKKKKKKK: populate')
 #       if self.is_current_app:
        if self.request.toolbar:
            print(self.request.toolbar)
            print( 'registration')
            print(self.app_path)
            menu = self.toolbar.get_or_create_menu('demo', _('Capture'),2)
            print( "MENU: ", menu)
            menu.add_modal_item(u'Listado', url="capture")
#            menu.add_item("demo",1)
            menu.add_break()
#            url = reverse('admin:polls_poll_changelist')
#            menu.add_sideframe_item(_('Poll overview'), url=url)

