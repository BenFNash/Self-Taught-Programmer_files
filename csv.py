import csv

with open("st.csv", "w", newline=''):
    w = csv.writer(f, delimiter=",")
    w.writerow(['one','two','three'])