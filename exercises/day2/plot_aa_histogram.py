import sys
from collections import Counter
import csv
import seaborn as sns
import pandas as pd

def aa_count(input_file_path, output_file_name="aa_count.csv"):
    counter = Counter()
    with open(input_file_path,"r") as file:
        for line in file:
            if line[0] == ">":
                continue
            line = line.rstrip("\n") # removes linebreak character
            counter = counter + Counter(line)
    with open(output_file_name,"w") as output:
        aa_writer = csv.DictWriter(output, fieldnames=["aa","count"], extrasaction="ignore")
        aa_writer.writeheader()
        for key,item in counter.items():
            aa_writer.writerow({"aa":key, "count":item})

def barplot(filename, filename_output = "output.png"):
    dataframe = pd.read_csv(filename)
    sns_plot = sns.catplot(data= dataframe, kind="bar", x=f"{dataframe.columns[0]}", y=f"{dataframe.columns[1]}")
    fig = sns_plot.fig
    fig.savefig(filename_output)


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    aa_count(input_file_path)
    barplot("aa_count.csv")