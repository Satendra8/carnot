echo "BUILD START"
python3.9 -m pip install -r requirments.txt
python3.9 manage.py collectstatic --no-input --clear
echo "BUILD END"