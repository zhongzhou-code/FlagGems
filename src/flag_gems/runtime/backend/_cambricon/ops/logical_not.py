import logging

import triton
import triton.language as tl

from ..utils.pointwise_dynamic import pointwise_dynamic

logger = logging.getLogger(__name__)


@pointwise_dynamic(promotion_methods=[(0, "ALWAYS_BOOL")])
@triton.jit
def logical_not_func(x):
    return not x.to(tl.int1)


def logical_not(A):
    logger.debug("GEMS_CAMBRICON LOGICAL_NOT")
    return logical_not_func(A)
