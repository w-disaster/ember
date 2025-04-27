DIR="./base_pe_dir/family_test/"
mkdir -p "$DIR"
docker run --rm -v "$(pwd):/src/" cdrx/pyinstaller-windows "pyinstaller --onefile --distpath $DIR hello_world.py"