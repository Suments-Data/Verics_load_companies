import csv
import requests
import json


token = "TU TOKEN VA AQUI"
# https://www.suments.com
# https://developers.suments.com
# https://developers.suments.com/#api-Acci%C3%B3n-AddCompany


def write_rel_companies_analysis(companies):

    data_file = open('rel_companies_analysis.csv', 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for company in companies:
        if count == 0:
            header = company.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(company.values())

    data_file.close()
    return


def read_companies():
    companies = list()
    tmp = {
        "company_name": "",
        "company_domain": "",
        "company_email": "",
        "company_contact": "",
        "company_phone": ""
    }
    with open('companies.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                line_count += 1
                if row[0] == '':
                    print(
                        f"Error in line {line_count}, column [0]. Mandatory parameter 'company_name'")
                    print("https://developers.suments.com/#api-Acci%C3%B3n-AddCompany")
                    exit()
                if row[1] == '':
                    print(
                        f"Error in line {line_count}, column [1]. Mandatory parameter 'company_domain'")
                    print("https://developers.suments.com/#api-Acci%C3%B3n-AddCompany")
                    exit()
                tmp = {
                    "company_name": f"{row[0]}",
                    "company_domain": f"{row[1]}",
                    "company_email": f"{row[2]}",
                    "company_contact": f"{row[3]}",
                    "company_phone": f"{row[4]}"
                }
        companies.append(tmp)

    return companies


"""
https://developers.suments.com/#api-Acci%C3%B3n-AddCompany
"""


def send_companies(companies):
    url = 'https://api.suments.com/api2/AAddCompany'
    tmp = {
        "company_name": "",
        "company_domain": "",
        "id_analylis": ""
    }
    minimal = list()
    for company in companies:

        myComp = {
            "company_name": f"{company['company_name']}",
            "company_domain": f"{company['company_domain']}",
            "company_email": f"{company['company_email']}",
            "company_contact": f"{company['company_contact']}",
            "company_phone": f"{company['company_phone']}",
            "token": f"{token}"
        }
        try:
            x = requests.post(url, data=myComp)
            data = json.loads(x.text)
            tmp = {
                "company_name": f"{company['company_name']}",
                "company_domain": f"{company['company_domain']}",
                "id_analylis": data["payload"]["id_analysis"]
            }
            minimal.append(tmp)
        except Exception as e:
            print(e)

    return minimal


if __name__ == "__main__":

    companies = read_companies()
    companies_min = send_companies(companies)
    write_rel_companies_analysis(companies_min)
