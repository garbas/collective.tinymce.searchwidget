
from zope.component import getMultiAdapter

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


class ImageDialogView(BrowserView):
    """ """
    
    __call__ = ViewPageTemplateFile('dialog.pt')

    formname = 'searchwidget-images'

    def __init__(self, context, request, view=None):
        self.context = aq_inner(context)
        self.request = request
        self.__parent__ = view
        self.portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.site_url = self.portal_state.portal_url()

    def generate_javascript(self):
        return '''
            jq("#tinymce-dialog .searchPage #form-buttons-search").click(function() {
              jq("#tinymce-dialog .seachResultPage").load(
                    "%(site_url)s/++search++%(formname)s?form.buttons.search=1&"+
                    jq("#tinymce-dialog form .field input").serialize()+
                    " .seachResultPage", null, function() {
                jq("#tinymce-dialog .searchResults dd").click(function() {
                  jq("#tinymce-dialog .searchResults dd.selected").removeClass("selected");  
                  jq(this).addClass('selected');
                  return false;
                });
              });
              return false;
            });''' % dict(
                site_url = self.site_url,
                formname = self.formname)

