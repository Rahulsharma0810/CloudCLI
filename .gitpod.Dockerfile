FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN brew install fzf

RUN curl -sSL https://sdk.cloud.google.com > /tmp/gcl && bash /tmp/gcl --install-dir=~/gcloud --disable-prompts
ENV PATH $PATH:~/gcloud/google-cloud-sdk/bin
