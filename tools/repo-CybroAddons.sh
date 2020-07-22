cd ~/server/11/sources
git clone --depth 1 --branch 11.0 --single-branch https://github.com/CybroOdoo/CybroAddons.git CybroOdoo-CybroAddons
cd ~/server/11/sources
find . -name "oca_dependencies.txt" -type f -delete
cd ~/server/11/
sources bin/activate
cd ~/server/11
./maintainer-quality-tools/travis/clone_oca_dependencies sources/ .
find ~/server/11/sources -mindepth 1 -maxdepth 1 -type d | sort | tr '\n' ','