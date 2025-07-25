import logging

import triton
import triton.language as tl

from ..utils.pointwise_dynamic import pointwise_dynamic

logger = logging.getLogger(__name__)


@pointwise_dynamic(promotion_methods=[(0, "INT_TO_FLOAT")])
@triton.jit
def exp_func(x):
    return tl.exp(x.to(tl.float32))


def exp(A):
    logger.debug("GEMS_CAMBRICON EXP")
    return exp_func(A)


def exp_(A):
    logger.debug("GEMS_CAMBRICON EXP_")
    return exp_func(A, out0=A)
