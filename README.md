# Overbond-Assessment

This application parses through an Excel data file to extract CleanBid, CleanAsk and Last Price values to plot them against their corresponding Issuance Dates. 

The python programming language, matplotlib, and pandas libraries are used throughout this application. 
Python was used because it is a high level language providing exceptional readability and state of the art graphing solutions via matplotlib and efficient data manipulation and analysis through the pandas software library. 

Provided if more time were given, automated testing and a more accurate time series would be included in the horizontal axis of the scatter plot. However, the application does provide the desired output from the sample file given. 

This application uses an approach where each type of desired value is within a distinct and labeled column of the Excel file. Also note that each type of value begins with a specific prefix. For example, all CleanBid values begin with "BPr." This allows us to check each desired column and extract all cells that begin with the specific prefix and slice the extracted value to obtain the number a float representation. Each type of value is extracted and then plotted against the corresponding Issuance Date on a scattter plot. 

# Executing The Application

To execute the application please make sure python, matplotlib, and pandas are all downloaded along with a supporting IDE. Furthermore, all source files are placed in the "src" folder and all data files are in the "datafiles" folder. To avoid complications, please ensure that the "src" and "datafiles" folders are within the same directory, and the name of the data file is "Book1.xlsx" and all data is on "Sheet1."
