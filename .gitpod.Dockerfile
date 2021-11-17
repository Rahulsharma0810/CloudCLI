FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN brew install fzf
RUN brew install --cask google-cloud-sdk
RUN pip3 install -U crcmod click google-api-python-client googleapiclient
