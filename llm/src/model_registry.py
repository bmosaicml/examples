# Copyright 2022 MosaicML Examples authors
# SPDX-License-Identifier: Apache-2.0

from src.hf_causal_lm import ComposerHFCausalLM
from src.mosaic_gpt import ComposerMosaicGPT
from src.branching_gpt import ComposerBranchingGPT

COMPOSER_MODEL_REGISTRY = {
    'mosaic_gpt': ComposerMosaicGPT,
    'branching_gpt': ComposerBranchingGPT,
    'hf_causal_lm': ComposerHFCausalLM,
}
