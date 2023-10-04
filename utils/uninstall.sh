# Uninstall Script for mainer.
# Developer: INovomiast2 <ivnovomi> (intra.42.fr)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Check if alias is already set for mainer
if ! grep -q "alias mainer" ~/.zshrc; then
  echo "${GREEN}Mainer is not installed!${NC}"
  exit 1
fi

echo "${GREEN}Uninstalling Mainer...${NC}"
# Remove GitPython package
pip3 uninstall -y GitPython
# Remove alias from .zshrc
sed -i '/alias mainer/d' ~/.zshrc
# Remove mainer directory
rm -rf ~/.mainer
echo "${GREEN}Mainer uninstalled!${NC}"