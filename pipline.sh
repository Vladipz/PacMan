Green="\033[0;32m"
Yellow="\033[0;33m"
NC="\033[0m"
echo -e "${Yellow}Starting tests...${NC}"
pytest ./tests/
echo -e "${Green}Tests finished${NC}"
echo -e "${Yellow}Starting linting...${NC}"
flake8 . -v
echo -e "${Green}Linting finished${NC}"
