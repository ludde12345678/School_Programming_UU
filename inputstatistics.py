import inputClasses;
import math;

def CSV():
    filename2 = "CO2Emissions_filtered.csv"
    csv = inputClasses.CsvProcessor(filename2);
    try:
        csv.plotData(['dnk', 'fin', 'isl', 'dnk', 'swe'], 1960, 2014);
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    
def read_text():
    filename = "text.txt";
    f = inputClasses.filestatistics(filename);
    print(f.totalWords());
    print(f.countDiffWords());
    print("enter n to find n most common words");
    n = int(input());4
    print("enter n to find n most uncommon words");
    m = int(input());
    print("Most common words:");
    print(f.commonwords(n));
    print("Most uncommon words");
    print(f.uncommonwords(m));

read_text();