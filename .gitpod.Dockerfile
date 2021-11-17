FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN brew install fzf

RUN pip install -U crcmod click google-api-python-client

RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts
 
