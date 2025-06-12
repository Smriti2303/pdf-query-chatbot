from llama_cpp import Llama

# Adjust this path to your local model (LLaMA 2 7B GGUF, for example)
LLAMA_PATH = "models\llama-2-7b-chat.gguf"
llm = Llama(model_path=LLAMA_PATH, n_ctx=2048)

def get_llm_response(prompt, context):
    """Combine user prompt with context and query the local LLaMA LLM."""
    system_prompt = "You are an assistant answering questions based on provided PDF content."
    full_prompt = f"{system_prompt}\n\nContext:\n{context}\n\nQuestion: {prompt}\nAnswer:"
    output = llm(full_prompt, max_tokens=512, stop=["\n"])
    return output["choices"][0]["text"].strip()