# Installation script for Mainer
# Developer: INovomiast2 <ivnovomi> (intra.42.fr)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Check if alias is already set for mainer
if grep -q "alias mainer" ~/.zshrc; then
  echo "${RED}Mainer is already installed!${NC}"
  exit 1
fi

echo "${GREEN}Downloading Mainer...${NC}"
git clone https://github.com/INovomiast2/mainer.git ~/.mainer
echo "${GREEN}Mainer downloaded!${NC}"
echo "${GREEN}Installing Mainer...${NC}"
# Check if python3 is installed
if ! command -v python &> /dev/null; then
  echo "${RED}Python3 is not installed!${NC}"
  exit 1
fi
# Check if pip3 is installed
if ! command -v pip &> /dev/null; then
  echo "${RED}Pip3 is not installed!${NC}"
  exit 1
fi
# Install all the python3 dependencies
pip3 install -r ~/.mainer/requirements.txt
# When all the requirements are installed, add alias to .zshrc
if [ $? -eq 0 ]; then
  echo "${GREEN}Mainer installed!${NC}"
  echo "alias mainer='python3 ~/.mainer/mainer.py'" >> ~/.zshrc
  echo "${GREEN}Mainer alias added!${NC}"
  echo "${GREEN}Mainer is ready to use!${NC}"
else
  echo "${RED}Mainer installation failed!${NC}"
fi
