from kay.ext.testutils.gae_test_base import GAETestBase

from adminapp.views import set_test_data
from mainapp.models import JPlayerData

class SetPlayerDataTest(GAETestBase):

    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_set_data(self):
        set_test_data()
        results = JPlayerData.all().filter(u'display_page_flg =',True).fetch(1000)
        self.assertEquals(len(results),260)
