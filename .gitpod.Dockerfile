FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN brew install fzf
RUN brew install homebrew/cask/google-cloud-sdk
RUN pip install -U crcmod click google-api-python-client
 
