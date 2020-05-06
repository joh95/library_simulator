#imagen base
FROM python:3.7.4
#Exponer el puerto 80 ()
EXPOSE 8001

#copiar todo el proyecto dentro del contenedor
WORKDIR /project

# Adding requirements file
ADD requirements.txt /project/

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#script para correr el servidor
CMD ["python", "./main.py", "runserver", "0.0.0.0:8001"]




# docker run -itd \
#     --name platform \
#     --network=charlie_network \
#     --link=charlie_postgres \
#     -e "VIRTUAL_HOST=glt.charliebot.ai" \
#     -e "LETSENCRYPT_HOST=glt.charliebot.ai" \
#     -e "LETSENCRYPT_EMAIL=elias@guane.com.co" \
#     platform:glt