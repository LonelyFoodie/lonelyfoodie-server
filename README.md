# lonelyfoodie-server

##### To build and run this project:
1. Install Docker
2. Run this command
``` bash
git clone https://github.com/LonelyFoodie/lonelyfoodie-server.git
cd lonelyfoodie-server
docker build -t lonelyfoodie-server .
docker run -p 5000:5000 lonelyfoodie-server
```
3. Visit http://localhost:5000/

Or just...
1. Install Python
2. Run this command

``` bash
git clone https://github.com/LonelyFoodie/lonelyfoodie-server.git
cd lonelyfoodie-server
pip install -r requirements.txt
python app.py
```
3. Visit http://localhost:5000/
