python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/hello_world_sdk-1.3.0-py3-none-any.whl --force-reinstall
