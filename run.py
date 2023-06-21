import random
import time
import sys
import os
import pandas
import inspect
from colorama import Fore, Back, Style
from utils.core import load_pipelines_from_project, get_params, load_pipelines_from_project, get_transformation
import psutil

initial_memory = psutil.Process().memory_info().rss

pipeline, sources = get_params()
if pipeline is None:
    all = load_pipelines_from_project()
    raise Exception(f'Please specify pipeline to load from the following options: ' +
                    ",".join([p['slug'] for p in all]))
else:
    pipeline = load_pipelines_from_project(pipeline)[0]
    if "sources" not in pipeline:
        raise Exception(
            f"Pipeline {pipeline['slug']} is missing sources on the YML")
    else:
        sources = pipeline['sources']


if sources is None or len(sources) == 0:
    raise Exception(
        f'Missing CSV Files to for source from when running pipeline {pipeline}.\n Hint: please specify the name of the CSV files on the project.yml')
else:
    for i in range(len(sources)):
        if ".csv" not in sources[i]:
            sources[i] = sources[i] + ".csv"


dfs = []
for source in sources:
    dfs.append(pandas.read_csv("sources/"+source))

df_out = None
count = 0


for t in pipeline['transformations']:
    count += 1
    print(Fore.WHITE +
          f"[] Applying {count} transformation {t} with {len(dfs)} sources...")
    run, _in, _out = get_transformation(pipeline['slug'], t)
    if df_out is not None:
        dfs[0] = df_out
        
    args_spect = inspect.getfullargspec(run)
    df_out = run(*dfs[:len(args_spect.args)])

file_name = source.split('.')[0]
df_out.to_csv(
    f"output/{pipeline['slug']}{str(round(time.time()))}.csv")


final_memory = psutil.Process().memory_info().rss

# Calculate the memory usage difference
memory_usage = final_memory - initial_memory

print(f"Memory usage: {memory_usage} bytes")
print(f"Memory usage: {memory_usage / 1024} kilobytes")
print(f"Memory usage: {memory_usage / (1024 * 1024)} megabytes")