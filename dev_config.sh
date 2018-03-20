printf "Apt Update.."
apt-get -qqy update
echo -e "\n----- Apt Install.. -----\n"
apt-get -qqy install node git postgresql libpq-dev libyaml-0-2 libyaml-dev
apt-get -qqy install python3 python3-dev python3-pip python3-setuptools
# Pillow requirements
apt-get -qqy install libtiff5-dev libjpeg8 libjpeg8-dev zlib1g zlib1g-dev \
      libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

echo -e "\n----- Enter Project -----\n"
cd /home/vagrant/spinthewheel.gr
echo -e "\n------ Create Virtualenv -----\n"
pip3 install virtualenv && virtualenv -p $(which python3) env

echo "source /home/vagrant/spinthewheel.gr/env/bin/activate" >> /home/vagrant/.profile
source /home/vagrant/spinthewheel.gr/env/bin/activate

echo -e "\n----- Setup Postgres -----\n"
su postgres -c 'createuser -d spin'
su postgres -c 'createdb -O spin spin'

echo -e "\n----- Pip install requirements -----\n"
pip install -r requirements.txt

echo -e "\n----- Npm install requirements -----\n"
npm install

vagrantTip="The shared directory is located at /home/vagrant/spinthewheel.gr\nTo access your shared files: cd spinthewheel.gr"

echo -e $vagrantTip > /etc/motd
