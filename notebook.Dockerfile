# This is the image every user's notebook container runs.
# It does NOT need the GPU — GPU work is submitted to Ray and runs there.
# CPU PyTorch is plenty for data prep, experimentation, and job submission.
FROM quay.io/jupyter/scipy-notebook:python-3.11

RUN pip install --no-cache-dir "ray[client]" matplotlib seaborn pandas scikit-learn && \
    pip install --no-cache-dir torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cpu
