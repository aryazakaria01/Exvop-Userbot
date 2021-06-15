# Docker Tag Images, Using Python Slim Buster.
FROM biansepang/weebproject:buster
# ==========================================
#              Exvop - Userbot
# ==========================================
RUN git clone -b Lynx-Userbot https://github.com/aryazakaria01/Exvop-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --no-cache-dir --upgrade pip setuptools
WORKDIR /root/userbot

# Install Requirements Packages
RUN pip3 install --no-cache-dir -r https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/Lynx-Userbot/requirements.txt

# Finishim
CMD ["python3","-m","userbot"]
