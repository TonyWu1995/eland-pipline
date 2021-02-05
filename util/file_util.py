import csv


def save_csv(file_path, data_list):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data_list:
                writer.writerow(row)
    except Exception as e:
        raise Exception(e)
