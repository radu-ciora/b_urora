import huggingface_hub

# single file download
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="gpt2", filename="config.json", local_dir="Z:\\research\\openAI\\gpt_repo",
                local_dir_use_symlinks="auto")

# entire repo download
from huggingface_hub import snapshot_download
snapshot_download(repo_id="lysandre/arxiv-nlp", revision="refs/pr/1", local_dir="Z:\\research\\openAI\\lysandre", local_dir_use_symlinks="auto")
