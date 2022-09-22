
import csv
from logging import exception;
import matplotlib.pyplot as plot;
import smooth;

#class that gathers statistics from a text document
class filestatistics:
    
    
    def __init__(self, filename):
        self.file = open(filename, "r");
        self.text = self.file.read();
        
    def totalWords(self):
        counter = 0;
        for c in self.text.split(" "):
            counter += 1;
        return counter;
    
    def countDiffWords(self):
        characterdict = {};
        words = [ i.strip(" \n").strip("?").strip(".") for i in self.text.split(" ")]
        for c in words:
            
            if not c in characterdict.keys():
                characterdict[c] = 1;
            else:
                characterdict[c] += 1;
                
        return characterdict;
    
    def commonwords(self, n):
        worddict = self.countDiffWords();
        commonwords = [];
        for i in range(n):
            ocurrence = 0;
            highestword = "";
            for key in worddict:
                if(worddict[key] > ocurrence):
                    ocurrence = worddict[key];
                    highestword = key;
            del worddict[highestword];
            commonwords.append(highestword);
        return commonwords;

    def uncommonwords(self, n):
        worddict = self.countDiffWords();
        uncommonwords = [];
        for i in range(n):
            ocurrence = 1;
            lowestWord = "";
            for key in worddict:
                if(worddict[key] <= ocurrence):
                    ocurrence = worddict[key];
                    lowestWord = key;
            del worddict[lowestWord]
            uncommonwords.append(lowestWord);
            
            
        return uncommonwords;



#class that reads and processes a csv file
class CsvProcessor:
    processedcsv = {};
    def __init__(self, filename):
        with open(filename, "r") as f:
            reader = csv.reader(f);
            self.load_csv(reader);
      
    def load_csv(self, reader):
        self.processedcsv = {str.lower(k[1]):[float(x) for x in k[3:]]for k in reader}
        del self.processedcsv["country code"];
            
    def plotData(self, countries, starttime, endtime):
        # start/endtime needs to be between 1960 - 2014
        if(starttime < 1960 or endtime > 2014):
            raise exception("Error, Bad Plot Time");
        time = list(range(starttime, endtime+1));
        fig, ax = plot.subplots();
        for x in countries:
            line = ax.plot(time, smooth.smooth_a(self.processedcsv[x], 5), label=(x))
            ax.plot(time, smooth.smooth_b(self.processedcsv[x], 5), linestyle="--", color=line[-1].get_color())
            ax.plot(time, self.processedcsv[x], linestyle=":",color=line[-1].get_color())

            
        plot.legend(fontsize="small");
        ax.set(xlabel="Time(Years)", ylabel="CO2 Emissions (kt)", title="Yearly Emissions of CO2 by Country(Source=me)")
        plot.show();
    
    
    def getProcessedcsv(self):
        return self.processedcsv;
    
    