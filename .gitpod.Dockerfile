FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN brew install fzf
RUN curl -sSL https://sdk.cloud.google.com | bash
RUN pip3 install -U crcmod click google-api-python-client googleapiclient
