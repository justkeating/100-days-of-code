# thank you Corey Schafer for read write csv tutorial
import csv
# random thing about paths, need to include the where file is being run. Where this is being run is thought to be at 100 days of code repo one dir up
with open('paddles/paddleDatabase/paddlesSpreadSheet.csv', 'r') as csv_file:
    # DictReader is used instead of reader so we can reference the column description instead of index. easier to write and read
    csv_reader = csv.DictReader(csv_file)
    with open('paddles_above_200.csv', 'w') as new_file:
        field_names = ['Company','Paddle','Core Thickness (mm)','Condition','Price','Shape','Manufacturing Process','Surface Texture','Surface Material','Core Material','Spin RPM','Spin Percentile','Length (in)','Width (in)','Handle Length (in)','Static Weight (oz)','Swing Weight','Swing Weight Percentile','Twist Weight','Twist Weight Percentile','Balance Point (cm)','Balance Point Percentile','Serve Speed-MPH (Power)','Power Percentile','Punch Volley Speed-MPH (Pop)','Pop Percentile','Surface Hardness (Shore D)']
        # field_names will be what is being written to so we can adjust what we want to write
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            line['Price'] = line['Price'].replace('$', '' )
            line['Price'] = float(line['Price'])
            if line['Price'] >= 200:
                csv_writer.writerow(line)
