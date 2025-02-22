# Copyright (c) Microsoft. All rights reserved.

import asyncio

import e2e_text_completion
import pytest

import semantic_kernel as sk
import semantic_kernel.connectors.ai.hugging_face as sk_hf


@pytest.mark.asyncio
async def test_hf_local_text_generation_service_with_skills():
    kernel = sk.Kernel()

    # Configure LLM service
    kernel.config.add_text_service(
        "gpt2", sk_hf.HuggingFaceTextCompletion("gpt2", task="text-generation")
    )

    await e2e_text_completion.simple_completion(kernel)


if __name__ == "__main__":
    asyncio.run(test_hf_local_text_generation_service_with_skills())
