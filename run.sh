docker pull stephentyndall/ailovecraft:latest

docker run -d -p 5000:5000 stephentyndall/ailovecraft:latest

echo "Waiting for site to load"
for i in {1..5}
do
    sleep 2
    echo "-"
done

python -m webbrowser -t "http://localhost:5000"
