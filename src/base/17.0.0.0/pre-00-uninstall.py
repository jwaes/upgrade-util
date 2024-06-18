import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):
    
    modules_to_uninstall = [
        'jt_documents_product',
        'jt_documents_website',
    ]

    for candidate in modules_to_uninstall:
        _logger.info("About to uninstall module %s", candidate)
        util.uninstall_module(cr,candidate)

