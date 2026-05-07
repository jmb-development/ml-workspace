FROM rayproject/ray:2.55.1-py311-gpu

# PyTorch with CUDA — GPU training code runs here, not in the notebooks
RUN pip install --no-cache-dir torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu121
