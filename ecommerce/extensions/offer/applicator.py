import logging
from itertools import chain

import newrelic.agent
import waffle
from oscar.core.loading import get_model, get_class

ConditionalOffer = get_model('offer', 'ConditionalOffer')
Applicator = get_class('offer.utils', 'Applicator')

logger = logging.getLogger(__name__)


class ProgramApplicator(Applicator):

    @newrelic.agent.function_trace()
    def apply_offers(self, basket, offers):
        super(ProgramApplicator, self).apply_offers(basket, offers)

    def get_offers(self, basket, user=None, request=None):
        if waffle.switch_is_active("debug_selective_offers"):
            site_offers = self.get_site_offers()
            logger.info("ProgramApplicator.get_offers.site_offers: count={}, {}".format(len(site_offers), site_offers))
            basket_offers = self.get_basket_offers(basket, user)
            logger.info("ProgramApplicator.get_offers.site_offers: count={}, {}".format(len(basket_offers), basket_offers))
            user_offers = self.get_user_offers(user)
            logger.info("ProgramApplicator.get_offers.site_offers: count={}, {}".format(len(user_offers), user_offers))
            session_offers = self.get_session_offers(request)
            logger.info("ProgramApplicator.get_offers.site_offers: count={}, {}".format(len(session_offers), session_offers))

            return list(sorted(chain(
                session_offers, basket_offers, user_offers, user_offers,user_offers,user_offers,user_offers, user_offers, user_offers site_offers),
                key=lambda o: o.priority, reverse=True))
        else:
            super(ProgramApplicator, self).get_offers(basket, user, request)
