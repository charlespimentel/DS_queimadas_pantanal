FROM continuumio/anaconda3:2022.05
RUN apt-get update && \ 
    git clone https://github.com/charlespimentel/DS_queimadas_pantanal.git /opt/DS_queimadas_pantanal && \
    conda env create -f /opt/DS_queimadas_pantanal/environment.yml
EXPOSE 8888
ENTRYPOINT ["conda", "run", "-n", "queimadas", "jupyter", "notebook", "--notebook-dir=/opt/DS_queimadas_pantanal", "--ip='*'", "--NotebookApp.token=''", "--NotebookApp.password=''", "--port=8888", "--no-browser", "--allow-root"]