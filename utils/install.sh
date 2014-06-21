#!/bin/bash

BREW_MODS=("openssl" "wget" "python3" "python")
PIP_MODS=("pyserial")

cat <<EOF
	This script will install these brew modules: 
		${BREW_MODS[@]}
	and these pip modules: 
		${PIP_MODS[@]}
	Please install xcode stuff if prompted
	Press any key to continue
EOF
read -n 1 -s

die(){
	echo "$1"; exit 1
}
# install stuff, used to install other stuff
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)" #|| die "Could not get root"
brew update
brew doctor

for mod in "${BREW_MODS[@]}"; do
	brew install ${mod} || die "Failed to install ${mod}"
done

for mod in "${PIP_MODS[@]}"; do 
	pip3 install ${mod} || die "Failed to install ${mod}"
done

echo "finished installing"
